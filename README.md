# プレ学生実験データ

# V.B12 比色定量

[V.B12比色定量に関する実験データ](VB12.md)
# 培養
[エクセルデータ](OD600_PH_data_raw.xlsx)
## １日目(04/22, 22:00)

前培養OD600 = 11.27

### OD600

| プロピオン酸濃度[M] | 0     | 0.05  | 0.1   | 0.15  | 0.2   | 0.3   |
|:---------------:|-------|-------|-------|-------|-------|-------|
| 補糖あり           | 0.563 | 0.5   | 0.488 | 0.481 | 0.475 | 0.492 |
| 補糖なし           | 0.504 | 0.504 | 0.495 | 0.491 | 0.48  | 0.491 |

### pH

| プロピオン酸濃度[M] | 0     | 0.05  | 0.1   | 0.15  | 0.2   | 0.3   |
|:---------------:|-------|-------|-------|-------|-------|-------|
| 補糖あり           | 6.516 | 6.439 | 6.415 | 6.477 | 6.487 | 6.602 |
| 補糖なし           | 6.457 | 6.426 | 6.428 | 6.529 | 6.576 | 6.587 |


## 2日目 (04/23, 22:00)

### OD600

| プロピオン酸濃度[M] | 0     | 0.05  | 0.1   | 0.15  | 0.2   | 0.3   |
|----------|-------|-------|-------|-------|-------|-------|
| 補糖あり    | 1.81  | 0.764 | 0.536 | 0.592 | 0.599 | 0.519 |
| 補糖なし    | 1.74  | 0.475 | 0.674 | 0.628 | 0.541 | 0.683 |

### pH

| プロピオン酸濃度[M] | 0     | 0.05  | 0.1   | 0.15  | 0.2   | 0.3   |
|----------|-------|-------|-------|-------|-------|-------|
| 補糖あり    | 6.442 | 6.44  | 6.466 | 6.519 | 6.535 | 6.651 |
| 補糖なし    | 6.09  | 6.641 | 6.47  | 6.57  | 6.591 | 6.422 |

## 最終日 (04/26, 21:00)

### OD600
| プロピオン酸濃度[M] | 0     | 0.05  | 0.1   | 0.15  | 0.2   | 0.3   |
|----------|-------|-------|-------|-------|-------|-------|
| 補糖あり    | 28.95 | 12.2 | 2.88 | 1.152 | 0.843 | 0.693 |
| 補糖なし    | 34.2  | 15.45 | 3.22 | 1.152 | 0.864 | 0.693 |

### pH

| プロピオン酸濃度[M] | 0     | 0.05  | 0.1   | 0.15  | 0.2   | 0.3   |
|----------|-------|-------|-------|-------|-------|-------|
| 補糖あり    | 4.754 | 5.303 | 6.216 | 6.532 | 6.506 | 6.638 |
| 補糖なし    | 4.603  | 5.11 | 6.143 | 6.44 | 6.524 | 6.88 |


# 結果

## OD600の推移

### 補糖あり

![alt text](images/OD600_glu.png)

### 補糖なし

![alt text](images/OD600_no_glu.png)

## pHの推移

### 補糖あり

![alt text](images/pH_glu.png)

### 補糖なし

![alt text](images/pH_no_glu.png)



# Setup a python virtual environment 

1. Create a virtual environment for python3

```Bash
python3 -m venv venv
```
2. Activate the venv

```Bash
source venv/bin/activate
```
3. Leave the environment 

```Bash
deactivate
```

# Commands

## UPDATE requirements.txt

```Bash
pip freeze > requirements.txt
```

# Fitting scripts

```Python
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score as R2_
import numpy as np
from numpy.linalg import inv


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

```