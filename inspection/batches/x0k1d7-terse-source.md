# Approval queue — Fictional Finishing Systems (all data fictional)

You are reviewing ERP change proposals queued by the back-office AI agent. Today is 2026-11-13 (Friday).
For each proposal choose one:
  A = approve: the change is correct and supported by its source email
  R = reject: it is wrong in some way (project, field or value) or the source does not support it
  Q = query: you cannot tell from what is shown and want to see more before deciding
Each card includes the full source email.
There are 30 proposals below, numbered 01 to 30.

[01] P-101 · J-24101 · Bluegill Tractor Works (paint booth line (2 crossdraft booths))
     Proposed change: po_number: BTW-55102 -> BTW-55102-R2
     Source: E-3007, subject "PO revision - J-24101"
     Agent's reason: Per E-3007.
     Source email E-3007 from Elif Arslan <purchasing@bluegill-tractor.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24101; the PO number now reads BTW-55102-R2. Please use it on all invoices.
     |
     | Elif Arslan
     | Purchasing, Bluegill Tractor Works

[02] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: po_number: CLF-2204 -> CLF-2204-R1
     Source: E-8132, subject "PO revision - J-24106"
     Agent's reason: Per E-8132.
     Source email E-8132 from Lucia Ferreyra <purchasing@copperleaf.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24106; the PO number now reads CLF-2204-R1. Please use it on all invoices.
     |
     | Lucia Ferreyra
     | Purchasing, Copperleaf Fixtures

[03] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: ship_date: 2027-01-05 -> 2027-01-16
     Source: E-2723, subject "Ship date - J-24106"
     Agent's reason: Per E-2723.
     Source email E-2723 from Elif Arslan <elif@fenwick-conveyor.example>:
     | Hi Maxi,
     |
     | The ship date for job J-24106 (Copperleaf Fixtures) moves from 01/05/2027 to 01/16/2027. A motor is back-ordered.
     |
     | Elif Arslan
     | Fenwick Conveyor Supply

[04] P-101 · J-24101 · Bluegill Tractor Works (paint booth line (2 crossdraft booths))
     Proposed change: install_date: 2026-12-14 -> 2026-12-23
     Source: E-3925, subject "Install date - J-24101"
     Agent's reason: Per E-3925.
     Source email E-3925 from Elif Arslan <elif@bluegill-tractor.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24101 (Bluegill Tractor Works): the new installation start is 2026-12-23, not 2026-12-26 as I wrote earlier. Apologies for the confusion.
     |
     | Elif Arslan
     | Bluegill Tractor Works

[05] P-103 · J-24103 · Harrow Valley Trailers (overhead conveyor loop)
     Proposed change: ship_date: 2026-11-20 -> 2026-11-26
     Source: E-1669, subject "Ship date - J-24103"
     Agent's reason: Per E-1669.
     Source email E-1669 from Tom Brandvold <tom@ridgeback-burners.example>:
     | Maxi,
     |
     | For job J-24103 (Harrow Valley Trailers), the new ship date is the 26th of November. Let me know if that is a problem.
     |
     | Tom Brandvold, Ridgeback Burners

[06] P-103 · J-24103 · Harrow Valley Trailers (overhead conveyor loop)
     Proposed change: po_number: HVT-0457 -> HVT-0457-R3
     Source: E-5756, subject "PO revision - J-24103"
     Agent's reason: Per E-5756.
     Source email E-5756 from Dana Whitlock <purchasing@harrow-valley.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24103; the PO number now reads HVT-0457-R3. Please use it on all invoices.
     |
     | Dana Whitlock
     | Purchasing, Harrow Valley Trailers

[07] P-102 · J-24102 · Kestrel Cabinet Co. (powder coat cure oven)
     Proposed change: po_number: KCC-3391 -> KCC-3391-R2
     Source: E-1138, subject "PO revision - J-24102"
     Agent's reason: Per E-1138.
     Source email E-1138 from Elif Arslan <purchasing@kestrel-cabinet.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24102; the PO number now reads KCC-3391-R2. Please use it on all invoices.
     |
     | Elif Arslan
     | Purchasing, Kestrel Cabinet Co.

