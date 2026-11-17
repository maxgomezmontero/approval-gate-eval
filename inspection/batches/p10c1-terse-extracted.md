# Approval queue — Fictional Finishing Systems (all data fictional)

You are reviewing ERP change proposals queued by the back-office AI agent. Today is 2026-11-13 (Friday).
For each proposal choose one:
  A = approve: the change is correct and supported by its source email
  R = reject: it is wrong in some way (project, field or value) or the source does not support it
  Q = query: you cannot tell from what is shown and want to see more before deciding
Each card includes the full source email and an automatic evidence alignment that may contain extraction errors.
There are 30 proposals below, numbered 01 to 30.

[01] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: ship_date: 2027-01-05 -> 2027-01-21
     Source: E-5134, subject "Ship date - J-24106"
     Agent's reason: Per E-5134.
     Source email E-5134 from Lucia Ferreyra <lucia@quill-filtration.example>:
     | Hi Maxi,
     |
     | The ship date for job J-24106 (Copperleaf Fixtures) moves from January 5, 2027 to January 21, 2027. Sorry for the trouble.
     |
     | Lucia Ferreyra
     | Quill Filtration
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, The ship date for job J-24106 (Copperleaf Fixtures) moves from January 5, 2027 to January 21, 2027."
       job found in source: J-24106   |   project in proposal: J-24106
       field mentioned in source: ship_date   |   field in proposal: ship_date   |   proposed value: 2027-01-21

[02] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: install_date: 2027-01-19 -> 2027-01-04
     Source: E-8666, subject "Install date - J-24106"
     Agent's reason: Per E-8666.
     Source email E-8666 from Elif Arslan <elif@copperleaf.example>:
     | Hi Maxi,
     |
     | Bad news on the schedule. Everything on job J-24106 (Copperleaf Fixtures) slips 13 days earlier than the date we last gave you. Sorry.
     |
     | Elif Arslan
     | Copperleaf Fixtures
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Everything on job J-24106 (Copperleaf Fixtures) slips 13 days earlier than the date we last gave you."
       job found in source: J-24106   |   project in proposal: J-24106
       field mentioned in source: unknown   |   field in proposal: install_date   |   proposed value: 2027-01-04

[03] P-101 · J-24101 · Bluegill Tractor Works (paint booth line (2 crossdraft booths))
     Proposed change: install_date: 2026-12-14 -> 2026-12-29
     Source: E-7172, subject "Install date - J-24108"
     Agent's reason: Per E-7172.
     Source email E-7172 from Lucia Ferreyra <lucia@bluegill-tractor.example>:
     | Maxi,
     |
     | For job J-24108 (Bluegill Tractor Works), the new installation start is the 29th of December. Let me know if that is a problem.
     |
     | Lucia Ferreyra, Bluegill Tractor Works
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Maxi, For job J-24108 (Bluegill Tractor Works), the new installation start is the 29th of December."
       job found in source: J-24108   |   project in proposal: J-24101
       field mentioned in source: install_date   |   field in proposal: install_date   |   proposed value: 2026-12-29

[04] P-105 · J-24105 · Tamsin Farm Equipment (abrasive blast room)
     Proposed change: po_number: TFE-1180 -> TFE-118-0R1
     Source: E-3703, subject "PO revision - J-24105"
     Agent's reason: Per E-3703.
     Source email E-3703 from Elif Arslan <purchasing@tamsin-farm.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24105; the PO number now reads TFE-1180-R1. Please use it on all invoices.
     |
     | Elif Arslan
     | Purchasing, Tamsin Farm Equipment
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24105; the PO number now reads TFE-1180-R1."
       job found in source: J-24105   |   project in proposal: J-24105
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: TFE-118-0R1

