# Approval queue — Fictional Finishing Systems (all data fictional)

You are reviewing ERP change proposals queued by the back-office AI agent. Today is 2026-11-13 (Friday).
For each proposal choose one:
  A = approve: the change is correct and supported by its source email
  R = reject: it is wrong in some way (project, field or value) or the source does not support it
  Q = query: you cannot tell from what is shown and want to see more before deciding
Each card includes the full source email and a system-generated evidence alignment.
There are 30 proposals below, numbered 01 to 30.

## Emails received after the agent built this queue (newest last)

L01 from Elif Arslan <elif@ridgeback-burners.example>: Confirming the date in my earlier email about job J-24110 stands: 2027-01-29.
L02 from Sam Ostrowski <sam@orion-volt.example>: Following up on my earlier email about job J-24104: please disregard the date I sent. The installation start is now January 27, 2027.
L03 from Sam Ostrowski <sam@quill-filtration.example>: Thanks for the quick reply on job J-24109. No other changes from our side.
L04 from Sam Ostrowski <sam@bluegill-tractor.example>: Confirming the date in my earlier email about job J-24101 stands: 2026-12-26.
L05 from Sam Ostrowski <purchasing@harrow-valley.example>: Just confirming the PO for job J-24103 is HVT-0457-R2, as in my earlier email.
L06 from Hana Kowalczyk <hana@saltmarsh-controls.example>: Confirming the date in my earlier email about job J-24106 stands: 2027-01-23.
L07 from Priya Okafor <priya@redfern-steel.example>: Thanks for the quick reply on job J-24107. No other changes from our side.
L08 from Sam Ostrowski <sam@quill-filtration.example>: Confirming the date in my earlier email about job J-24103 stands: 2026-12-02.
L09 from Priya Okafor <purchasing@larkspur-appliance.example>: Just confirming the PO for job J-24109 is LA-2593, as in my earlier email.
L10 from Dana Whitlock <dana@harrow-valley.example>: Thanks for the quick reply on job J-24103. No other changes from our side.

## Proposals

[01] P-101 · J-24101 · Bluegill Tractor Works (paint booth line (2 crossdraft booths))
     Proposed change: ship_date: 2026-12-01 -> 2026-12-14
     Source: E-2634, subject "Ship date - J-24101"
     Agent's reason: Per E-2634.
     Source email E-2634 from Hana Kowalczyk <hana@saltmarsh-controls.example>:
     | Hi Maxi,
     |
     | The ship date for job J-24101 (Bluegill Tractor Works) moves from 12/01/2026 to 12/14/2026. Our shutdown moved.
     |
     | Hana Kowalczyk
     | Saltmarsh Controls
     Evidence alignment (system-generated):
       sentence in source carrying the value: "The ship date for job J-24101 (Bluegill Tractor Works) moves from 12/01/2026 to 12/14/2026."
       job in source: J-24101   |   project in proposal: J-24101
       field in proposal: ship_date   |   proposed value: 2026-12-14

[02] P-108 · J-24108 · Bluegill Tractor Works (gas-fired cure oven)
     Proposed change: install_date: 2027-01-06 -> 2027-01-12
     Source: E-5993, subject "Install date - J-24108"
     Agent's reason: Per E-5993.
     Source email E-5993 from Tom Brandvold <tom@bluegill-tractor.example>:
     | Maxi,
     |
     | For job J-24108 (Bluegill Tractor Works), the new installation start is the 12th of January. Let me know if that is a problem.
     |
     | Tom Brandvold, Bluegill Tractor Works
     Evidence alignment (system-generated):
       sentence in source carrying the value: "For job J-24108 (Bluegill Tractor Works), the new installation start is the 12th of January."
       job in source: J-24108   |   project in proposal: J-24108
       field in proposal: install_date   |   proposed value: 2027-01-12

[03] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: ship_date: 2027-01-12 -> 2027-01-23
     Source: E-3071, subject "Ship date - J-24109"
     Agent's reason: Per E-3071.
     Source email E-3071 from Sam Ostrowski <sam@quill-filtration.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24109 (Larkspur Appliance) slips 11 days later than the date we last gave you. Sorry.
     |
     | Sam Ostrowski
     | Quill Filtration
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Everything on job J-24109 (Larkspur Appliance) slips 11 days later than the date we last gave you."
       job in source: J-24109   |   project in proposal: J-24109
       field in proposal: ship_date   |   proposed value: 2027-01-23

