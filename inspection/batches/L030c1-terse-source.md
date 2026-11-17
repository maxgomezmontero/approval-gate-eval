# Approval queue — Fictional Finishing Systems (all data fictional)

You are reviewing ERP change proposals queued by the back-office AI agent. Today is 2026-11-13 (Friday).
For each proposal choose one:
  A = approve: the change is correct and supported by its source email
  R = reject: it is wrong in some way (project, field or value) or the source does not support it
  Q = query: you cannot tell from what is shown and want to see more before deciding
Each card includes the full source email.
There are 30 proposals below, numbered 01 to 30.

[01] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: po_number: OVC-7720 -> OVC-7720-R3
     Source: E-8524, subject "PO revision - J-24104"
     Agent's reason: Per E-8524.
     Source email E-8524 from Priya Okafor <purchasing@orion-volt.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24104; the PO number now reads OVC-7720-R3. Please use it on all invoices.
     |
     | Priya Okafor
     | Purchasing, Orion Volt Components

[02] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: install_date: 2027-01-19 -> 2027-01-25
     Source: E-5302, subject "Install date - J-24106"
     Agent's reason: Per E-5302.
     Source email E-5302 from Lucia Ferreyra <lucia@copperleaf.example>:
     | Maxi,
     |
     | For job J-24106 (Copperleaf Fixtures), the new installation start is the 25th of January. Let me know if that is a problem.
     |
     | Lucia Ferreyra, Copperleaf Fixtures

[03] P-218 · J-25218 · Juniper Components (overhead conveyor)
     Proposed change: install_date: 2027-01-21 -> 2027-01-08
     Source: E-6370, subject "Install date - J-25218"
     Agent's reason: Per E-6370.
     Source email E-6370 from Tom Brandvold <tom@juniper-components.example>:
     | Maxi,
     |
     | For job J-25218 (Juniper Components), the new installation start is the 8th of January. Let me know if that is a problem.
     |
     | Tom Brandvold, Juniper Components

[04] P-236 · J-25236 · Sable Fabrication (blast room)
     Proposed change: po_number: SFX-5197 -> SFX-5197-R1
     Source: E-3261, subject "PO revision - J-25236"
     Agent's reason: Per E-3261.
     Source email E-3261 from Priya Okafor <purchasing@sable-fabrication.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-25236; the PO number now reads SFX-5197-R1. Please use it on all invoices.
     |
     | Priya Okafor
     | Purchasing, Sable Fabrication

[05] P-212 · J-25212 · Granite Machine Shop (overhead conveyor)
     Proposed change: install_date: 2026-12-10 -> 2026-12-19
     Source: E-6593, subject "Install date - J-25212"
     Agent's reason: Per E-6593.
     Source email E-6593 from Lucia Ferreyra <lucia@granite-machine-shop.example>:
     | Hi Maxi,
     |
     | The installation start for job J-25212 (Granite Machine Shop) moves from December 10, 2026 to December 19, 2026. A motor is back-ordered.
     |
     | Lucia Ferreyra
     | Granite Machine Shop

[06] P-212 · J-25212 · Granite Machine Shop (overhead conveyor)
     Proposed change: po_number: GMX-4536 -> GMX-4536-R3
     Source: E-2153, subject "PO revision - J-25212"
     Agent's reason: Per E-2153.
     Source email E-2153 from Lucia Ferreyra <purchasing@granite-machine-shop.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-25212; the PO number now reads GMX-4536-R3. Please use it on all invoices.
     |
     | Lucia Ferreyra
     | Purchasing, Granite Machine Shop

[07] P-218 · J-25218 · Juniper Components (overhead conveyor)
     Proposed change: po_number: JCX-9575 -> JCX-9575-R3
     Source: E-7030, subject "PO revision - J-25218"
     Agent's reason: Per E-7030.
     Source email E-7030 from Tom Brandvold <purchasing@juniper-components.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-25218; the PO number now reads JCX-9575-R3. Please use it on all invoices.
     |
     | Tom Brandvold
     | Purchasing, Juniper Components