[05] P-105 · J-24105 · Tamsin Farm Equipment (abrasive blast room)
     Proposed change: ship_date: 2026-12-08 -> 2026-12-16
     Source: E-8179, subject "Ship date - J-24105"
     Agent's reason: Per E-8179.
     Source email E-8179 from Hana Kowalczyk <hana@quill-filtration.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24105 (Tamsin Farm Equipment): the new ship date is 2026-12-16, not 2026-12-23 as I wrote earlier. Apologies for the confusion.
     |
     | Hana Kowalczyk
     | Quill Filtration
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Correction to my email this morning about job J-24105 (Tamsin Farm Equipment): the new ship date is 2026-12-16, not 2026-12-23 as I wrote earlier."
       job found in source: J-24105   |   project in proposal: J-24105
       field mentioned in source: ship_date   |   field in proposal: ship_date   |   proposed value: 2026-12-16

[06] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: install_date: 2027-01-11 -> 2026-12-21
     Source: E-6400, subject "Ship date - J-24104"
     Agent's reason: Per E-6400.
     Source email E-6400 from Priya Okafor <priya@quill-filtration.example>:
     | Hi Maxi,
     |
     | The ship date for job J-24104 (Orion Volt Components) moves from 12/15/2026 to 12/21/2026. Sorry for the trouble.
     |
     | Priya Okafor
     | Quill Filtration
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, The ship date for job J-24104 (Orion Volt Components) moves from 12/15/2026 to 12/21/2026."
       job found in source: J-24104   |   project in proposal: J-24104
       field mentioned in source: ship_date   |   field in proposal: install_date   |   proposed value: 2026-12-21

[07] P-110 · J-24110 · Orion Volt Components (power-and-free conveyor)
     Proposed change: po_number: OVC-7791 -> OVC-7791-R3
     Source: E-5404, subject "PO revision - J-24110"
     Agent's reason: Per E-5404.
     Source email E-5404 from Lucia Ferreyra <purchasing@orion-volt.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24110; the PO number now reads OVC-7791-R3. Please use it on all invoices.
     |
     | Lucia Ferreyra
     | Purchasing, Orion Volt Components
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24110; the PO number now reads OVC-7791-R3."
       job found in source: J-24110   |   project in proposal: J-24110
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: OVC-7791-R3

[08] P-103 · J-24103 · Harrow Valley Trailers (overhead conveyor loop)
     Proposed change: ship_date: 2026-11-20 -> 2026-12-02
     Source: E-5638, subject "Ship date - J-24103"
     Agent's reason: Per E-5638.
     Source email E-5638 from Hana Kowalczyk <hana@fenwick-conveyor.example>:
     | Maxi,
     |
     | For job J-24103 (Harrow Valley Trailers), the new ship date is the 2nd of December. Let me know if that is a problem.
     |
     | Hana Kowalczyk, Fenwick Conveyor Supply
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Maxi, For job J-24103 (Harrow Valley Trailers), the new ship date is the 2nd of December."
       job found in source: J-24103   |   project in proposal: J-24103
       field mentioned in source: ship_date   |   field in proposal: ship_date   |   proposed value: 2026-12-02

[09] P-108 · J-24108 · Bluegill Tractor Works (gas-fired cure oven)
     Proposed change: po_number: BTW-55187 -> BTW-55187-R1
     Source: E-8976, subject "PO revision - J-24108"
     Agent's reason: Per E-8976.
     Source email E-8976 from Tom Brandvold <purchasing@bluegill-tractor.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24108; the PO number now reads BTW-55187-R1. Please use it on all invoices.
     |
     | Tom Brandvold
     | Purchasing, Bluegill Tractor Works
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24108; the PO number now reads BTW-55187-R1."
       job found in source: J-24108   |   project in proposal: J-24108
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: BTW-55187-R1

[10] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: ship_date: 2026-12-15 -> 2026-12-28
     Source: E-4959, subject "Ship date - J-24104"
     Agent's reason: Per E-4959.
     Source email E-4959 from Sam Ostrowski <sam@fenwick-conveyor.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24104 (Orion Volt Components): the new ship date is 12/28/2026, not 12/23/2026 as I wrote earlier. Apologies for the confusion.
     |
     | Sam Ostrowski
     | Fenwick Conveyor Supply
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Correction to my email this morning about job J-24104 (Orion Volt Components): the new ship date is 12/28/2026, not 12/23/2026 as I wrote earlier."
       job found in source: J-24104   |   project in proposal: J-24104
       field mentioned in source: ship_date   |   field in proposal: ship_date   |   proposed value: 2026-12-28