[04] P-110 · J-24110 · Orion Volt Components (power-and-free conveyor)
     Proposed change: po_number: OVC-7791 -> OVC-7791-R1
     Source: E-2691, subject "PO revision - J-24110"
     Agent's reason: Per E-2691.
     Source email E-2691 from Elif Arslan <purchasing@orion-volt.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24110; the PO number now reads OVC-7791-R1. Please use it on all invoices.
     |
     | Elif Arslan
     | Purchasing, Orion Volt Components
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Our buyer re-issued the purchase order for job J-24110; the PO number now reads OVC-7791-R1."
       job in source: J-24110   |   project in proposal: J-24110
       field in proposal: po_number   |   proposed value: OVC-7791-R1

[05] P-107 · J-24107 · Redfern Steel Shelving (conveyor extension)
     Proposed change: po_number: (blank) -> RSS-1797
     Source: E-6954, subject "PO revision - J-24107"
     Agent's reason: Per E-6954.
     Source email E-6954 from Dana Whitlock <purchasing@redfern-steel.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24107; the PO number now reads RSS-1797. Please use it on all invoices.
     |
     | Dana Whitlock
     | Purchasing, Redfern Steel Shelving
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Our buyer re-issued the purchase order for job J-24107; the PO number now reads RSS-1797."
       job in source: J-24107   |   project in proposal: J-24107
       field in proposal: po_number   |   proposed value: RSS-1797

[06] P-108 · J-24108 · Bluegill Tractor Works (gas-fired cure oven)
     Proposed change: po_number: BTW-55187 -> BTW-55187-R2
     Source: E-7714, subject "PO revision - J-24108"
     Agent's reason: Per E-7714.
     Source email E-7714 from Dana Whitlock <purchasing@bluegill-tractor.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24108; the PO number now reads BTW-55187-R2. Please use it on all invoices.
     |
     | Dana Whitlock
     | Purchasing, Bluegill Tractor Works
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Our buyer re-issued the purchase order for job J-24108; the PO number now reads BTW-55187-R2."
       job in source: J-24108   |   project in proposal: J-24108
       field in proposal: po_number   |   proposed value: BTW-55187-R2

[07] P-110 · J-24110 · Orion Volt Components (power-and-free conveyor)
     Proposed change: ship_date: 2027-01-20 -> 2027-01-29
     Source: E-4523, subject "Ship date - J-24110"
     Agent's reason: Per E-4523.
     Source email E-4523 from Elif Arslan <elif@ridgeback-burners.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24110 (Orion Volt Components): the new ship date is 01/29/2027, not 01/26/2027 as I wrote earlier. Apologies for the confusion.
     |
     | Elif Arslan
     | Ridgeback Burners
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Correction to my email this morning about job J-24110 (Orion Volt Components): the new ship date is 01/29/2027, not 01/26/2027 as I wrote earlier."
       job in source: J-24110   |   project in proposal: J-24110
       field in proposal: ship_date   |   proposed value: 2027-01-29

[08] P-107 · J-24107 · Redfern Steel Shelving (conveyor extension)
     Proposed change: ship_date: 2026-11-27 -> 2026-12-12
     Source: E-8320, subject "Ship date - J-24107"
     Agent's reason: Per E-8320.
     Source email E-8320 from Tom Brandvold <tom@ridgeback-burners.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24107 (Redfern Steel Shelving): the new ship date is 12/12/2026, not 12/15/2026 as I wrote earlier. Apologies for the confusion.
     |
     | Tom Brandvold
     | Ridgeback Burners
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Correction to my email this morning about job J-24107 (Redfern Steel Shelving): the new ship date is 12/12/2026, not 12/15/2026 as I wrote earlier."
       job in source: J-24107   |   project in proposal: J-24107
       field in proposal: ship_date   |   proposed value: 2026-12-12