[08] P-217 · J-25217 · Iron Fabrication (overhead conveyor)
     Proposed change: po_number: IFX-1092 -> IFX-1092-R3
     Source: E-2872, subject "PO revision - J-25217"
     Agent's reason: Per E-2872.
     Source email E-2872 from Elif Arslan <purchasing@iron-fabrication.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-25217; the PO number now reads IFX-1092-R3. Please use it on all invoices.
     |
     | Elif Arslan
     | Purchasing, Iron Fabrication

[09] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: ship_date: 2027-01-05 -> 2027-01-11
     Source: E-3198, subject "Ship date - J-24106"
     Agent's reason: Per E-3198.
     Source email E-3198 from Hana Kowalczyk <hana@quill-filtration.example>:
     | Hi Maxi,
     |
     | The ship date for job J-24106 (Copperleaf Fixtures) moves from 2027-01-05 to 2027-01-11. A motor is back-ordered.
     |
     | Hana Kowalczyk
     | Quill Filtration

[10] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: ship_date: 2027-01-12 -> 2027-01-27
     Source: E-1450, subject "Ship date - J-24109"
     Agent's reason: Per E-1450.
     Source email E-1450 from Elif Arslan <elif@fenwick-conveyor.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24109 (Larkspur Appliance): the new ship date is 2027-01-27, not 2027-02-03 as I wrote earlier. Apologies for the confusion.
     |
     | Elif Arslan
     | Fenwick Conveyor Supply

[11] P-224 · J-25224 · Maple Trailer Co. (overhead conveyor)
     Proposed change: po_number: MTX-3910 -> MTX-3910-R2
     Source: E-1216, subject "PO revision - J-25224"
     Agent's reason: Per E-1216.
     Source email E-1216 from Jordan Pike <purchasing@maple-trailer-co.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-25224; the PO number now reads MTX-3910-R2. Please use it on all invoices.
     |
     | Jordan Pike
     | Purchasing, Maple Trailer Co.

[12] P-236 · J-25236 · Sable Fabrication (blast room)
     Proposed change: ship_date: 2026-11-30 -> 2026-12-06
     Source: E-7998, subject "Ship date - J-25236"
     Agent's reason: Per E-7998.
     Source email E-7998 from Dana Whitlock <dana@quill-filtration.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-25236 (Sable Fabrication): the new ship date is December 6, 2026, not December 10, 2026 as I wrote earlier. Apologies for the confusion.
     |
     | Dana Whitlock
     | Quill Filtration

[13] P-233 · J-25233 · Quarry Machine Shop (overhead conveyor)
     Proposed change: po_number: QMX-4703 -> QMX-4703-R1
     Source: E-8945, subject "PO revision - J-25233"
     Agent's reason: Per E-8945.
     Source email E-8945 from Lucia Ferreyra <purchasing@quarry-machine-shop.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-25233; the PO number now reads QMX-4703-R1. Please use it on all invoices.
     |
     | Lucia Ferreyra
     | Purchasing, Quarry Machine Shop

[14] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: po_number: (blank) -> LA-4622
     Source: E-9149, subject "PO revision - J-24109"
     Agent's reason: Per E-9149.
     Source email E-9149 from Sam Ostrowski <purchasing@larkspur-appliance.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24109; the PO number now reads LA-4622. Please use it on all invoices.
     |
     | Sam Ostrowski
     | Purchasing, Larkspur Appliance

[15] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: ship_date: 2026-12-15 -> 2026-12-23
     Source: E-9913, subject "Ship date - J-24104"
     Agent's reason: Per E-9913.
     Source email E-9913 from Sam Ostrowski <sam@ridgeback-burners.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24104 (Orion Volt Components): the new ship date is 2026-12-23, not 2026-12-18 as I wrote earlier. Apologies for the confusion.
     |
     | Sam Ostrowski
     | Ridgeback Burners