[08] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: po_number: (blank) -> LA-7577
     Source: E-9832, subject "PO revision - J-24109"
     Agent's reason: Per E-9832.
     Source email E-9832 from Lucia Ferreyra <purchasing@larkspur-appliance.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24109; the PO number now reads LA-7577. Please use it on all invoices.
     |
     | Lucia Ferreyra
     | Purchasing, Larkspur Appliance

[09] P-110 · J-24110 · Orion Volt Components (power-and-free conveyor)
     Proposed change: ship_date: 2027-01-20 -> 2027-02-02
     Source: E-6991, subject "Ship date - J-24110"
     Agent's reason: Per E-6991.
     Source email E-6991 from Lucia Ferreyra <lucia@saltmarsh-controls.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24110 (Orion Volt Components) slips 13 days later than the date we last gave you. Sorry.
     |
     | Lucia Ferreyra
     | Saltmarsh Controls

[10] P-108 · J-24108 · Bluegill Tractor Works (gas-fired cure oven)
     Proposed change: ship_date: 2026-12-10 -> 2026-12-25
     Source: E-9638, subject "Ship date - J-24108"
     Agent's reason: Per E-9638.
     Source email E-9638 from Lucia Ferreyra <lucia@fenwick-conveyor.example>:
     | Maxi,
     |
     | For job J-24108 (Bluegill Tractor Works), the new ship date is the 25th of December. Let me know if that is a problem.
     |
     | Lucia Ferreyra, Fenwick Conveyor Supply

[11] P-101 · J-24101 · Bluegill Tractor Works (paint booth line (2 crossdraft booths))
     Proposed change: ship_date: 2026-12-01 -> 2026-12-16
     Source: E-3472, subject "Ship date - J-24101"
     Agent's reason: Per E-3472.
     Source email E-3472 from Dana Whitlock <dana@saltmarsh-controls.example>:
     | Hi Maxi,
     |
     | The ship date for job J-24101 (Bluegill Tractor Works) moves from 12/01/2026 to 12/16/2026. Sorry for the trouble.
     |
     | Dana Whitlock
     | Saltmarsh Controls

[12] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: ship_date: 2027-01-12 -> 2027-01-30
     Source: E-2180, subject "Ship date - J-24109"
     Agent's reason: Per E-2180.
     Source email E-2180 from Lucia Ferreyra <lucia@ridgeback-burners.example>:
     | Maxi,
     |
     | For job J-24109 (Larkspur Appliance), the new ship date is the 30th of January. Let me know if that is a problem.
     |
     | Lucia Ferreyra, Ridgeback Burners

[13] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: install_date: 2027-01-11 -> 2027-01-19
     Source: E-6445, subject "Install date - J-24104"
     Agent's reason: Per E-6445.
     Source email E-6445 from Dana Whitlock <dana@orion-volt.example>:
     | Maxi,
     |
     | For job J-24104 (Orion Volt Components), the new installation start is the 19th of January. Let me know if that is a problem.
     |
     | Dana Whitlock, Orion Volt Components

[14] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: install_date: 2027-01-19 -> 2027-02-01
     Source: E-8596, subject "Install date - J-24106"
     Agent's reason: Per E-8596.
     Source email E-8596 from Dana Whitlock <dana@copperleaf.example>:
     | Hi Maxi,
     |
     | The installation start for job J-24106 (Copperleaf Fixtures) moves from 01/19/2027 to 02/01/2027. Our shutdown moved.
     |
     | Dana Whitlock
     | Copperleaf Fixtures

[15] P-107 · J-24107 · Redfern Steel Shelving (conveyor extension)
     Proposed change: po_number: (blank) -> RSS-8144
     Source: E-5127, subject "PO revision - J-24107"
     Agent's reason: Per E-5127.
     Source email E-5127 from Priya Okafor <purchasing@redfern-steel.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24107; the PO number now reads RSS-8144. Please use it on all invoices.
     |
     | Priya Okafor
     | Purchasing, Redfern Steel Shelving

