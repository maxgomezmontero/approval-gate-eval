# Approval queue — Fictional Finishing Systems (all data fictional)

You are reviewing ERP change proposals queued by the back-office AI agent. Today is 2026-11-13 (Friday).
For each proposal choose one:
  A = approve: the change is correct and supported by its source email
  R = reject: it is wrong in some way (project, field or value) or the source does not support it
  Q = query: you cannot tell from what is shown and want to see more before deciding
Each card includes the full source email.
There are 30 proposals below, numbered 01 to 30.

## Emails received after the agent built this queue (newest last)

L01 from Lucia Ferreyra <purchasing@orion-volt.example>: Just confirming the PO for job J-24104 is OVC-7720-R1, as in my earlier email.
L02 from Hana Kowalczyk <hana@kestrel-cabinet.example>: Thanks for the quick reply on job J-24102. No other changes from our side.
L03 from Priya Okafor <priya@tamsin-farm.example>: Following up on my earlier email about job J-24105: please disregard the date I sent. The installation start is now January 1, 2027.
L04 from Elif Arslan <purchasing@tamsin-farm.example>: Just confirming the PO for job J-24105 is TFE-1180-R3, as in my earlier email.
L05 from Lucia Ferreyra <lucia@quill-filtration.example>: Confirming the date in my earlier email about job J-24102 stands: 2026-12-02.
L06 from Sam Ostrowski <sam@saltmarsh-controls.example>: Confirming the date in my earlier email about job J-24109 stands: 2027-01-18.
L07 from Tom Brandvold <tom@redfern-steel.example>: Confirming the date in my earlier email about job J-24107 stands: 2026-11-23.
L08 from Priya Okafor <purchasing@bluegill-tractor.example>: Just confirming the PO for job J-24101 is BTW-55102-R1, as in my earlier email.
L09 from Lucia Ferreyra <purchasing@bluegill-tractor.example>: Just confirming the PO for job J-24108 is BTW-55187-R2, as in my earlier email.
L10 from Hana Kowalczyk <hana@orion-volt.example>: Confirming the date in my earlier email about job J-24110 stands: 2027-02-26.

## Proposals

[01] P-101 · J-24101 · Bluegill Tractor Works (paint booth line (2 crossdraft booths))
     Proposed change: install_date: 2026-12-14 -> 2026-12-27
     Source: E-2066, subject "Install date - J-24101"
     Agent's reason: Per E-2066.
     Source email E-2066 from Sam Ostrowski <sam@bluegill-tractor.example>:
     | Hi Maxi,
     |
     | The installation start for job J-24101 (Bluegill Tractor Works) moves from 2026-12-14 to 2026-12-27. Our shutdown moved.
     |
     | Sam Ostrowski
     | Bluegill Tractor Works

[02] P-102 · J-24102 · Kestrel Cabinet Co. (powder coat cure oven)
     Proposed change: po_number: KCC-3391 -> KCC-3391-R2
     Source: E-7880, subject "PO revision - J-24102"
     Agent's reason: Per E-7880.
     Source email E-7880 from Lucia Ferreyra <purchasing@kestrel-cabinet.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24102; the PO number now reads KCC-3391-R2. Please use it on all invoices.
     |
     | Lucia Ferreyra
     | Purchasing, Kestrel Cabinet Co.

[03] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: ship_date: 2027-01-12 -> 2027-01-18
     Source: E-4674, subject "Ship date - J-24109"
     Agent's reason: Per E-4674.
     Source email E-4674 from Sam Ostrowski <sam@saltmarsh-controls.example>:
     | Maxi,
     |
     | For job J-24109 (Larkspur Appliance), the new ship date is the 18th of January. Let me know if that is a problem.
     |
     | Sam Ostrowski, Saltmarsh Controls

[04] P-110 · J-24110 · Orion Volt Components (power-and-free conveyor)
     Proposed change: ship_date: 2027-01-20 -> 2027-01-28
     Source: E-6317, subject "Ship date - J-24110"
     Agent's reason: Per E-6317.
     Source email E-6317 from Priya Okafor <priya@ridgeback-burners.example>:
     | Maxi,
     |
     | For job J-24110 (Orion Volt Components), the new ship date is the 28th of January. Let me know if that is a problem.
     |
     | Priya Okafor, Ridgeback Burners

