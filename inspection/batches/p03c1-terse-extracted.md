# Approval queue — Fictional Finishing Systems (all data fictional)

You are reviewing ERP change proposals queued by the back-office AI agent. Today is 2026-11-13 (Friday).
For each proposal choose one:
  A = approve: the change is correct and supported by its source email
  R = reject: it is wrong in some way (project, field or value) or the source does not support it
  Q = query: you cannot tell from what is shown and want to see more before deciding
Each card includes the full source email and an automatic evidence alignment that may contain extraction errors.
There are 30 proposals below, numbered 01 to 30.

[01] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: po_number: CLF-2204 -> CLF-2204-R3
     Source: E-5280, subject "PO revision - J-24106"
     Agent's reason: Per E-5280.
     Source email E-5280 from Hana Kowalczyk <purchasing@copperleaf.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24106; the PO number now reads CLF-2204-R3. Please use it on all invoices.
     |
     | Hana Kowalczyk
     | Purchasing, Copperleaf Fixtures
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24106; the PO number now reads CLF-2204-R3."
       job found in source: J-24106   |   project in proposal: J-24106
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: CLF-2204-R3

[02] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: po_number: (blank) -> LA-2644
     Source: E-7134, subject "PO revision - J-24109"
     Agent's reason: Per E-7134.
     Source email E-7134 from Jordan Pike <purchasing@larkspur-appliance.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24109; the PO number now reads LA-2644. Please use it on all invoices.
     |
     | Jordan Pike
     | Purchasing, Larkspur Appliance
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24109; the PO number now reads LA-2644."
       job found in source: J-24109   |   project in proposal: J-24109
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: LA-2644

[03] P-102 · J-24102 · Kestrel Cabinet Co. (powder coat cure oven)
     Proposed change: po_number: KCC-3391 -> KCC-3391-R2
     Source: E-2389, subject "PO revision - J-24102"
     Agent's reason: Per E-2389.
     Source email E-2389 from Sam Ostrowski <purchasing@kestrel-cabinet.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24102; the PO number now reads KCC-3391-R2. Please use it on all invoices.
     |
     | Sam Ostrowski
     | Purchasing, Kestrel Cabinet Co.
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24102; the PO number now reads KCC-3391-R2."
       job found in source: J-24102   |   project in proposal: J-24102
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: KCC-3391-R2

[04] P-107 · J-24107 · Redfern Steel Shelving (conveyor extension)
     Proposed change: install_date: 2026-12-09 -> 2026-12-18
     Source: E-3108, subject "Install date - J-24107"
     Agent's reason: Per E-3108.
     Source email E-3108 from Sam Ostrowski <sam@redfern-steel.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24107 (Redfern Steel Shelving): the new installation start is 12/18/2026, not 12/15/2026 as I wrote earlier. Apologies for the confusion.
     |
     | Sam Ostrowski
     | Redfern Steel Shelving
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Correction to my email this morning about job J-24107 (Redfern Steel Shelving): the new installation start is 12/18/2026, not 12/15/2026 as I wrote earlier."
       job found in source: J-24107   |   project in proposal: J-24107
       field mentioned in source: install_date   |   field in proposal: install_date   |   proposed value: 2026-12-18

[05] P-101 · J-24101 · Bluegill Tractor Works (paint booth line (2 crossdraft booths))
     Proposed change: po_number: BTW-55102 -> BTW-55102-R3
     Source: E-7082, subject "PO revision - J-24101"
     Agent's reason: Per E-7082.
     Source email E-7082 from Dana Whitlock <purchasing@bluegill-tractor.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24101; the PO number now reads BTW-55102-R3. Please use it on all invoices.
     |
     | Dana Whitlock
     | Purchasing, Bluegill Tractor Works
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24101; the PO number now reads BTW-55102-R3."
       job found in source: J-24101   |   project in proposal: J-24101
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: BTW-55102-R3

[06] P-110 · J-24110 · Orion Volt Components (power-and-free conveyor)
     Proposed change: ship_date: 2027-01-20 -> 2027-01-26
     Source: E-3686, subject "Ship date - J-24110"
     Agent's reason: Per E-3686.
     Source email E-3686 from Hana Kowalczyk <hana@fenwick-conveyor.example>:
     | Maxi,
     |
     | For job J-24110 (Orion Volt Components), the new ship date is the 26th of January. Let me know if that is a problem.
     |
     | Hana Kowalczyk, Fenwick Conveyor Supply
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Maxi, For job J-24110 (Orion Volt Components), the new ship date is the 26th of January."
       job found in source: J-24110   |   project in proposal: J-24110
       field mentioned in source: ship_date   |   field in proposal: ship_date   |   proposed value: 2027-01-26