[11] P-102 · J-24102 · Kestrel Cabinet Co. (powder coat cure oven)
     Proposed change: po_number: KCC-3391 -> KCC-3391-R2
     Source: E-5971, subject "PO revision - J-24102"
     Agent's reason: Per E-5971.
     Source email E-5971 from Hana Kowalczyk <purchasing@kestrel-cabinet.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24102; the PO number now reads KCC-3391-R2. Please use it on all invoices.
     |
     | Hana Kowalczyk
     | Purchasing, Kestrel Cabinet Co.
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24102; the PO number now reads KCC-3391-R2."
       job found in source: J-24102   |   project in proposal: J-24102
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: KCC-3391-R2

[12] P-110 · J-24110 · Orion Volt Components (power-and-free conveyor)
     Proposed change: ship_date: 2027-01-20 -> 2027-01-31
     Source: E-8804, subject "Ship date - J-24110"
     Agent's reason: Per E-8804.
     Source email E-8804 from Dana Whitlock <dana@ridgeback-burners.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24110 (Orion Volt Components): the new ship date is 01/28/2027, not 01/31/2027 as I wrote earlier. Apologies for the confusion.
     |
     | Dana Whitlock
     | Ridgeback Burners
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Correction to my email this morning about job J-24110 (Orion Volt Components): the new ship date is 01/28/2027, not 01/31/2027 as I wrote earlier."
       job found in source: J-24110   |   project in proposal: J-24110
       field mentioned in source: ship_date   |   field in proposal: ship_date   |   proposed value: 2027-01-31

[13] P-108 · J-24108 · Bluegill Tractor Works (gas-fired cure oven)
     Proposed change: install_date: 2027-01-06 -> 2027-01-21
     Source: E-4173, subject "Install date - J-24108"
     Agent's reason: Per E-4173.
     Source email E-4173 from Jordan Pike <jordan@bluegill-tractor.example>:
     | Hi Maxi,
     |
     | Could we move the installation start for job J-24108 (Bluegill Tractor Works) to Thu Jan 21? I still need to confirm internally and will get back to you Monday.
     |
     | Thanks,
     | Jordan Pike
     | Bluegill Tractor Works
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Could we move the installation start for job J-24108 (Bluegill Tractor Works) to Thu Jan 21?"
       job found in source: J-24108   |   project in proposal: J-24108
       field mentioned in source: install_date   |   field in proposal: install_date   |   proposed value: 2027-01-21

[14] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: ship_date: 2027-01-12 -> 2027-01-25
     Source: E-6762, subject "Ship date - J-24109"
     Agent's reason: Per E-6762.
     Source email E-6762 from Jordan Pike <jordan@ridgeback-burners.example>:
     | Hi Maxi,
     |
     | The ship date for job J-24109 (Larkspur Appliance) moves from 2027-01-12 to 2027-01-25. Our shutdown moved.
     |
     | Jordan Pike
     | Ridgeback Burners
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, The ship date for job J-24109 (Larkspur Appliance) moves from 2027-01-12 to 2027-01-25."
       job found in source: J-24109   |   project in proposal: J-24109
       field mentioned in source: ship_date   |   field in proposal: ship_date   |   proposed value: 2027-01-25

[15] P-103 · J-24103 · Harrow Valley Trailers (overhead conveyor loop)
     Proposed change: install_date: 2026-12-02 -> 2026-12-18
     Source: E-2972, subject "Install date - J-24103"
     Agent's reason: Per E-2972.
     Source email E-2972 from Dana Whitlock <dana@harrow-valley.example>:
     | Hi Maxi,
     |
     | Could we move the installation start for job J-24103 (Harrow Valley Trailers) to 12/18/2026? I still need to confirm internally and will get back to you Monday.
     |
     | Thanks,
     | Dana Whitlock
     | Harrow Valley Trailers
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Could we move the installation start for job J-24103 (Harrow Valley Trailers) to 12/18/2026?"
       job found in source: J-24103   |   project in proposal: J-24103
       field mentioned in source: install_date   |   field in proposal: install_date   |   proposed value: 2026-12-18

