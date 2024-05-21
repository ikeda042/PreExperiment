import matplotlib.pyplot as plt
from sklearn.metrics import r2_score as R2_
import numpy as np
from numpy.linalg import inv


class LinearRegression:
    def __init__(
        self,
        X: list[float],
        Y: list[float],
        zero_intercept: bool,
        xlabel: str,
        ylabel: str,
        out_name: str,
    ) -> None:
        self.X: np.ndarray = (
            np.array(X).reshape(-1, 1)
            if zero_intercept
            else np.array([[1, i] for i in X])
        )
        self.Y: np.ndarray = np.array(Y).reshape(-1, 1)
        self.zero_intercept: bool = zero_intercept
        self.theta: np.ndarray = None
        self.theta: list[float] = inv(self.X.T @ self.X) @ self.X.T @ self.Y
        self.xlabel: str = xlabel
        self.ylabel: str = ylabel
        self.R2: float = R2_(self.Y, self.X @ self.theta)
        self.symbol: str = " + " if self.theta[0][0] > 0 else ""
        self.out_name: str = out_name

    def plot(self) -> None:
        plt.scatter(self.X[:, -1], self.Y)
        plt.plot(self.X[:, -1], self.X @ self.theta, color="black")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.tick_params(direction="in")
        plt.text(
            0.1,
            0.9,
            f"R2: {round(self.R2, 5)}",
            fontsize=12,
            transform=plt.gca().transAxes,
        )
        plt.text(
            0.1,
            0.8,
            (
                f"y = {round(self.theta[-1][0], 4)}x{self.symbol}{round(self.theta[0][0], 4)}"
                if not self.zero_intercept
                else f"y = {round(self.theta[0][0], 4)}x"
            ),
            fontsize=12,
            transform=plt.gca().transAxes,
        )
        plt.savefig(f"{self.out_name}", dpi=400)

    def predict(self, x: float) -> float:
        return (
            self.theta[0][0] * x
            if self.zero_intercept
            else self.theta[0][0] + self.theta[1][0] * x
        )


### ブランクのOD360 ###
blank: float = 0.002
### conc. V.B12　標準液(µg/ml) ###
conc: list[float] = [0, 0.25, 0.5, 1, 2, 2.5, 4, 5]
### OD360 nm ###
OD360: list[float] = [0, 0.005, 0.009, 0.02, 0.04, 0.047, 0.087, 0.103]

OD360_Delta: list[float] = [OD360[i] - blank for i in range(len(conc))]

L = LinearRegression(
    X=conc,
    Y=OD360_Delta,
    zero_intercept=True,
    xlabel="V.B12 (µg/ml)",
    ylabel=r"$ \text{OD}_{360}$",
    out_name="clean_docs/VB12_std_final.png",
)

L.plot()
