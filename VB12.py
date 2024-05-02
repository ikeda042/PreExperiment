# OD360 = 0.021C_V.B.12 + 0.003
# V.B.12 = (OD360 - 0.003) / 0.021
PROPIONIC_ACID = [0, 0.05, 0.10, 0.15, 0.20, 0.30]

OD360_propionic_acid_p_1 = [0.444, 0.175, 0.162, 0.113, 0.135, 0.089]
OD360_propionic_acid_n_1 = [0.269, 0.253, 0.156, 0.025, 0.129, 0.099]
OD360_propionic_acid_p_2 = [0.329, 0.125, 0.126, 0.078, 0.098, 0.044]
OD360_propionic_acid_n_2 = [0.244, 0.216, 0.119, 0.025, 0.079, 0.074]
VB12_propionic_acid_p_1 = [
    (OD360 - 0.003) / 0.021 for OD360 in OD360_propionic_acid_p_1
]

VB12_propionic_acid_n_1 = [
    (OD360 - 0.003) / 0.021 for OD360 in OD360_propionic_acid_n_1
]

VB12_propionic_acid_p_2 = [
    (OD360 - 0.003) / 0.021 for OD360 in OD360_propionic_acid_p_2
]

VB12_propionic_acid_n_2 = [
    (OD360 - 0.003) / 0.021 for OD360 in OD360_propionic_acid_n_2
]
