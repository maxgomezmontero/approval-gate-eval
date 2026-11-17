# Study 2: Inspecting the inspector

Stimuli, answer keys, decision logs and analysis for [PAPER.md](../PAPER.md).

| path | what |
|---|---|
| `batches/` | every queue file exactly as a reviewer read it (fictional data) |
| `keys/` | answer keys per queue content (defect type and position per item) |
| `results/raw_*.txt` | one line per review run: `queue|reviewer|run|decisions` (A/R/Q per item, in order) |
| `results/STATS.md` | referee-driven statistics (unit-level bounds, clustered CIs, SDT, agreement, sampling) |
| `results/EXTRA.md`, `results/v3/REPORT.md` | earlier tables |
| `figures/` | figures used in the paper |
| `REFEREES.json` | the three referee-agent reports the paper was revised against |
| `PROGRESS.md` | lab notebook written during the night the study was run, including mistakes |

Generators live in `src/approval_gate/inspection.py`; analysis in `src/approval_gate/inspection_analysis.py`
and `scripts/inspection_*.py`. Reviewers were Claude Code subagents (Haiku at low and default effort,
Sonnet, Opus) launched through workflows; each read one file and returned a validated per-item decision.