[05] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: install_date: 2027-01-19 -> 2027-01-03
     Source: E-5092, subject "Install date - J-24106"
     Agent's reason: Per E-5092.
     Source email E-5092 from Tom Brandvold <tom@copperleaf.example>:
     | Hi Maxi,
     |
     | The installation start for job J-24106 (Copperleaf Fixtures) moves from January 19, 2027 to January 3, 2027. Sorry for the trouble.
     |
     | Tom Brandvold
     | Copperleaf Fixtures

[06] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: po_number: CLF-2204 -> CLF-2204-R3
     Source: E-2327, subject "PO revision - J-24106"
     Agent's reason: Per E-2327.
     Source email E-2327 from Jordan Pike <purchasing@copperleaf.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24106; the PO number now reads CLF-2204-R3. Please use it on all invoices.
     |
     | Jordan Pike
     | Purchasing, Copperleaf Fixtures

[07] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: install_date: 2027-01-11 -> 2027-01-19
     Source: E-3551, subject "Install date - J-24104"
     Agent's reason: Per E-3551.
     Source email E-3551 from Tom Brandvold <tom@orion-volt.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24104 (Orion Volt Components): the new installation start is 2027-01-19, not 2027-01-14 as I wrote earlier. Apologies for the confusion.
     |
     | Tom Brandvold
     | Orion Volt Components

[08] P-107 · J-24107 · Redfern Steel Shelving (conveyor extension)
     Proposed change: install_date: 2026-12-09 -> 2026-11-23
     Source: E-6214, subject "Install date - J-24107"
     Agent's reason: Per E-6214.
     Source email E-6214 from Tom Brandvold <tom@redfern-steel.example>:
     | Maxi,
     |
     | For job J-24107 (Redfern Steel Shelving), the new installation start is the 23rd of November. Let me know if that is a problem.
     |
     | Tom Brandvold, Redfern Steel Shelving

[09] P-107 · J-24107 · Redfern Steel Shelving (conveyor extension)
     Proposed change: ship_date: 2026-11-27 -> 2026-12-05
     Source: E-5564, subject "Ship date - J-24107"
     Agent's reason: Per E-5564.
     Source email E-5564 from Elif Arslan <elif@fenwick-conveyor.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24107 (Redfern Steel Shelving): the new ship date is 2026-12-05, not 2026-12-02 as I wrote earlier. Apologies for the confusion.
     |
     | Elif Arslan
     | Fenwick Conveyor Supply

[10] P-105 · J-24105 · Tamsin Farm Equipment (abrasive blast room)
     Proposed change: po_number: TFE-1180 -> TFE-1180-R3
     Source: E-2061, subject "PO revision - J-24105"
     Agent's reason: Per E-2061.
     Source email E-2061 from Elif Arslan <purchasing@tamsin-farm.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24105; the PO number now reads TFE-1180-R3. Please use it on all invoices.
     |
     | Elif Arslan
     | Purchasing, Tamsin Farm Equipment

[11] P-103 · J-24103 · Harrow Valley Trailers (overhead conveyor loop)
     Proposed change: ship_date: 2026-11-20 -> 2026-11-26
     Source: E-7681, subject "Ship date - J-24103"
     Agent's reason: Per E-7681.
     Source email E-7681 from Hana Kowalczyk <hana@ridgeback-burners.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24103 (Harrow Valley Trailers) slips 6 days later than the date we last gave you. Sorry.
     |
     | Hana Kowalczyk
     | Ridgeback Burners

[12] P-102 · J-24102 · Kestrel Cabinet Co. (powder coat cure oven)
     Proposed change: ship_date: 2026-11-24 -> 2026-12-02
     Source: E-1253, subject "Ship date - J-24102"
     Agent's reason: Per E-1253.
     Source email E-1253 from Lucia Ferreyra <lucia@quill-filtration.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24102 (Kestrel Cabinet Co.) slips 8 days later than the date we last gave you. Sorry.
     |
     | Lucia Ferreyra
     | Quill Filtration

[13] P-108 · J-24108 · Bluegill Tractor Works (gas-fired cure oven)
     Proposed change: po_number: BTW-55187 -> BTW-55187-R2
     Source: E-8581, subject "PO revision - J-24108"
     Agent's reason: Per E-8581.
     Source email E-8581 from Lucia Ferreyra <purchasing@bluegill-tractor.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24108; the PO number now reads BTW-55187-R2. Please use it on all invoices.
     |
     | Lucia Ferreyra
     | Purchasing, Bluegill Tractor Works