[07] P-102 · J-24102 · Kestrel Cabinet Co. (powder coat cure oven)
     Proposed change: ship_date: 2026-11-24 -> 2026-12-07
     Source: E-5000, subject "Ship date - J-24102"
     Agent's reason: Per E-5000.
     Source email E-5000 from Lucia Ferreyra <lucia@quill-filtration.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24102 (Kestrel Cabinet Co.) slips 13 days later than the date we last gave you. Sorry.
     |
     | Lucia Ferreyra
     | Quill Filtration
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Everything on job J-24102 (Kestrel Cabinet Co.) slips 13 days later than the date we last gave you."
       job found in source: J-24102   |   project in proposal: J-24102
       field mentioned in source: unknown   |   field in proposal: ship_date   |   proposed value: 2026-12-07

[08] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: ship_date: 2027-01-12 -> 2027-01-28
     Source: E-4890, subject "Ship date - J-24109"
     Agent's reason: Per E-4890.
     Source email E-4890 from Tom Brandvold <tom@saltmarsh-controls.example>:
     | Maxi,
     |
     | For job J-24109 (Larkspur Appliance), the new ship date is the 28th of January. Let me know if that is a problem.
     |
     | Tom Brandvold, Saltmarsh Controls
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Maxi, For job J-24109 (Larkspur Appliance), the new ship date is the 28th of January."
       job found in source: J-24109   |   project in proposal: J-24109
       field mentioned in source: ship_date   |   field in proposal: ship_date   |   proposed value: 2027-01-28

[09] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: install_date: 2027-01-19 -> 2027-02-03
     Source: E-7104, subject "Install date - J-24106"
     Agent's reason: Per E-7104.
     Source email E-7104 from Hana Kowalczyk <hana@copperleaf.example>:
     | Maxi,
     |
     | For job J-24106 (Copperleaf Fixtures), the new installation start is the 3rd of February. Let me know if that is a problem.
     |
     | Hana Kowalczyk, Copperleaf Fixtures
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Maxi, For job J-24106 (Copperleaf Fixtures), the new installation start is the 3rd of February."
       job found in source: J-24106   |   project in proposal: J-24106
       field mentioned in source: install_date   |   field in proposal: install_date   |   proposed value: 2027-02-03

[10] P-103 · J-24103 · Harrow Valley Trailers (overhead conveyor loop)
     Proposed change: po_number: HVT-0457 -> HVT-0457-R1
     Source: E-6152, subject "PO revision - J-24103"
     Agent's reason: Per E-6152.
     Source email E-6152 from Lucia Ferreyra <purchasing@harrow-valley.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24103; the PO number now reads HVT-0457-R1. Please use it on all invoices.
     |
     | Lucia Ferreyra
     | Purchasing, Harrow Valley Trailers
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24103; the PO number now reads HVT-0457-R1."
       job found in source: J-24103   |   project in proposal: J-24103
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: HVT-0457-R1

[11] P-101 · J-24101 · Bluegill Tractor Works (paint booth line (2 crossdraft booths))
     Proposed change: ship_date: 2026-12-01 -> 2026-12-16
     Source: E-8983, subject "Ship date - J-24101"
     Agent's reason: Per E-8983.
     Source email E-8983 from Jordan Pike <jordan@saltmarsh-controls.example>:
     | Maxi,
     |
     | For job J-24101 (Bluegill Tractor Works), the new ship date is the 16th of December. Let me know if that is a problem.
     |
     | Jordan Pike, Saltmarsh Controls
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Maxi, For job J-24101 (Bluegill Tractor Works), the new ship date is the 16th of December."
       job found in source: J-24101   |   project in proposal: J-24101
       field mentioned in source: ship_date   |   field in proposal: ship_date   |   proposed value: 2026-12-16

[12] P-107 · J-24107 · Redfern Steel Shelving (conveyor extension)
     Proposed change: po_number: (blank) -> RSS-2477
     Source: E-4981, subject "PO revision - J-24107"
     Agent's reason: Per E-4981.
     Source email E-4981 from Hana Kowalczyk <purchasing@redfern-steel.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24107; the PO number now reads RSS-2477. Please use it on all invoices.
     |
     | Hana Kowalczyk
     | Purchasing, Redfern Steel Shelving
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24107; the PO number now reads RSS-2477."
       job found in source: J-24107   |   project in proposal: J-24107
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: RSS-2477