[09] P-102 · J-24102 · Kestrel Cabinet Co. (powder coat cure oven)
     Proposed change: install_date: 2026-12-07 -> 2026-12-22
     Source: E-8879, subject "Install date - J-24102"
     Agent's reason: Per E-8879.
     Source email E-8879 from Dana Whitlock <dana@kestrel-cabinet.example>:
     | Hi Maxi,
     |
     | The installation start for job J-24102 (Kestrel Cabinet Co.) moves from Mon Dec 7 to Tue Dec 22. Sorry for the trouble.
     |
     | Dana Whitlock
     | Kestrel Cabinet Co.
     Evidence alignment (system-generated):
       sentence in source carrying the value: "The installation start for job J-24102 (Kestrel Cabinet Co.) moves from Mon Dec 7 to Tue Dec 22."
       job in source: J-24102   |   project in proposal: J-24102
       field in proposal: install_date   |   proposed value: 2026-12-22

[10] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: ship_date: 2026-12-15 -> 2026-12-30
     Source: E-7218, subject "Ship date - J-24104"
     Agent's reason: Per E-7218.
     Source email E-7218 from Dana Whitlock <dana@quill-filtration.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24104 (Orion Volt Components) slips 15 days later than the date we last gave you. Sorry.
     |
     | Dana Whitlock
     | Quill Filtration
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Everything on job J-24104 (Orion Volt Components) slips 15 days later than the date we last gave you."
       job in source: J-24104   |   project in proposal: J-24104
       field in proposal: ship_date   |   proposed value: 2026-12-30

[11] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: po_number: (blank) -> LA-2593
     Source: E-5448, subject "PO revision - J-24109"
     Agent's reason: Per E-5448.
     Source email E-5448 from Priya Okafor <purchasing@larkspur-appliance.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24109; the PO number now reads LA-2593. Please use it on all invoices.
     |
     | Priya Okafor
     | Purchasing, Larkspur Appliance
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Our buyer re-issued the purchase order for job J-24109; the PO number now reads LA-2593."
       job in source: J-24109   |   project in proposal: J-24109
       field in proposal: po_number   |   proposed value: LA-2593

[12] P-107 · J-24107 · Redfern Steel Shelving (conveyor extension)
     Proposed change: install_date: 2026-12-09 -> 2026-11-26
     Source: E-1627, subject "Install date - J-24107"
     Agent's reason: Per E-1627.
     Source email E-1627 from Priya Okafor <priya@redfern-steel.example>:
     | Maxi,
     |
     | For job J-24107 (Redfern Steel Shelving), the new installation start is the 26th of November. Let me know if that is a problem.
     |
     | Priya Okafor, Redfern Steel Shelving
     Evidence alignment (system-generated):
       sentence in source carrying the value: "For job J-24107 (Redfern Steel Shelving), the new installation start is the 26th of November."
       job in source: J-24107   |   project in proposal: J-24107
       field in proposal: install_date   |   proposed value: 2026-11-26

[13] P-105 · J-24105 · Tamsin Farm Equipment (abrasive blast room)
     Proposed change: po_number: TFE-1180 -> TFE-1180-R1
     Source: E-6263, subject "PO revision - J-24105"
     Agent's reason: Per E-6263.
     Source email E-6263 from Jordan Pike <purchasing@tamsin-farm.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24105; the PO number now reads TFE-1180-R1. Please use it on all invoices.
     |
     | Jordan Pike
     | Purchasing, Tamsin Farm Equipment
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Our buyer re-issued the purchase order for job J-24105; the PO number now reads TFE-1180-R1."
       job in source: J-24105   |   project in proposal: J-24105
       field in proposal: po_number   |   proposed value: TFE-1180-R1

[14] P-102 · J-24102 · Kestrel Cabinet Co. (powder coat cure oven)
     Proposed change: po_number: KCC-3391 -> KCC-3391-R2
     Source: E-3582, subject "PO revision - J-24102"
     Agent's reason: Per E-3582.
     Source email E-3582 from Hana Kowalczyk <purchasing@kestrel-cabinet.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24102; the PO number now reads KCC-3391-R2. Please use it on all invoices.
     |
     | Hana Kowalczyk
     | Purchasing, Kestrel Cabinet Co.
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Our buyer re-issued the purchase order for job J-24102; the PO number now reads KCC-3391-R2."
       job in source: J-24102   |   project in proposal: J-24102
       field in proposal: po_number   |   proposed value: KCC-3391-R2

