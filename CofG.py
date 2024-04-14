import matplotlib.pyplot as plt

# X & Y Coordinates

x_values = []
y_values = []

# Station Calculation

def find_sta(index, weight):
    sta = round(index / weight, 3)
    return sta

# APS Calculations

basic_weight = int(input("Enter BASIC WEIGHT: "))
basic_index = int(input("Enter BASIC INDEX: "))
jump_seat = input("Will the jump seat be occupied? (YES or NO) ")
qhci = input("Will a QHCI be on the aircraft? (YES or NO) ")

if jump_seat.lower() == "yes":
    pilots_index = 14
else:
    pilots_index = 8.5

if qhci.lower() == "yes":
    qhci_index = 16
else:
    qhci_index = 0
    
no2_index = 14
no1_index = 47

crew_weight = 400
crew_index = (pilots_index * 2) + no2_index + no1_index + qhci_index

aps = basic_weight + crew_weight
aps_index = basic_index + crew_index
aps_sta = find_sta(aps_index, aps)

x_values.append(aps_sta)
y_values.append(aps)

# Airframe Fuel Calculations

af_fuel = int(input("Airframe fuel required (KG): "))
af_fuel_index = af_fuel / 3.17

aps_fuel = aps + af_fuel
aps_fuel_index = aps_index + af_fuel_index
aps_fuel_sta = find_sta(aps_fuel_index, aps_fuel)

x_values.append(aps_fuel_sta)
y_values.append(aps_fuel)

# ERT Fuel Calculations

ert_fuel = int(input("ERT fuel required: "))
if ert_fuel > 0:
    ert_position = int(input("Forward edge of the ERT (STA): ")) + 30
    ert_fuel_sta = (ert_fuel / ert_position) / 1000
    aps_fuel_ert = aps_fuel + ert_fuel
    aps_fuel_ert_sta = round(aps_fuel_sta + ert_fuel_sta, 3)
    
    x_values.append(aps_fuel_ert_sta)
    y_values.append(aps_fuel_ert)

# USL Calculations

front_hook_index = 249
centre_hook_index = 331
aft_hook_index = 409  

# front_hook = int(input("Weight of USLs on front hook: (enter 0 if no USL) "))
# ctr_hook = int(input("Weight of USLs on centre hook: (enter 0 if no USL) "))
# aft_hook = int(input("Weight of USLs on aft hook: (enter 0 if no USL) "))

# Cargo Calculations

cargo_required = input("Will you be taking any freight? (YES or NO) ")
if cargo_required.lower() == "yes":
    cargo_c = int(input("How much weight will be in Section C? "))
    cargo_c_index = cargo_c * 0.181
    cargo_d = int(input("How much weight will be in Section D? "))
    cargo_d_index = cargo_d * 0.303
    cargo_e = int(input("How much weight will be in Section E? "))
    cargo_e_index = cargo_e * 0.425
    cargo_f = int(input("How much weight will be in Section F? "))
    cargo_f_index = cargo_f * 0.536
    
    total_cargo = cargo_c + cargo_d + cargo_e + cargo_f
    cargo_index = (cargo_c_index + cargo_d_index + cargo_e_index + cargo_f_index)
    cargo_sta = round((total_cargo / cargo_index) / 1000, 3)
    
    aps_fuel_ert_cargo = aps_fuel_ert + total_cargo
    aps_fuel_ert_cargo_sta = aps_fuel_ert_sta + cargo_sta
    
    x_values.append(aps_fuel_ert_cargo_sta)
    y_values.append(aps_fuel_ert_cargo)

# Plot

cofg_envelope_x = [0.310, 0.310, 0.322, 0.322, 0.331, 0.331, 0.343, 0.349, 0.349]
cofg_envelope_y = [10000, 15000, 22700, 24500, 24500, 22700, 15000, 13000, 10000]
cofg_craning_envelope_x = [0.310, 0.310, 0.319, 0.331, 0.349, 0.349]
cofg_craning_envelope_y = [10000, 19300, 24500, 24500, 19300, 10000]

x_axis_labels = [range(300, 360, 10)]
plt.title("Mk 6/6a C of G Graph")
plt.figure(figsize = (5, 8))
plt.plot(x_values, y_values, marker = "x")
plt.plot(cofg_envelope_x, cofg_envelope_y, color = "black")
plt.plot(cofg_craning_envelope_x, cofg_craning_envelope_y, color = "black", linestyle = "--")
plt.show()

print("C of G calculated.")