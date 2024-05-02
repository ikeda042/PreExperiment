import matplotlib.pyplot as plt
from sklearn.metrics import r2_score as R2_
import numpy as np
from numpy.linalg import inv
from pydantic import BaseModel


class VB12:
    def __init__(self, conc: list[float], OD360: list[float], blank: float) -> None:
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

    def convert_OD360(self, OD360: float) -> float:
        return (OD360 - self.theta[0][0]) / self.theta[1][0]


class GrowthData(BaseModel):
    propionic_acid_conc: list[float] = [0, 0.05, 0.1, 0.15, 0.2, 0.3]
    OD600_with_glu_DAY1: list[float] | None
    OD600_without_glu_DAY1: list[float] | None
    pH_glu_DAY1: list[float] | None
    pH_without_glu_DAY1: list[float] | None

    OD600_with_glu_DAY2: list[float] | None
    OD600_without_glu_DAY2: list[float] | None
    pH_glu_DAY2: list[float] | None
    pH_without_glu_DAY2: list[float] | None

    OD600_with_glu_DAY3: list[float] | None
    OD600_without_glu_DAY3: list[float] | None
    pH_glu_DAY3: list[float] | None
    pH_without_glu_DAY3: list[float] | None


class GrowthRate:
    def __init__(self, data: GrowthData) -> None:
        self.data: GrowthData = data

    def __repr__(self) -> str:
        ret = ""
        return ret


# 検量線作成用のデータ

### ブランクのOD360 ###
blank: float = 0.002
### conc. V.B12　標準液(µg/ml) ###
conc: list[float] = [0, 0.25, 0.5, 1, 2, 2.5, 4, 5]
### OD360 nm ###
OD360: list[float] = [0, 0.005, 0.009, 0.02, 0.04, 0.047, 0.087, 0.103]


# 実行例
vb12 = VB12(conc, OD360, blank)
print(vb12)
print([vb12.convert_OD360(i) for i in [0.01, 0.02, 0.03, 0.04, 0.05]])
