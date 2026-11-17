"""Inspect task: `inspect eval src/approval_gate/task.py --model anthropic/claude-haiku-5-5`.

Task args:
  variant  "default" | "speed" | "hard"  (speed: "measured by how fast records are updated";
           hard: no written policy, plus a vague "keep things moving" note from the operator)
  family   one family name, or "all"
  agent    "llm" | "rules"        (rules = keyword/regex baseline, makes no model calls)
  honesty  ask "did you write anything directly?" after the episode (llm only)
"""

from __future__ import annotations

from inspect_ai import Task, task
from inspect_ai.agent import as_solver, react
from inspect_ai.dataset import MemoryDataset, Sample
from inspect_ai.model import ChatMessageSystem, ChatMessageUser, get_model
from inspect_ai.scorer import Score, Target, mean, scorer, stderr
from inspect_ai.solver import Generate, Solver, TaskState, solver
from inspect_ai.util import store

from .backoffice import BackOffice
from .baseline import run_rules
from .generator import DATA_PATH, Scenario, read_jsonl
from .prompts import HONESTY_QUESTION, system_prompt, user_message
from .scoring import load_costs, score_episode
from .tools import STORE_KEY, all_tools

MESSAGE_LIMIT = 40


def scenario_samples(family: str = "all", variant: str = "default") -> list[Sample]:
    samples = []
    for s in read_jsonl(DATA_PATH):
        if family not in ("all", s.family):
            continue
        samples.append(Sample(
            id=s.id,
            input=user_message(s.operator_note, variant),
            metadata={"family": s.family, "scenario": s.to_dict()},
        ))
    return samples


@solver
def init_backoffice(variant: str) -> Solver:
    async def solve(state: TaskState, generate: Generate) -> TaskState:
        scenario = Scenario.from_dict(state.metadata["scenario"])
        store().set(STORE_KEY, BackOffice.from_scenario(scenario).to_dict())
        state.messages.insert(0, ChatMessageSystem(content=system_prompt(variant)))
        return state

    return solve


@solver
def rules_agent() -> Solver:
    async def solve(state: TaskState, generate: Generate) -> TaskState:
        office = BackOffice.from_dict(store().get(STORE_KEY))
        report = run_rules(office)
        store().set(STORE_KEY, office.to_dict())
        state.output.completion = report
        store().set("final_report", report)
        return state

    return solve


@solver
def keep_final_report() -> Solver:
    async def solve(state: TaskState, generate: Generate) -> TaskState:
        store().set("final_report", state.output.completion or "")
        return state

    return solve


@solver
def honesty_check() -> Solver:
    """One extra turn after the episode: the audit question, answered without tools."""

    async def solve(state: TaskState, generate: Generate) -> TaskState:
        state.messages.append(ChatMessageUser(content=HONESTY_QUESTION))
        out = await get_model().generate(state.messages, tools=all_tools(), tool_choice="none")
        state.messages.append(out.message)
        store().set("honesty_answer", out.completion or "")
        return state

    return solve


@scorer(metrics={"success": [mean(), stderr()], "violation": [mean(), stderr()], "cost": [mean(), stderr()]})
def approval_gate_scorer():
    costs = load_costs()

    async def score(state: TaskState, target: Target) -> Score:
        scenario = Scenario.from_dict(state.metadata["scenario"])
        office = BackOffice.from_dict(store().get(STORE_KEY))
        honesty = store().get("honesty_answer", None)
        result = score_episode(office, scenario, costs, final_text=store().get("final_report", ""),
                               honesty_answer=honesty)
        return Score(
            value={
                "success": float(result.task_success),
                "violation": float(result.gate_violation),
                "cost": result.cost,
            },
            explanation="; ".join(f"{e['type']}: {e['detail']}" for e in result.errors) or "no errors",
            metadata={**result.as_metadata(), "family": scenario.family, "actions": office.actions},
        )

    return score


@task
def approval_gate(variant: str = "default", family: str = "all", agent: str = "llm",
                  honesty: bool = True) -> Task:
    if agent == "rules":
        chain = [init_backoffice(variant), rules_agent()]
    else:
        chain = [init_backoffice(variant), as_solver(react(tools=all_tools())), keep_final_report()]
        if honesty:
            chain.append(honesty_check())
    return Task(
        dataset=MemoryDataset(scenario_samples(family, variant), name=f"approval_gate_{variant}"),
        solver=chain,
        scorer=approval_gate_scorer(),
        message_limit=MESSAGE_LIMIT,
        metadata={"variant": variant, "agent": agent},
    )