[15] P-102 · J-24102 · Kestrel Cabinet Co. (powder coat cure oven)
     Proposed change: ship_date: 2026-11-24 -> 2026-12-09
     Source: E-1071, subject "Ship date - J-24102"
     Agent's reason: Per E-1071.
     Source email E-1071 from Lucia Ferreyra <lucia@ridgeback-burners.example>:
     | Hi Maxi,
     |
     | The ship date for job J-24102 (Kestrel Cabinet Co.) moves from November 24, 2026 to December 9, 2026. Sorry for the trouble.
     |
     | Lucia Ferreyra
     | Ridgeback Burners
     Evidence alignment (system-generated):
       sentence in source carrying the value: "The ship date for job J-24102 (Kestrel Cabinet Co.) moves from November 24, 2026 to December 9, 2026."
       job in source: J-24102   |   project in proposal: J-24102
       field in proposal: ship_date   |   proposed value: 2026-12-09

[16] P-103 · J-24103 · Harrow Valley Trailers (overhead conveyor loop)
     Proposed change: install_date: 2026-12-02 -> 2026-12-13
     Source: E-4162, subject "Install date - J-24103"
     Agent's reason: Per E-4162.
     Source email E-4162 from Dana Whitlock <dana@harrow-valley.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24103 (Harrow Valley Trailers) slips 11 days later than the date we last gave you. Sorry.
     |
     | Dana Whitlock
     | Harrow Valley Trailers
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Everything on job J-24103 (Harrow Valley Trailers) slips 11 days later than the date we last gave you."
       job in source: J-24103   |   project in proposal: J-24103
       field in proposal: install_date   |   proposed value: 2026-12-13

[17] P-101 · J-24101 · Bluegill Tractor Works (paint booth line (2 crossdraft booths))
     Proposed change: install_date: 2026-12-14 -> 2026-12-26
     Source: E-9908, subject "Install date - J-24101"
     Agent's reason: Per E-9908.
     Source email E-9908 from Sam Ostrowski <sam@bluegill-tractor.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24101 (Bluegill Tractor Works): the new installation start is 2026-12-26, not 2026-12-30 as I wrote earlier. Apologies for the confusion.
     |
     | Sam Ostrowski
     | Bluegill Tractor Works
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Correction to my email this morning about job J-24101 (Bluegill Tractor Works): the new installation start is 2026-12-26, not 2026-12-30 as I wrote earlier."
       job in source: J-24101   |   project in proposal: J-24101
       field in proposal: install_date   |   proposed value: 2026-12-26

[18] P-103 · J-24103 · Harrow Valley Trailers (overhead conveyor loop)
     Proposed change: po_number: HVT-0457 -> HVT-0457-R2
     Source: E-8998, subject "PO revision - J-24103"
     Agent's reason: Per E-8998.
     Source email E-8998 from Sam Ostrowski <purchasing@harrow-valley.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24103; the PO number now reads HVT-0457-R2. Please use it on all invoices.
     |
     | Sam Ostrowski
     | Purchasing, Harrow Valley Trailers
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Our buyer re-issued the purchase order for job J-24103; the PO number now reads HVT-0457-R2."
       job in source: J-24103   |   project in proposal: J-24103
       field in proposal: po_number   |   proposed value: HVT-0457-R2

[19] P-110 · J-24110 · Orion Volt Components (power-and-free conveyor)
     Proposed change: install_date: 2027-02-15 -> 2027-03-05
     Source: E-7922, subject "Install date - J-24110"
     Agent's reason: Per E-7922.
     Source email E-7922 from Tom Brandvold <tom@orion-volt.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24110 (Orion Volt Components) slips 18 days later than the date we last gave you. Sorry.
     |
     | Tom Brandvold
     | Orion Volt Components
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Everything on job J-24110 (Orion Volt Components) slips 18 days later than the date we last gave you."
       job in source: J-24110   |   project in proposal: J-24110
       field in proposal: install_date   |   proposed value: 2027-03-05