[14] P-102 · J-24102 · Kestrel Cabinet Co. (powder coat cure oven)
     Proposed change: install_date: 2026-12-07 -> 2026-12-25
     Source: E-1228, subject "Install date - J-24102"
     Agent's reason: Per E-1228.
     Source email E-1228 from Hana Kowalczyk <hana@kestrel-cabinet.example>:
     | Maxi,
     |
     | For job J-24102 (Kestrel Cabinet Co.), the new installation start is the 25th of December. Let me know if that is a problem.
     |
     | Hana Kowalczyk, Kestrel Cabinet Co.

[15] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: po_number: (blank) -> LA-5215
     Source: E-3306, subject "PO revision - J-24109"
     Agent's reason: Per E-3306.
     Source email E-3306 from Tom Brandvold <purchasing@larkspur-appliance.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24109; the PO number now reads LA-5215. Please use it on all invoices.
     |
     | Tom Brandvold
     | Purchasing, Larkspur Appliance

[16] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: install_date: 2027-02-01 -> 2027-01-24
     Source: E-4211, subject "Install date - J-24109"
     Agent's reason: Per E-4211.
     Source email E-4211 from Priya Okafor <priya@larkspur-appliance.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24109 (Larkspur Appliance): the new installation start is 01/24/2027, not 01/28/2027 as I wrote earlier. Apologies for the confusion.
     |
     | Priya Okafor
     | Larkspur Appliance

[17] P-110 · J-24110 · Orion Volt Components (power-and-free conveyor)
     Proposed change: po_number: OVC-7791 -> OVC-7791-R1
     Source: E-5476, subject "PO revision - J-24110"
     Agent's reason: Per E-5476.
     Source email E-5476 from Jordan Pike <purchasing@orion-volt.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24110; the PO number now reads OVC-7791-R1. Please use it on all invoices.
     |
     | Jordan Pike
     | Purchasing, Orion Volt Components

[18] P-101 · J-24101 · Bluegill Tractor Works (paint booth line (2 crossdraft booths))
     Proposed change: ship_date: 2026-12-01 -> 2026-12-07
     Source: E-4814, subject "Ship date - J-24101"
     Agent's reason: Per E-4814.
     Source email E-4814 from Dana Whitlock <dana@saltmarsh-controls.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24101 (Bluegill Tractor Works) slips 6 days later than the date we last gave you. Sorry.
     |
     | Dana Whitlock
     | Saltmarsh Controls

[19] P-107 · J-24107 · Redfern Steel Shelving (conveyor extension)
     Proposed change: po_number: (blank) -> RSS-4916
     Source: E-4169, subject "PO revision - J-24107"
     Agent's reason: Per E-4169.
     Source email E-4169 from Priya Okafor <purchasing@redfern-steel.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24107; the PO number now reads RSS-4916. Please use it on all invoices.
     |
     | Priya Okafor
     | Purchasing, Redfern Steel Shelving

[20] P-105 · J-24105 · Tamsin Farm Equipment (abrasive blast room)
     Proposed change: ship_date: 2026-12-08 -> 2026-12-23
     Source: E-8969, subject "Ship date - J-24105"
     Agent's reason: Per E-8969.
     Source email E-8969 from Dana Whitlock <dana@quill-filtration.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24105 (Tamsin Farm Equipment) slips 15 days later than the date we last gave you. Sorry.
     |
     | Dana Whitlock
     | Quill Filtration

[21] P-108 · J-24108 · Bluegill Tractor Works (gas-fired cure oven)
     Proposed change: ship_date: 2026-12-10 -> 2026-12-26
     Source: E-1321, subject "Ship date - J-24108"
     Agent's reason: Per E-1321.
     Source email E-1321 from Lucia Ferreyra <lucia@saltmarsh-controls.example>:
     | Hi Maxi,
     |
     | The ship date for job J-24108 (Bluegill Tractor Works) moves from 2026-12-10 to 2026-12-26. A motor is back-ordered.
     |
     | Lucia Ferreyra
     | Saltmarsh Controls

