from functions import LinearRegression

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
PA_000_DELTA_OD340 = [PA_000_A2[i] - PA_000_A1[i] for i in range(len(PA_000_A1))]

# なし 0.05
PA_005_A1 = [0.048, 0.051, 0.051]
PA_005_A2 = [0.319, 0.055, 0.296]


# なし 0.10
PA_010_A1 = [-0.001, -0.015, 0.050]
PA_010_A2 = [0.149, 0.229, 0.233]

# なし 0.15
PA_015_A1 = [0.050, 0.082, 0.049]
PA_015_A2 = [0.487, 0.412, 0.236]

# なし 0.20
PA_020_A1 = [0.051, 0.051, 0.050]
PA_020_A2 = [0.216, 0.258, 0.264]

# なし 0.30
PA_030_A1 = [0.055, 0.069, 0.051]
PA_030_A2 = [0.456, 0.475, 0.271]

# あり 0
PA_000_A1_GLC = [0.048, 0.048, 0.048]
PA_000_A2_GLC = [0.247, 0.314, 0.408]

import matplotlib.pyplot as plt

fig = plt.figure(figsize=[6, 6])
