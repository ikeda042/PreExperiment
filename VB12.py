# OD360 = 0.021C_V.B.12 + 0.003
# V.B.12 = (OD360 - 0.003) / 0.021
PROPIONIC_ACID = [0, 0.05, 0.10, 0.15, 0.20, 0.30]

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


def OD_to_conc(OD360):
    return (OD360 - 0.003) / 0.021


OD360_propionic_acid_p_1 = [0.444, 0.175, 0.162, 0.113, 0.135, 0.089]
OD360_propionic_acid_n_1 = [0.269, 0.253, 0.156, 0.025, 0.129, 0.099]
OD360_propionic_acid_p_2 = [0.329, 0.125, 0.126, 0.078, 0.098, 0.044]
OD360_propionic_acid_n_2 = [0.244, 0.216, 0.119, 0.025, 0.079, 0.074]

maxod = max(
    max(OD360_propionic_acid_p_1),
    max(OD360_propionic_acid_n_1),
    max(OD360_propionic_acid_p_2),
    max(OD360_propionic_acid_n_2),
)

VB12_propionic_acid_p_1 = [OD_to_conc(i) for i in OD360_propionic_acid_p_1]
VB12_propionic_acid_n_1 = [OD_to_conc(i) for i in OD360_propionic_acid_n_1]
VB12_propionic_acid_p_2 = [OD_to_conc(i) for i in OD360_propionic_acid_p_2]
VB12_propionic_acid_n_2 = [OD_to_conc(i) for i in OD360_propionic_acid_n_2]


# n = 1
fig = plt.figure(figsize=(8, 4))
# STD line for VB12 OD360 = 0.021VB_conc + 0.003

plt.plot(
    [0, maxod],
    [0.003, (maxod - 0.003) / 0.021],
    color="red",
)


plt.scatter(
    OD360_propionic_acid_n_1, VB12_propionic_acid_n_1, color="tab:blue", alpha=1
)
plt.scatter(OD360_propionic_acid_p_1, VB12_propionic_acid_p_1, color="tab:red", alpha=1)

# それぞれの点からx軸に対して垂直に線をおろす
for i in range(len(OD360_propionic_acid_n_1)):
    plt.plot(
        [OD360_propionic_acid_n_1[i], OD360_propionic_acid_n_1[i]],
        [0, VB12_propionic_acid_n_1[i]],
        color="tab:blue",
        alpha=0.5,
    )
    plt.plot(
        [OD360_propionic_acid_p_1[i], OD360_propionic_acid_p_1[i]],
        [0, VB12_propionic_acid_p_1[i]],
        color="tab:red",
        alpha=0.5,
    )

plt.legend(["Standard line", "Glu. - ", "Glu. +"])
plt.xlabel(r"$Conc._\text{V.B.12}$  (µg/ml)")
plt.ylabel(r"$\text{OD}_{360}$")
plt.tick_params(direction="in")

fig.savefig("images/VB121.png", dpi=500)

fig.clf()

# n = 2
fig = plt.figure(figsize=(8, 4))

plt.plot(
    [0, maxod],
    [0.003, (maxod - 0.003) / 0.021],
    color="red",
)

plt.scatter(
    OD360_propionic_acid_n_2, VB12_propionic_acid_n_2, color="tab:blue", alpha=1
)
plt.scatter(OD360_propionic_acid_p_2, VB12_propionic_acid_p_2, color="tab:red", alpha=1)

# それぞれの点からx軸に対して垂直に線をおろす
for i in range(len(OD360_propionic_acid_n_2)):
    plt.plot(
        [OD360_propionic_acid_n_2[i], OD360_propionic_acid_n_2[i]],
        [0, VB12_propionic_acid_n_2[i]],
        color="tab:blue",
        alpha=0.5,
    )
    plt.plot(
        [OD360_propionic_acid_p_2[i], OD360_propionic_acid_p_2[i]],
        [0, VB12_propionic_acid_p_2[i]],
        color="tab:red",
        alpha=0.5,
    )

plt.legend(["Standard line", "Glu. - ", "Glu. +"])
plt.xlabel(r"$Conc._\text{V.B.12}$  (µg/ml)")
plt.ylabel(r"$\text{OD}_{360}$")
plt.tick_params(direction="in")

fig.savefig("images/VB122.png", dpi=500)