[22] P-103 · J-24103 · Harrow Valley Trailers (overhead conveyor loop)
     Proposed change: install_date: 2026-12-02 -> 2026-12-20
     Source: E-2063, subject "Install date - J-24103"
     Agent's reason: Per E-2063.
     Source email E-2063 from Priya Okafor <priya@harrow-valley.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24103 (Harrow Valley Trailers) slips 18 days later than the date we last gave you. Sorry.
     |
     | Priya Okafor
     | Harrow Valley Trailers

[23] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: po_number: OVC-7720 -> OVC-7720-R1
     Source: E-1695, subject "PO revision - J-24104"
     Agent's reason: Per E-1695.
     Source email E-1695 from Lucia Ferreyra <purchasing@orion-volt.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24104; the PO number now reads OVC-7720-R1. Please use it on all invoices.
     |
     | Lucia Ferreyra
     | Purchasing, Orion Volt Components

[24] P-105 · J-24105 · Tamsin Farm Equipment (abrasive blast room)
     Proposed change: install_date: 2026-12-21 -> 2026-12-29
     Source: E-8628, subject "Install date - J-24105"
     Agent's reason: Per E-8628.
     Source email E-8628 from Priya Okafor <priya@tamsin-farm.example>:
     | Maxi,
     |
     | For job J-24105 (Tamsin Farm Equipment), the new installation start is the 29th of December. Let me know if that is a problem.
     |
     | Priya Okafor, Tamsin Farm Equipment

[25] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: ship_date: 2026-12-15 -> 2026-12-31
     Source: E-4133, subject "Ship date - J-24104"
     Agent's reason: Per E-4133.
     Source email E-4133 from Elif Arslan <elif@saltmarsh-controls.example>:
     | Hi Maxi,
     |
     | The ship date for job J-24104 (Orion Volt Components) moves from 12/15/2026 to 12/31/2026. Our shutdown moved.
     |
     | Elif Arslan
     | Saltmarsh Controls

[26] P-101 · J-24101 · Bluegill Tractor Works (paint booth line (2 crossdraft booths))
     Proposed change: po_number: BTW-55102 -> BTW-55102-R1
     Source: E-7286, subject "PO revision - J-24101"
     Agent's reason: Per E-7286.
     Source email E-7286 from Priya Okafor <purchasing@bluegill-tractor.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24101; the PO number now reads BTW-55102-R1. Please use it on all invoices.
     |
     | Priya Okafor
     | Purchasing, Bluegill Tractor Works

[27] P-110 · J-24110 · Orion Volt Components (power-and-free conveyor)
     Proposed change: install_date: 2027-02-15 -> 2027-02-26
     Source: E-4593, subject "Install date - J-24110"
     Agent's reason: Per E-4593.
     Source email E-4593 from Hana Kowalczyk <hana@orion-volt.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24110 (Orion Volt Components) slips 11 days later than the date we last gave you. Sorry.
     |
     | Hana Kowalczyk
     | Orion Volt Components

[28] P-103 · J-24103 · Harrow Valley Trailers (overhead conveyor loop)
     Proposed change: po_number: HVT-0457 -> HVT-0457-R1
     Source: E-2114, subject "PO revision - J-24103"
     Agent's reason: Per E-2114.
     Source email E-2114 from Hana Kowalczyk <purchasing@harrow-valley.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24103; the PO number now reads HVT-0457-R1. Please use it on all invoices.
     |
     | Hana Kowalczyk
     | Purchasing, Harrow Valley Trailers

[29] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: ship_date: 2027-01-05 -> 2027-01-21
     Source: E-7058, subject "Ship date - J-24106"
     Agent's reason: Per E-7058.
     Source email E-7058 from Lucia Ferreyra <lucia@ridgeback-burners.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24106 (Copperleaf Fixtures) slips 16 days later than the date we last gave you. Sorry.
     |
     | Lucia Ferreyra
     | Ridgeback Burners

[30] P-108 · J-24108 · Bluegill Tractor Works (gas-fired cure oven)
     Proposed change: install_date: 2027-01-06 -> 2026-12-31
     Source: E-8378, subject "Install date - J-24108"
     Agent's reason: Per E-8378.
     Source email E-8378 from Dana Whitlock <dana@bluegill-tractor.example>:
     | Maxi,
     |
     | For job J-24108 (Bluegill Tractor Works), the new installation start is the 31st of December. Let me know if that is a problem.
     |
     | Dana Whitlock, Bluegill Tractor Works