[16] P-101 · J-24101 · Bluegill Tractor Works (paint booth line (2 crossdraft booths))
     Proposed change: ship_date: 2026-12-01 -> 2026-12-22
     Source: E-2050, subject "Install date - J-24101"
     Agent's reason: Per E-2050.
     Source email E-2050 from Sam Ostrowski <sam@bluegill-tractor.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24101 (Bluegill Tractor Works): the new installation start is December 22, 2026, not December 25, 2026 as I wrote earlier. Apologies for the confusion.
     |
     | Sam Ostrowski
     | Bluegill Tractor Works
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Correction to my email this morning about job J-24101 (Bluegill Tractor Works): the new installation start is December 22, 2026, not December 25, 2026 as I wrote earlier."
       job found in source: J-24101   |   project in proposal: J-24101
       field mentioned in source: install_date   |   field in proposal: ship_date   |   proposed value: 2026-12-22

[17] P-107 · J-24107 · Redfern Steel Shelving (conveyor extension)
     Proposed change: install_date: 2026-12-09 -> 2026-12-27
     Source: E-4110, subject "Install date - J-24107"
     Agent's reason: Per E-4110.
     Source email E-4110 from Lucia Ferreyra <lucia@redfern-steel.example>:
     | Hi Maxi,
     |
     | The installation start for job J-24107 (Redfern Steel Shelving) moves from December 9, 2026 to December 27, 2026. Sorry for the trouble.
     |
     | Lucia Ferreyra
     | Redfern Steel Shelving
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, The installation start for job J-24107 (Redfern Steel Shelving) moves from December 9, 2026 to December 27, 2026."
       job found in source: J-24107   |   project in proposal: J-24107
       field mentioned in source: install_date   |   field in proposal: install_date   |   proposed value: 2026-12-27

[18] P-108 · J-24108 · Bluegill Tractor Works (gas-fired cure oven)
     Proposed change: ship_date: 2026-12-10 -> 2026-12-21
     Source: E-8136, subject "Ship date - J-24108"
     Agent's reason: Per E-8136.
     Source email E-8136 from Jordan Pike <jordan@saltmarsh-controls.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24108 (Bluegill Tractor Works): the new ship date is 12/21/2026, not 12/25/2026 as I wrote earlier. Apologies for the confusion.
     |
     | Jordan Pike
     | Saltmarsh Controls
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Correction to my email this morning about job J-24108 (Bluegill Tractor Works): the new ship date is 12/21/2026, not 12/25/2026 as I wrote earlier."
       job found in source: J-24108   |   project in proposal: J-24108
       field mentioned in source: ship_date   |   field in proposal: ship_date   |   proposed value: 2026-12-21

[19] P-102 · J-24102 · Kestrel Cabinet Co. (powder coat cure oven)
     Proposed change: install_date: 2026-12-07 -> 2026-12-25
     Source: E-2653, subject "Install date - J-24102"
     Agent's reason: Per E-2653.
     Source email E-2653 from Elif Arslan <elif@kestrel-cabinet.example>:
     | Maxi,
     |
     | For job J-24102 (Kestrel Cabinet Co.), the new installation start is the 25th of December. Let me know if that is a problem.
     |
     | Elif Arslan, Kestrel Cabinet Co.
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Maxi, For job J-24102 (Kestrel Cabinet Co.), the new installation start is the 25th of December."
       job found in source: J-24102   |   project in proposal: J-24102
       field mentioned in source: install_date   |   field in proposal: install_date   |   proposed value: 2026-12-25

[20] P-103 · J-24103 · Harrow Valley Trailers (overhead conveyor loop)
     Proposed change: po_number: HVT-0457 -> HVT-0457-R1
     Source: E-2767, subject "PO revision - J-24103"
     Agent's reason: Per E-2767.
     Source email E-2767 from Tom Brandvold <purchasing@harrow-valley.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24103; the PO number now reads HVT-0457-R1. Please use it on all invoices.
     |
     | Tom Brandvold
     | Purchasing, Harrow Valley Trailers
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24103; the PO number now reads HVT-0457-R1."
       job found in source: J-24103   |   project in proposal: J-24103
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: HVT-0457-R1

