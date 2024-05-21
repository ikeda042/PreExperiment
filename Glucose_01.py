from functions import LinearRegression
import seaborn as sns

sns.set()
conc: list[float] = [0, 0.5, 1.0, 1.5, 2.0, 2.5]

# 検量線データ
# 試薬1をブランクとした場合のOD340
OD340_A1: list[float] = [0, 0.004, -0.002, 0.0, 0.0, -0.001]
OD340_A2: list[float] = [
    0,
    0.13,
    0.255,
    0.383,
    0.510,
    0.639,
]

OD340_Delta: list[float] = [OD340_A2[i] - OD340_A1[i] for i in range(len(conc))]
print(OD340_Delta)

L = LinearRegression(
    X=conc,
    Y=OD340_Delta,
    zero_intercept=True,
    xlabel="Glucose (mg/mL)",
    ylabel=r"$\Delta OD_{340}$",
    out_name="images/Glucose_01.png",
)

L.plot()


def delta(A1, A2) -> list[float]:
    return [j - i for i, j in zip(A1, A2)]


# なし 0
PA_000_A1 = [0.051, 0.050, 0.046]
PA_000_A2 = [0.363, 0.358, 0.247]
PA_000_DELTA_OD340 = delta(PA_000_A1, PA_000_A2)

PA_000_GLU_A1 = [L.predict_y(i) for i in PA_000_DELTA_OD340]

# なし 0.05
PA_005_A1 = [0.048, 0.051, 0.051]
PA_005_A2 = [0.319, 0.055, 0.296]
PA_005_DELTA_OD340 = delta(PA_005_A1, PA_005_A2)

PA_005_GLU_A1 = [L.predict_y(i) for i in PA_005_DELTA_OD340]


# なし 0.10
PA_010_A1 = [-0.001, -0.015, 0.050]
PA_010_A2 = [0.149, 0.229, 0.233]
PA_010_DELTA_OD340 = delta(PA_010_A1, PA_010_A2)

PA_010_GLU_A1 = [L.predict_y(i) for i in PA_010_DELTA_OD340]


# なし 0.15
PA_015_A1 = [0.050, 0.082, 0.049]
PA_015_A2 = [0.487, 0.412, 0.236]
PA_015_DELTA_OD340 = delta(PA_015_A1, PA_015_A2)

PA_015_GLU_A1 = [L.predict_y(i) for i in PA_015_DELTA_OD340]

# なし 0.20
PA_020_A1 = [0.051, 0.051, 0.050]
PA_020_A2 = [0.216, 0.258, 0.264]
PA_020_DELTA_OD340 = delta(PA_020_A1, PA_020_A2)

PA_020_GLU_A1 = [L.predict_y(i) for i in PA_020_DELTA_OD340]

# なし 0.30
PA_030_A1 = [0.055, 0.069, 0.051]
PA_030_A2 = [0.456, 0.475, 0.271]
PA_030_DELTA_OD340 = delta(PA_030_A1, PA_030_A2)

PA_030_GLU_A1 = [L.predict_y(i) for i in PA_030_DELTA_OD340]

# あり 0
PA_000_A1_GLC = [0.048, 0.048, 0.048]
PA_000_A2_GLC = [0.247, 0.314, 0.408]
PA_000_DELTA_OD340_GLC = delta(PA_000_A1_GLC, PA_000_A2_GLC)

PA_000_GLU_A1_GLC = [L.predict_y(i) for i in PA_000_DELTA_OD340_GLC]

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(9, 6))

days = [0, 1, 4]

plt.plot(days, PA_000_DELTA_OD340, label="P.A. 0.00 M", marker="o")
plt.plot(days, PA_005_DELTA_OD340, label="P.A. 0.05 M", marker="o")
plt.plot(days, PA_010_DELTA_OD340, label="P.A. 0.10 M", marker="o")
plt.plot(days, PA_015_DELTA_OD340, label="P.A. 0.15 M", marker="o")
plt.plot(days, PA_020_DELTA_OD340, label="P.A. 0.20 M", marker="o")
plt.plot(days, PA_030_DELTA_OD340, label="P.A. 0.30 M", marker="o")
plt.plot(days, PA_000_DELTA_OD340_GLC, label="P.A. 0.00 M (GLC +)", marker="o")

plt.xlabel("Day")
plt.ylabel(r"$\Delta OD_{340}$")
plt.legend()
# ticks to inside
plt.tick_params(direction="in")
plt.savefig("images/Glucose_01.png", dpi=400)