[13] P-107 · J-24107 · Redfern Steel Shelving (conveyor extension)
     Proposed change: ship_date: 2026-11-27 -> 2026-12-25
     Source: E-9883, subject "Install date - J-24107"
     Agent's reason: Per E-9883.
     Source email E-9883 from Hana Kowalczyk <hana@redfern-steel.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24107 (Redfern Steel Shelving) slips 16 days later than the date we last gave you. Sorry.
     |
     | Hana Kowalczyk
     | Redfern Steel Shelving
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Everything on job J-24107 (Redfern Steel Shelving) slips 16 days later than the date we last gave you."
       job found in source: J-24107   |   project in proposal: J-24107
       field mentioned in source: unknown   |   field in proposal: ship_date   |   proposed value: 2026-12-25

[14] P-101 · J-24101 · Bluegill Tractor Works (paint booth line (2 crossdraft booths))
     Proposed change: install_date: 2026-12-14 -> 2026-12-27
     Source: E-1067, subject "Install date - J-24101"
     Agent's reason: Per E-1067.
     Source email E-1067 from Sam Ostrowski <sam@bluegill-tractor.example>:
     | Maxi,
     |
     | For job J-24101 (Bluegill Tractor Works), the new installation start is the 27th of December. Let me know if that is a problem.
     |
     | Sam Ostrowski, Bluegill Tractor Works
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Maxi, For job J-24101 (Bluegill Tractor Works), the new installation start is the 27th of December."
       job found in source: J-24101   |   project in proposal: J-24101
       field mentioned in source: install_date   |   field in proposal: install_date   |   proposed value: 2026-12-27

[15] P-105 · J-24105 · Tamsin Farm Equipment (abrasive blast room)
     Proposed change: install_date: 2026-12-21 -> 2026-12-30
     Source: E-9164, subject "Install date - J-24105"
     Agent's reason: Per E-9164.
     Source email E-9164 from Priya Okafor <priya@tamsin-farm.example>:
     | Hi Maxi,
     |
     | The installation start for job J-24105 (Tamsin Farm Equipment) moves from December 21, 2026 to December 30, 2026. A motor is back-ordered.
     |
     | Priya Okafor
     | Tamsin Farm Equipment
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, The installation start for job J-24105 (Tamsin Farm Equipment) moves from December 21, 2026 to December 30, 2026."
       job found in source: J-24105   |   project in proposal: J-24105
       field mentioned in source: install_date   |   field in proposal: install_date   |   proposed value: 2026-12-30

[16] P-103 · J-24103 · Harrow Valley Trailers (overhead conveyor loop)
     Proposed change: ship_date: 2026-11-20 -> 2026-12-01
     Source: E-1853, subject "Ship date - J-24103"
     Agent's reason: Per E-1853.
     Source email E-1853 from Priya Okafor <priya@fenwick-conveyor.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24103 (Harrow Valley Trailers) slips 11 days later than the date we last gave you. Sorry.
     |
     | Priya Okafor
     | Fenwick Conveyor Supply
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Everything on job J-24103 (Harrow Valley Trailers) slips 11 days later than the date we last gave you."
       job found in source: J-24103   |   project in proposal: J-24103
       field mentioned in source: unknown   |   field in proposal: ship_date   |   proposed value: 2026-12-01

[17] P-110 · J-24110 · Orion Volt Components (power-and-free conveyor)
     Proposed change: install_date: 2027-02-15 -> 2027-01-28
     Source: E-7541, subject "Install date - J-24110"
     Agent's reason: Per E-7541.
     Source email E-7541 from Lucia Ferreyra <lucia@orion-volt.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24110 (Orion Volt Components) slips 18 days earlier than the date we last gave you. Sorry.
     |
     | Lucia Ferreyra
     | Orion Volt Components
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Everything on job J-24110 (Orion Volt Components) slips 18 days earlier than the date we last gave you."
       job found in source: J-24110   |   project in proposal: J-24110
       field mentioned in source: unknown   |   field in proposal: install_date   |   proposed value: 2027-01-28

[18] P-105 · J-24105 · Tamsin Farm Equipment (abrasive blast room)
     Proposed change: ship_date: 2026-12-08 -> 2026-12-17
     Source: E-5346, subject "Ship date - J-24105"
     Agent's reason: Per E-5346.
     Source email E-5346 from Sam Ostrowski <sam@ridgeback-burners.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24105 (Tamsin Farm Equipment) slips 9 days later than the date we last gave you. Sorry.
     |
     | Sam Ostrowski
     | Ridgeback Burners
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Everything on job J-24105 (Tamsin Farm Equipment) slips 9 days later than the date we last gave you."
       job found in source: J-24105   |   project in proposal: J-24105
       field mentioned in source: unknown   |   field in proposal: ship_date   |   proposed value: 2026-12-17