[21] P-106 · J-24106 · Copperleaf Fixtures (batch cure oven)
     Proposed change: po_number: CLF-2204 -> CLF-2204-R3
     Source: E-3078, subject "PO revision - J-24106"
     Agent's reason: Per E-3078.
     Source email E-3078 from Sam Ostrowski <purchasing@copperleaf.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24106; the PO number now reads CLF-2204-R3. Please use it on all invoices.
     |
     | Sam Ostrowski
     | Purchasing, Copperleaf Fixtures
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24106; the PO number now reads CLF-2204-R3."
       job found in source: J-24106   |   project in proposal: J-24106
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: CLF-2204-R3

[22] P-110 · J-24110 · Orion Volt Components (power-and-free conveyor)
     Proposed change: install_date: 2027-02-15 -> 2027-01-23
     Source: E-4950, subject "Install date - J-24104"
     Agent's reason: Per E-4950.
     Source email E-4950 from Hana Kowalczyk <hana@orion-volt.example>:
     | Maxi,
     |
     | For job J-24104 (Orion Volt Components), the new installation start is the 23rd of January. Let me know if that is a problem.
     |
     | Hana Kowalczyk, Orion Volt Components
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Maxi, For job J-24104 (Orion Volt Components), the new installation start is the 23rd of January."
       job found in source: J-24104   |   project in proposal: J-24110
       field mentioned in source: install_date   |   field in proposal: install_date   |   proposed value: 2027-01-23

[23] P-107 · J-24107 · Redfern Steel Shelving (conveyor extension)
     Proposed change: po_number: (blank) -> RSS-9647
     Source: E-9619, subject "PO revision - J-24107"
     Agent's reason: Per E-9619.
     Source email E-9619 from Dana Whitlock <purchasing@redfern-steel.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24107; the PO number now reads RSS-9467. Please use it on all invoices.
     |
     | Dana Whitlock
     | Purchasing, Redfern Steel Shelving
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24107; the PO number now reads RSS-9467."
       job found in source: J-24107   |   project in proposal: J-24107
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: RSS-9647

[24] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: install_date: 2027-02-01 -> 2027-02-07
     Source: E-2438, subject "Install date - J-24109"
     Agent's reason: Per E-2438.
     Source email E-2438 from Sam Ostrowski <sam@larkspur-appliance.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24109 (Larkspur Appliance): the new installation start is Sun Feb 7, not Thu Feb 4 as I wrote earlier. Apologies for the confusion.
     |
     | Sam Ostrowski
     | Larkspur Appliance
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Correction to my email this morning about job J-24109 (Larkspur Appliance): the new installation start is Sun Feb 7, not Thu Feb 4 as I wrote earlier."
       job found in source: J-24109   |   project in proposal: J-24109
       field mentioned in source: install_date   |   field in proposal: install_date   |   proposed value: 2027-02-07

[25] P-107 · J-24107 · Redfern Steel Shelving (conveyor extension)
     Proposed change: ship_date: 2026-11-27 -> 2026-12-09
     Source: E-3309, subject "Ship date - J-24107"
     Agent's reason: Per E-3309.
     Source email E-3309 from Elif Arslan <elif@ridgeback-burners.example>:
     | Hi Maxi,
     |
     | The ship date for job J-24107 (Redfern Steel Shelving) moves from Fri Nov 27 to Wed Dec 9. Sorry for the trouble.
     |
     | Elif Arslan
     | Ridgeback Burners
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, The ship date for job J-24107 (Redfern Steel Shelving) moves from Fri Nov 27 to Wed Dec 9."
       job found in source: J-24107   |   project in proposal: J-24107
       field mentioned in source: ship_date   |   field in proposal: ship_date   |   proposed value: 2026-12-09