[20] P-108 · J-24108 · Bluegill Tractor Works (gas-fired cure oven)
     Proposed change: ship_date: 2026-12-10 -> 2026-12-19
     Source: E-3664, subject "Ship date - J-24108"
     Agent's reason: Per E-3664.
     Source email E-3664 from Hana Kowalczyk <hana@ridgeback-burners.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24108 (Bluegill Tractor Works): the new ship date is December 19, 2026, not December 14, 2026 as I wrote earlier. Apologies for the confusion.
     |
     | Hana Kowalczyk
     | Ridgeback Burners
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Correction to my email this morning about job J-24108 (Bluegill Tractor Works): the new ship date is December 19, 2026, not December 14, 2026 as I wrote earlier."
       job in source: J-24108   |   project in proposal: J-24108
       field in proposal: ship_date   |   proposed value: 2026-12-19

[21] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: install_date: 2027-01-11 -> 2027-01-22
     Source: E-1606, subject "Install date - J-24104"
     Agent's reason: Per E-1606.
     Source email E-1606 from Sam Ostrowski <sam@orion-volt.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24104 (Orion Volt Components) slips 11 days later than the date we last gave you. Sorry.
     |
     | Sam Ostrowski
     | Orion Volt Components
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Everything on job J-24104 (Orion Volt Components) slips 11 days later than the date we last gave you."
       job in source: J-24104   |   project in proposal: J-24104
       field in proposal: install_date   |   proposed value: 2027-01-22

[22] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: po_number: CLF-2204 -> CLF-2204-R2
     Source: E-7263, subject "PO revision - J-24106"
     Agent's reason: Per E-7263.
     Source email E-7263 from Hana Kowalczyk <purchasing@copperleaf.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24106; the PO number now reads CLF-2204-R2. Please use it on all invoices.
     |
     | Hana Kowalczyk
     | Purchasing, Copperleaf Fixtures
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Our buyer re-issued the purchase order for job J-24106; the PO number now reads CLF-2204-R2."
       job in source: J-24106   |   project in proposal: J-24106
       field in proposal: po_number   |   proposed value: CLF-2204-R2

[23] P-101 · J-24101 · Bluegill Tractor Works (paint booth line (2 crossdraft booths))
     Proposed change: po_number: BTW-55102 -> BTW-55102-R1
     Source: E-6841, subject "PO revision - J-24101"
     Agent's reason: Per E-6841.
     Source email E-6841 from Hana Kowalczyk <purchasing@bluegill-tractor.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24101; the PO number now reads BTW-55102-R1. Please use it on all invoices.
     |
     | Hana Kowalczyk
     | Purchasing, Bluegill Tractor Works
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Our buyer re-issued the purchase order for job J-24101; the PO number now reads BTW-55102-R1."
       job in source: J-24101   |   project in proposal: J-24101
       field in proposal: po_number   |   proposed value: BTW-55102-R1

[24] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: install_date: 2027-02-01 -> 2027-01-17
     Source: E-6674, subject "Install date - J-24109"
     Agent's reason: Per E-6674.
     Source email E-6674 from Elif Arslan <elif@larkspur-appliance.example>:
     | Maxi,
     |
     | For job J-24109 (Larkspur Appliance), the new installation start is the 17th of January. Let me know if that is a problem.
     |
     | Elif Arslan, Larkspur Appliance
     Evidence alignment (system-generated):
       sentence in source carrying the value: "For job J-24109 (Larkspur Appliance), the new installation start is the 17th of January."
       job in source: J-24109   |   project in proposal: J-24109
       field in proposal: install_date   |   proposed value: 2027-01-17

[25] P-103 · J-24103 · Harrow Valley Trailers (overhead conveyor loop)
     Proposed change: ship_date: 2026-11-20 -> 2026-12-02
     Source: E-7972, subject "Ship date - J-24103"
     Agent's reason: Per E-7972.
     Source email E-7972 from Sam Ostrowski <sam@quill-filtration.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24103 (Harrow Valley Trailers): the new ship date is 12/02/2026, not 12/05/2026 as I wrote earlier. Apologies for the confusion.
     |
     | Sam Ostrowski
     | Quill Filtration
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Correction to my email this morning about job J-24103 (Harrow Valley Trailers): the new ship date is 12/02/2026, not 12/05/2026 as I wrote earlier."
       job in source: J-24103   |   project in proposal: J-24103
       field in proposal: ship_date   |   proposed value: 2026-12-02