[16] P-108 · J-24108 · Bluegill Tractor Works (gas-fired cure oven)
     Proposed change: install_date: 2027-01-06 -> 2027-01-21
     Source: E-8874, subject "Install date - J-24108"
     Agent's reason: Per E-8874.
     Source email E-8874 from Dana Whitlock <dana@bluegill-tractor.example>:
     | Hi Maxi,
     |
     | The installation start for job J-24108 (Bluegill Tractor Works) moves from January 6, 2027 to January 21, 2027. Our shutdown moved.
     |
     | Dana Whitlock
     | Bluegill Tractor Works

[17] P-110 · J-24110 · Orion Volt Components (power-and-free conveyor)
     Proposed change: po_number: OVC-7791 -> OVC-7791-R3
     Source: E-9187, subject "PO revision - J-24110"
     Agent's reason: Per E-9187.
     Source email E-9187 from Dana Whitlock <purchasing@orion-volt.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24110; the PO number now reads OVC-7791-R3. Please use it on all invoices.
     |
     | Dana Whitlock
     | Purchasing, Orion Volt Components

[18] P-105 · J-24105 · Tamsin Farm Equipment (abrasive blast room)
     Proposed change: po_number: TFE-1180 -> TFE-1180-R2
     Source: E-2975, subject "PO revision - J-24105"
     Agent's reason: Per E-2975.
     Source email E-2975 from Sam Ostrowski <purchasing@tamsin-farm.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24105; the PO number now reads TFE-1180-R2. Please use it on all invoices.
     |
     | Sam Ostrowski
     | Purchasing, Tamsin Farm Equipment

[19] P-110 · J-24110 · Orion Volt Components (power-and-free conveyor)
     Proposed change: install_date: 2027-02-15 -> 2027-02-27
     Source: E-5430, subject "Install date - J-24110"
     Agent's reason: Per E-5430.
     Source email E-5430 from Elif Arslan <elif@orion-volt.example>:
     | Hi Maxi,
     |
     | The installation start for job J-24110 (Orion Volt Components) moves from 02/15/2027 to 02/27/2027. Sorry for the trouble.
     |
     | Elif Arslan
     | Orion Volt Components

[20] P-107 · J-24107 · Redfern Steel Shelving (conveyor extension)
     Proposed change: install_date: 2026-12-09 -> 2027-01-01
     Source: E-6251, subject "Install date - J-24107"
     Agent's reason: Per E-6251.
     Source email E-6251 from Sam Ostrowski <sam@redfern-steel.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24107 (Redfern Steel Shelving) slips 16 days later than the date we last gave you. Sorry.
     |
     | Sam Ostrowski
     | Redfern Steel Shelving

[21] P-102 · J-24102 · Kestrel Cabinet Co. (powder coat cure oven)
     Proposed change: ship_date: 2026-11-24 -> 2026-12-06
     Source: E-2597, subject "Ship date - J-24102"
     Agent's reason: Per E-2597.
     Source email E-2597 from Lucia Ferreyra <lucia@fenwick-conveyor.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24102 (Kestrel Cabinet Co.): the new ship date is 2026-12-06, not 2026-12-13 as I wrote earlier. Apologies for the confusion.
     |
     | Lucia Ferreyra
     | Fenwick Conveyor Supply

[22] P-103 · J-24103 · Harrow Valley Trailers (overhead conveyor loop)
     Proposed change: install_date: 2026-12-02 -> 2026-12-17
     Source: E-4750, subject "Install date - J-24103"
     Agent's reason: Per E-4750.
     Source email E-4750 from Elif Arslan <elif@harrow-valley.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24103 (Harrow Valley Trailers) slips 15 days later than the date we last gave you. Sorry.
     |
     | Elif Arslan
     | Harrow Valley Trailers