[26] P-105 · J-24105 · Tamsin Farm Equipment (abrasive blast room)
     Proposed change: install_date: 2026-12-21 -> 2027-01-06
     Source: E-3588, subject "Install date - J-24105"
     Agent's reason: Per E-3588.
     Source email E-3588 from Priya Okafor <priya@tamsin-farm.example>:
     | Hi Maxi,
     |
     | Correction to my email this morning about job J-24105 (Tamsin Farm Equipment): the new installation start is 2027-01-06, not 2027-01-10 as I wrote earlier. Apologies for the confusion.
     |
     | Priya Okafor
     | Tamsin Farm Equipment
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Correction to my email this morning about job J-24105 (Tamsin Farm Equipment): the new installation start is 2027-01-06, not 2027-01-10 as I wrote earlier."
       job found in source: J-24105   |   project in proposal: J-24105
       field mentioned in source: install_date   |   field in proposal: install_date   |   proposed value: 2027-01-06

[27] P-102 · J-24102 · Kestrel Cabinet Co. (powder coat cure oven)
     Proposed change: ship_date: 2026-11-24 -> 2026-12-02
     Source: E-8183, subject "Ship date - J-24102"
     Agent's reason: Per E-8183.
     Source email E-8183 from Hana Kowalczyk <hana@fenwick-conveyor.example>:
     | Hi Maxi,
     |
     | The ship date for job J-24102 (Kestrel Cabinet Co.) moves from 11/24/2026 to 12/02/2026. Our shutdown moved.
     |
     | Hana Kowalczyk
     | Fenwick Conveyor Supply
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, The ship date for job J-24102 (Kestrel Cabinet Co.) moves from 11/24/2026 to 12/02/2026."
       job found in source: J-24102   |   project in proposal: J-24102
       field mentioned in source: ship_date   |   field in proposal: ship_date   |   proposed value: 2026-12-02

[28] P-109 · J-24109 · Larkspur Appliance (5-stage wash system)
     Proposed change: po_number: (blank) -> LA-1828
     Source: E-2683, subject "PO revision - J-24109"
     Agent's reason: Per E-2683.
     Source email E-2683 from Tom Brandvold <purchasing@larkspur-appliance.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24109; the PO number now reads LA-1828. Please use it on all invoices.
     |
     | Tom Brandvold
     | Purchasing, Larkspur Appliance
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24109; the PO number now reads LA-1828."
       job found in source: J-24109   |   project in proposal: J-24109
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: LA-1828

[29] P-101 · J-24101 · Bluegill Tractor Works (paint booth line (2 crossdraft booths))
     Proposed change: po_number: BTW-55102 -> BTW-55102-R3
     Source: E-8517, subject "PO revision - J-24101"
     Agent's reason: Per E-8517.
     Source email E-8517 from Sam Ostrowski <purchasing@bluegill-tractor.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24101; the PO number now reads BTW-55102-R3. Please use it on all invoices.
     |
     | Sam Ostrowski
     | Purchasing, Bluegill Tractor Works
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24101; the PO number now reads BTW-55102-R3."
       job found in source: J-24101   |   project in proposal: J-24101
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: BTW-55102-R3

[30] P-104 · J-24104 · Orion Volt Components (paint booth and cure oven)
     Proposed change: po_number: OVC-7720 -> OVC-7720-R2
     Source: E-9066, subject "PO revision - J-24104"
     Agent's reason: Per E-9066.
     Source email E-9066 from Jordan Pike <purchasing@orion-volt.example>:
     | Hi Maxi,
     |
     | Our buyer re-issued the purchase order for job J-24104; the PO number now reads OVC-7720-R2. Please use it on all invoices.
     |
     | Jordan Pike
     | Purchasing, Orion Volt Components
     Evidence alignment (automatic extraction, may be wrong):
       sentence in source with a value: "Hi Maxi, Our buyer re-issued the purchase order for job J-24104; the PO number now reads OVC-7720-R2."
       job found in source: J-24104   |   project in proposal: J-24104
       field mentioned in source: po_number   |   field in proposal: po_number   |   proposed value: OVC-7720-R2