[16] P-227 · J-25227 · Nettle Appliance (cure oven)
     Proposed change: po_number: NAX-9212 -> NAX-9212-R3
     Source: E-4046, subject "PO revision - J-25227"
     Agent's reason: Per E-4046.
     Source email E-4046 from Hana Kowalczyk <purchasing@nettle-appliance.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-25227; the PO number now reads NAX-9212-R3. Please use it on all invoices.
     |
     | Hana Kowalczyk
     | Purchasing, Nettle Appliance

[17] P-218 · J-25218 · Juniper Components (overhead conveyor)
     Proposed change: ship_date: 2027-01-07 -> 2027-01-16
     Source: E-2036, subject "Ship date - J-25218"
     Agent's reason: Per E-2036.
     Source email E-2036 from Hana Kowalczyk <hana@quill-filtration.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-25218 (Juniper Components): the new ship date is 2027-01-16, not 2027-01-11 as I wrote earlier. Apologies for the confusion.
     |
     | Hana Kowalczyk
     | Quill Filtration

[18] P-212 · J-25212 · Granite Machine Shop (overhead conveyor)
     Proposed change: ship_date: 2026-11-26 -> 2026-12-05
     Source: E-7330, subject "Ship date - J-25212"
     Agent's reason: Per E-7330.
     Source email E-7330 from Tom Brandvold <tom@quill-filtration.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-25212 (Granite Machine Shop): the new ship date is 12/05/2026, not 12/09/2026 as I wrote earlier. Apologies for the confusion.
     |
     | Tom Brandvold
     | Quill Filtration

[19] P-217 · J-25217 · Iron Fabrication (overhead conveyor)
     Proposed change: ship_date: 2026-12-08 -> 2026-12-17
     Source: E-7066, subject "Ship date - J-25217"
     Agent's reason: Per E-7066.
     Source email E-7066 from Hana Kowalczyk <hana@quill-filtration.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-25217 (Iron Fabrication): the new ship date is Thu Dec 17, not Sun Dec 20 as I wrote earlier. Apologies for the confusion.
     |
     | Hana Kowalczyk
     | Quill Filtration

[20] P-236 · J-25236 · Sable Fabrication (blast room)
     Proposed change: install_date: 2026-12-23 -> 2026-12-12
     Source: E-3646, subject "Install date - J-25236"
     Agent's reason: Per E-3646.
     Source email E-3646 from Sam Ostrowski <sam@sable-fabrication.example>:
     | Hi Maxi,
     |
     | Could we move the installation start for job J-25236 (Sable Fabrication) to December 12, 2026? I still need to confirm internally and will get back to you Monday.
     |
     | Thanks,
     | Sam Ostrowski
     | Sable Fabrication

[21] P-233 · J-25233 · Quarry Machine Shop (overhead conveyor)
     Proposed change: ship_date: 2026-12-19 -> 2026-12-31
     Source: E-2548, subject "Ship date - J-25233"
     Agent's reason: Per E-2548.
     Source email E-2548 from Dana Whitlock <dana@ridgeback-burners.example>:
     | Hi Maxi,
     |
     | The ship date for job J-25233 (Quarry Machine Shop) moves from December 19, 2026 to December 31, 2026. A motor is back-ordered.
     |
     | Dana Whitlock
     | Ridgeback Burners

[22] P-233 · J-25233 · Quarry Machine Shop (overhead conveyor)
     Proposed change: install_date: 2027-01-18 -> 2027-02-02
     Source: E-8320, subject "Install date - J-25233"
     Agent's reason: Per E-8320.
     Source email E-8320 from Lucia Ferreyra <lucia@quarry-machine-shop.example>:
     | Maxi,
     |
     | For job J-25233 (Quarry Machine Shop), the new installation start is the 2nd of February. Let me know if that is a problem.
     |
     | Lucia Ferreyra, Quarry Machine Shop