[19] P-108 · J-24108 · Bluegill Tractor Works (gas-fired cure oven)
     Proposed change: po_number: BTW-55187 -> BTW-55102-R1
     Source: E-1933, subject "PO revision - J-24101"
     Agent's reason: Per E-1933.
     Source email E-1933 from Hana Kowalczyk <purchasing@bluegill-tractor.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24101; the PO number now reads BTW-55102-R1. Please use it on all invoices.
     |
     | Hana Kowalczyk
     | Purchasing, Bluegill Tractor Works
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24101; the PO number now reads BTW-55102-R1."
       job found in source: J-24101   |   project in proposal: J-24108
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: BTW-55102-R1

[20] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: ship_date: 2027-01-05 -> 2027-01-20
     Source: E-8470, subject "Ship date - J-24106"
     Agent's reason: Per E-8470.
     Source email E-8470 from Jordan Pike <jordan@quill-filtration.example>:
     | Hi Maxi,
     |
     | The ship date for job J-24106 (Copperleaf Fixtures) moves from Tue Jan 5 to Wed Jan 20. Sorry for the trouble.
     |
     | Jordan Pike
     | Quill Filtration
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, The ship date for job J-24106 (Copperleaf Fixtures) moves from Tue Jan 5 to Wed Jan 20."
       job found in source: J-24106   |   project in proposal: J-24106
       field mentioned in source: ship_date   |   field in proposal: ship_date   |   proposed value: 2027-01-20

[21] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: install_date: 2027-01-11 -> 2027-01-17
     Source: E-3996, subject "Install date - J-24104"
     Agent's reason: Per E-3996.
     Source email E-3996 from Tom Brandvold <tom@orion-volt.example>:
     | Hi Maxi,
     |
     | The installation start for job J-24104 (Orion Volt Components) moves from 01/11/2027 to 01/17/2027. Sorry for the trouble.
     |
     | Tom Brandvold
     | Orion Volt Components
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, The installation start for job J-24104 (Orion Volt Components) moves from 01/11/2027 to 01/17/2027."
       job found in source: J-24104   |   project in proposal: J-24104
       field mentioned in source: install_date   |   field in proposal: install_date   |   proposed value: 2027-01-17

[22] P-108 · J-24108 · Bluegill Tractor Works (gas-fired cure oven)
     Proposed change: ship_date: 2026-12-10 -> 2026-12-18
     Source: E-2651, subject "Ship date - J-24108"
     Agent's reason: Per E-2651.
     Source email E-2651 from Dana Whitlock <dana@ridgeback-burners.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24108 (Bluegill Tractor Works) slips 8 days later than the date we last gave you. Sorry.
     |
     | Dana Whitlock
     | Ridgeback Burners
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Everything on job J-24108 (Bluegill Tractor Works) slips 8 days later than the date we last gave you."
       job found in source: J-24108   |   project in proposal: J-24108
       field mentioned in source: unknown   |   field in proposal: ship_date   |   proposed value: 2026-12-18

[23] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: install_date: 2027-02-01 -> 2027-02-26
     Source: E-2027, subject "Install date - J-24109"
     Agent's reason: Per E-2027.
     Source email E-2027 from Tom Brandvold <tom@larkspur-appliance.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24109 (Larkspur Appliance) slips 18 days later than the date we last gave you. Sorry.
     |
     | Tom Brandvold
     | Larkspur Appliance
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Everything on job J-24109 (Larkspur Appliance) slips 18 days later than the date we last gave you."
       job found in source: J-24109   |   project in proposal: J-24109
       field mentioned in source: unknown   |   field in proposal: install_date   |   proposed value: 2027-02-26

[24] P-110 · J-24110 · Orion Volt Components (power-and-free conveyor)
     Proposed change: po_number: OVC-7791 -> OVC-7791-R3
     Source: E-9587, subject "PO revision - J-24110"
     Agent's reason: Per E-9587.
     Source email E-9587 from Tom Brandvold <purchasing@orion-volt.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24110; the PO number now reads OVC-7791-R3. Please use it on all invoices.
     |
     | Tom Brandvold
     | Purchasing, Orion Volt Components
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24110; the PO number now reads OVC-7791-R3."
       job found in source: J-24110   |   project in proposal: J-24110
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: OVC-7791-R3