[26] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: install_date: 2027-01-19 -> 2027-01-04
     Source: E-7619, subject "Install date - J-24106"
     Agent's reason: Per E-7619.
     Source email E-7619 from Lucia Ferreyra <lucia@copperleaf.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24106 (Copperleaf Fixtures): the new installation start is Mon Jan 4, not Fri Jan 8 as I wrote earlier. Apologies for the confusion.
     |
     | Lucia Ferreyra
     | Copperleaf Fixtures
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Correction to my email this morning about job J-24106 (Copperleaf Fixtures): the new installation start is Mon Jan 4, not Fri Jan 8 as I wrote earlier."
       job in source: J-24106   |   project in proposal: J-24106
       field in proposal: install_date   |   proposed value: 2027-01-04

[27] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: po_number: OVC-7720 -> OVC-7720-R1
     Source: E-9391, subject "PO revision - J-24104"
     Agent's reason: Per E-9391.
     Source email E-9391 from Lucia Ferreyra <purchasing@orion-volt.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24104; the PO number now reads OVC-7720-R1. Please use it on all invoices.
     |
     | Lucia Ferreyra
     | Purchasing, Orion Volt Components
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Our buyer re-issued the purchase order for job J-24104; the PO number now reads OVC-7720-R1."
       job in source: J-24104   |   project in proposal: J-24104
       field in proposal: po_number   |   proposed value: OVC-7720-R1

[28] P-105 · J-24105 · Tamsin Farm Equipment (abrasive blast room)
     Proposed change: ship_date: 2026-12-08 -> 2026-12-16
     Source: E-7204, subject "Ship date - J-24105"
     Agent's reason: Per E-7204.
     Source email E-7204 from Dana Whitlock <dana@saltmarsh-controls.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24105 (Tamsin Farm Equipment) slips 8 days later than the date we last gave you. Sorry.
     |
     | Dana Whitlock
     | Saltmarsh Controls
     Evidence alignment (system-generated):
       sentence in source carrying the value: "Everything on job J-24105 (Tamsin Farm Equipment) slips 8 days later than the date we last gave you."
       job in source: J-24105   |   project in proposal: J-24105
       field in proposal: ship_date   |   proposed value: 2026-12-16

[29] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: ship_date: 2027-01-05 -> 2027-01-23
     Source: E-2635, subject "Ship date - J-24106"
     Agent's reason: Per E-2635.
     Source email E-2635 from Hana Kowalczyk <hana@saltmarsh-controls.example>:
     | Hi Maxi,
     |
     | The ship date for job J-24106 (Copperleaf Fixtures) moves from 2027-01-05 to 2027-01-23. Sorry for the trouble.
     |
     | Hana Kowalczyk
     | Saltmarsh Controls
     Evidence alignment (system-generated):
       sentence in source carrying the value: "The ship date for job J-24106 (Copperleaf Fixtures) moves from 2027-01-05 to 2027-01-23."
       job in source: J-24106   |   project in proposal: J-24106
       field in proposal: ship_date   |   proposed value: 2027-01-23

[30] P-105 · J-24105 · Tamsin Farm Equipment (abrasive blast room)
     Proposed change: install_date: 2026-12-21 -> 2027-01-01
     Source: E-8456, subject "Install date - J-24105"
     Agent's reason: Per E-8456.
     Source email E-8456 from Elif Arslan <elif@tamsin-farm.example>:
     | Maxi,
     |
     | For job J-24105 (Tamsin Farm Equipment), the new installation start is the 1st of January. Let me know if that is a problem.
     |
     | Elif Arslan, Tamsin Farm Equipment
     Evidence alignment (system-generated):
       sentence in source carrying the value: "For job J-24105 (Tamsin Farm Equipment), the new installation start is the 1st of January."
       job in source: J-24105   |   project in proposal: J-24105
       field in proposal: install_date   |   proposed value: 2027-01-01
