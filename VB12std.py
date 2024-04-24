import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import numpy as np
from numpy.linalg import inv

# data fields
blank: float = 0.002
conc: list[float] = [0, 0.25, 0.5, 1, 2, 2.5, 4, 5]
OD360: list[float] = [0, 0.005, 0.009, 0.02, 0.04, 0.047, 0.087, 0.103]
OD360: list[float] = [
    OD360[i] - blank if i != 0 else OD360[i] for i in range(len(OD360))
]


fig = plt.figure(figsize=(8, 4))

plt.scatter(conc, OD360, color="black")

X, Y = np.array([[1, i] for i in conc]), np.array(OD360).reshape(-1, 1)
theta: list[float] = inv(X.T @ X) @ X.T @ Y

plt.plot(conc, [theta[0] + theta[1] * i for i in conc], color="red")
OD360_tex: str = r"$\text{OD}_{360}$"
plt.text(
    1,
    0.08,
    f"{OD360_tex} = {theta[1][0]:.3f}"
    + r"$C_\text{V.B.12}$"
    + f" + {theta[0][0]:.3f} ",
    fontsize=12,
)

r2: float = r2_score(Y, [theta[0] + theta[1] * i for i in conc])
plt.text(1, 0.07, r"$R^2 =$" + f"{r2:.3f}", fontsize=12)

# set ticks to the inside
plt.tick_params(direction="in")
plt.xlabel(r"$Conc._\text{V.B.12}$  (µg/ml)")
plt.ylabel(r"$\text{OD}_{360}$")
plt.savefig("Standard.png", dpi=500)