[25] P-103 · J-24103 · Harrow Valley Trailers (overhead conveyor loop)
     Proposed change: install_date: 2026-12-02 -> 2026-12-17
     Source: E-9053, subject "Install date - J-24103"
     Agent's reason: Per E-9053.
     Source email E-9053 from Dana Whitlock <dana@harrow-valley.example>:
     | Maxi,
     |
     | For job J-24103 (Harrow Valley Trailers), the new installation start is the 17th of December. Let me know if that is a problem.
     |
     | Dana Whitlock, Harrow Valley Trailers
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Maxi, For job J-24103 (Harrow Valley Trailers), the new installation start is the 17th of December."
       job found in source: J-24103   |   project in proposal: J-24103
       field mentioned in source: install_date   |   field in proposal: install_date   |   proposed value: 2026-12-17

[26] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: po_number: OVC-7720 -> OVC-7720-R1
     Source: E-1371, subject "PO revision - J-24104"
     Agent's reason: Per E-1371.
     Source email E-1371 from Priya Okafor <purchasing@orion-volt.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24104; the PO number now reads OVC-7720-R1. Please use it on all invoices.
     |
     | Priya Okafor
     | Purchasing, Orion Volt Components
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24104; the PO number now reads OVC-7720-R1."
       job found in source: J-24104   |   project in proposal: J-24104
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: OVC-7720-R1

[27] P-102 · J-24102 · Kestrel Cabinet Co. (powder coat cure oven)
     Proposed change: install_date: 2026-12-07 -> 2026-12-15
     Source: E-1078, subject "Install date - J-24102"
     Agent's reason: Per E-1078.
     Source email E-1078 from Priya Okafor <priya@kestrel-cabinet.example>:
     | Maxi,
     |
     | For job J-24102 (Kestrel Cabinet Co.), the new installation start is the 15th of December. Let me know if that is a problem.
     |
     | Priya Okafor, Kestrel Cabinet Co.
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Maxi, For job J-24102 (Kestrel Cabinet Co.), the new installation start is the 15th of December."
       job found in source: J-24102   |   project in proposal: J-24102
       field mentioned in source: install_date   |   field in proposal: install_date   |   proposed value: 2026-12-15

[28] P-105 · J-24105 · Tamsin Farm Equipment (abrasive blast room)
     Proposed change: po_number: TFE-1180 -> TFE-1180-R1
     Source: E-3378, subject "PO revision - J-24105"
     Agent's reason: Per E-3378.
     Source email E-3378 from Sam Ostrowski <purchasing@tamsin-farm.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24105; the PO number now reads TFE-1180-R1. Please use it on all invoices.
     |
     | Sam Ostrowski
     | Purchasing, Tamsin Farm Equipment
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24105; the PO number now reads TFE-1180-R1."
       job found in source: J-24105   |   project in proposal: J-24105
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: TFE-1180-R1

[29] P-108 · J-24108 · Bluegill Tractor Works (gas-fired cure oven)
     Proposed change: install_date: 2027-01-06 -> 2027-01-24
     Source: E-4664, subject "Install date - J-24108"
     Agent's reason: Per E-4664.
     Source email E-4664 from Dana Whitlock <dana@bluegill-tractor.example>:
     | Hi Maxi,
     |
     | The installation start for job J-24108 (Bluegill Tractor Works) moves from Wed Jan 6 to Sun Jan 24. Sorry for the trouble.
     |
     | Dana Whitlock
     | Bluegill Tractor Works
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, The installation start for job J-24108 (Bluegill Tractor Works) moves from Wed Jan 6 to Sun Jan 24."
       job found in source: J-24108   |   project in proposal: J-24108
       field mentioned in source: install_date   |   field in proposal: install_date   |   proposed value: 2027-01-24

[30] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: ship_date: 2026-12-15 -> 2026-12-27
     Source: E-4933, subject "Ship date - J-24104"
     Agent's reason: Per E-4933.
     Source email E-4933 from Hana Kowalczyk <hana@ridgeback-burners.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24104 (Orion Volt Components): the new ship date is Sun Dec 27, not Thu Dec 31 as I wrote earlier. Apologies for the confusion.
     |
     | Hana Kowalczyk
     | Ridgeback Burners
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Correction to my email this morning about job J-24104 (Orion Volt Components): the new ship date is Sun Dec 27, not Thu Dec 31 as I wrote earlier."
       job found in source: J-24104   |   project in proposal: J-24104
       field mentioned in source: ship_date   |   field in proposal: ship_date   |   proposed value: 2026-12-27
