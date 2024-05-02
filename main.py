import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score as R2_
import numpy as np
from numpy.linalg import inv


class VB12:
    def __init__(self, conc: list[float], OD360: list[float], blank: float):
        self.blank: float = blank
        self.conc: list[float] = conc
        self.OD360: list[float] = [
            OD360[i] - self.blank if i != 0 else OD360[i] for i in range(len(OD360))
        ]
        X, Y = np.array([[1, i] for i in self.conc]), np.array(self.OD360).reshape(
            -1, 1
        )
        self.theta: list[float] = inv(X.T @ X) @ X.T @ Y
        self.r2: float = R2_(Y, [self.theta[0] + self.theta[1] * i for i in self.conc])

    def __repr__(self) -> str:
        return f"STD. line : {self.theta[1][0]:.3f}C_V.B.12 + {self.theta[0][0]:.3f}, R^2 = {self.r2:.3f}"


# 検量線作成用のデータ
blank: float = 0.002
conc: list[float] = [0, 0.25, 0.5, 1, 2, 2.5, 4, 5]
OD360: list[float] = [0, 0.005, 0.009, 0.02, 0.04, 0.047, 0.087, 0.103]

a = VB12(conc, OD360, blank)

print(a)