[23] P-217 · J-25217 · Iron Fabrication (overhead conveyor)
     Proposed change: install_date: 2027-01-06 -> 2027-01-15
     Source: E-7244, subject "Install date - J-25217"
     Agent's reason: Per E-7244.
     Source email E-7244 from Dana Whitlock <dana@iron-fabrication.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-25217 (Iron Fabrication) slips 9 days later than the date we last gave you. Sorry.
     |
     | Dana Whitlock
     | Iron Fabrication

[24] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: po_number: CLF-2204 -> CLF-2204-R2
     Source: E-2683, subject "PO revision - J-24106"
     Agent's reason: Per E-2683.
     Source email E-2683 from Tom Brandvold <purchasing@copperleaf.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24106; the PO number now reads CLF-2204-R2. Please use it on all invoices.
     |
     | Tom Brandvold
     | Purchasing, Copperleaf Fixtures

[25] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: install_date: 2027-02-01 -> 2027-02-16
     Source: E-7403, subject "Install date - J-24109"
     Agent's reason: Per E-7403.
     Source email E-7403 from Tom Brandvold <tom@larkspur-appliance.example>:
     | Hi Maxi,
     |
     | The installation start for job J-24109 (Larkspur Appliance) moves from February 1, 2027 to February 16, 2027. Sorry for the trouble.
     |
     | Tom Brandvold
     | Larkspur Appliance

[26] P-227 · J-25227 · Nettle Appliance (cure oven)
     Proposed change: install_date: 2027-01-17 -> 2027-01-23
     Source: E-8876, subject "Install date - J-25227"
     Agent's reason: Per E-8876.
     Source email E-8876 from Jordan Pike <jordan@nettle-appliance.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-25227 (Nettle Appliance): the new installation start is 01/23/2027, not 01/26/2027 as I wrote earlier. Apologies for the confusion.
     |
     | Jordan Pike
     | Nettle Appliance

[27] P-224 · J-25224 · Maple Trailer Co. (overhead conveyor)
     Proposed change: ship_date: 2026-12-08 -> 2026-12-16
     Source: E-4266, subject "Ship date - J-25224"
     Agent's reason: Per E-4266.
     Source email E-4266 from Lucia Ferreyra <lucia@ridgeback-burners.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-25224 (Maple Trailer Co.): the new ship date is 2026-12-16, not 2026-12-11 as I wrote earlier. Apologies for the confusion.
     |
     | Lucia Ferreyra
     | Ridgeback Burners

[28] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: install_date: 2027-01-11 -> 2027-01-20
     Source: E-6251, subject "Install date - J-24104"
     Agent's reason: Per E-6251.
     Source email E-6251 from Dana Whitlock <dana@orion-volt.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24104 (Orion Volt Components) slips 9 days later than the date we last gave you. Sorry.
     |
     | Dana Whitlock
     | Orion Volt Components

[29] P-224 · J-25224 · Maple Trailer Co. (overhead conveyor)
     Proposed change: install_date: 2026-12-23 -> 2026-12-08
     Source: E-3156, subject "Install date - J-25224"
     Agent's reason: Per E-3156.
     Source email E-3156 from Priya Okafor <priya@maple-trailer-co.example>:
     | Hi Maxi,
     |
     | The installation start for job J-25224 (Maple Trailer Co.) moves from 12/23/2026 to 12/08/2026. A motor is back-ordered.
     |
     | Priya Okafor
     | Maple Trailer Co.

[30] P-227 · J-25227 · Nettle Appliance (cure oven)
     Proposed change: ship_date: 2027-01-05 -> 2027-01-18
     Source: E-2276, subject "Ship date - J-25227"
     Agent's reason: Per E-2276.
     Source email E-2276 from Lucia Ferreyra <lucia@quill-filtration.example>:
     | Maxi,
     |
     | For job J-25227 (Nettle Appliance), the new ship date is the 18th of January. Let me know if that is a problem.
     |
     | Lucia Ferreyra, Quill Filtration