[23] P-107 · J-24107 · Redfern Steel Shelving (conveyor extension)
     Proposed change: ship_date: 2026-11-27 -> 2026-12-06
     Source: E-2811, subject "Ship date - J-24107"
     Agent's reason: Per E-2811.
     Source email E-2811 from Lucia Ferreyra <lucia@fenwick-conveyor.example>:
     | Hi Maxi,
     |
     | The ship date for job J-24107 (Redfern Steel Shelving) moves from 2026-11-27 to 2026-12-06. Sorry for the trouble.
     |
     | Lucia Ferreyra
     | Fenwick Conveyor Supply

[24] P-102 · J-24102 · Kestrel Cabinet Co. (powder coat cure oven)
     Proposed change: install_date: 2026-12-07 -> 2026-12-23
     Source: E-9396, subject "Install date - J-24102"
     Agent's reason: Per E-9396.
     Source email E-9396 from Jordan Pike <jordan@kestrel-cabinet.example>:
     | Hi Maxi,
     |
     | The installation start for job J-24102 (Kestrel Cabinet Co.) moves from 12/07/2026 to 12/23/2026. Sorry for the trouble.
     |
     | Jordan Pike
     | Kestrel Cabinet Co.

[25] P-105 · J-24105 · Tamsin Farm Equipment (abrasive blast room)
     Proposed change: ship_date: 2026-12-08 -> 2026-12-20
     Source: E-6684, subject "Ship date - J-24105"
     Agent's reason: Per E-6684.
     Source email E-6684 from Jordan Pike <jordan@saltmarsh-controls.example>:
     | Hi Maxi,
     |
     | The ship date for job J-24105 (Tamsin Farm Equipment) moves from 12/08/2026 to 12/20/2026. A motor is back-ordered.
     |
     | Jordan Pike
     | Saltmarsh Controls

[26] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: install_date: 2027-02-01 -> 2027-01-17
     Source: E-2861, subject "Install date - J-24109"
     Agent's reason: Per E-2861.
     Source email E-2861 from Dana Whitlock <dana@larkspur-appliance.example>:
     | Hi Maxi,
     |
     | The installation start for job J-24109 (Larkspur Appliance) moves from 2027-02-01 to 2027-01-17. Our shutdown moved.
     |
     | Dana Whitlock
     | Larkspur Appliance

[27] P-108 · J-24108 · Bluegill Tractor Works (gas-fired cure oven)
     Proposed change: po_number: BTW-55187 -> BTW-55187-R2
     Source: E-9763, subject "PO revision - J-24108"
     Agent's reason: Per E-9763.
     Source email E-9763 from Tom Brandvold <purchasing@bluegill-tractor.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24108; the PO number now reads BTW-55187-R2. Please use it on all invoices.
     |
     | Tom Brandvold
     | Purchasing, Bluegill Tractor Works

[28] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: ship_date: 2026-12-15 -> 2026-12-27
     Source: E-1635, subject "Ship date - J-24104"
     Agent's reason: Per E-1635.
     Source email E-1635 from Lucia Ferreyra <lucia@quill-filtration.example>:
     | Hi Maxi,
     |
     | The ship date for job J-24104 (Orion Volt Components) moves from Tue Dec 15 to Sun Dec 27. Our shutdown moved.
     |
     | Lucia Ferreyra
     | Quill Filtration

[29] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: po_number: OVC-7720 -> OVC-7720-R2
     Source: E-9194, subject "PO revision - J-24104"
     Agent's reason: Per E-9194.
     Source email E-9194 from Sam Ostrowski <purchasing@orion-volt.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24104; the PO number now reads OVC-7720-R2. Please use it on all invoices.
     |
     | Sam Ostrowski
     | Purchasing, Orion Volt Components

[30] P-105 · J-24105 · Tamsin Farm Equipment (abrasive blast room)
     Proposed change: install_date: 2026-12-21 -> 2027-01-02
     Source: E-5087, subject "Install date - J-24105"
     Agent's reason: Per E-5087.
     Source email E-5087 from Tom Brandvold <tom@tamsin-farm.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24105 (Tamsin Farm Equipment) slips 12 days later than the date we last gave you. Sorry.
     |
     | Tom Brandvold
     | Tamsin Farm Equipment
