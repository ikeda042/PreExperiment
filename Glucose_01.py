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
