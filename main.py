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
        self.X, self.Y = np.array([[1, i] for i in self.conc]), np.array(
            self.OD360
        ).reshape(-1, 1)
        self.theta: list[float] = inv(self.X.T @ self.X) @ self.X.T @ self.Y
        self.r2: float = R2_(
            self.Y, [self.theta[0] + self.theta[1] * i for i in self.conc]
        )

    def __repr__(self) -> str:
        return f"STD. line : {self.theta[1][0]:.3f}C_V.B.12 + {self.theta[0][0]:.3f}, R^2 = {self.r2:.3f}"

    def convert_OD360(self, OD360: float) -> float:
        return (OD360 - self.theta[0][0]) / self.theta[1][0]

    def plot_std(self) -> None:
        fig = plt.figure(figsize=(8, 4))
        plt.tick_params(direction="in")
        plt.xlabel(r"$Conc._\text{V.B.12}$  (µg/ml)")
        plt.ylabel(r"$\text{OD}_{360}$")
        plt.scatter(self.conc, self.OD360, color="black")
        plt.plot(conc, [self.theta[0] + self.theta[1] * i for i in conc], color="red")
        OD360_tex: str = r"$\text{OD}_{360}$"
        plt.text(
            1,
            0.08,
            f"{OD360_tex} = {self.theta[1][0]:.3f}"
            + r"$C_\text{V.B.12}$"
            + f" + {self.theta[0][0]:.3f} ",
            fontsize=12,
        )
        r2: float = R2_(self.Y, [self.theta[0] + self.theta[1] * i for i in conc])
        plt.text(1, 0.07, r"$R^2 =$" + f"{r2:.3f}", fontsize=12)
        fig.savefig("out_Standard.png", dpi=500)


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
        self.pro_glu_0: np.ndarray = np.array(
            [
                self.data.OD600_with_glu_DAY1[0],
                self.data.OD600_with_glu_DAY2[0],
                self.data.OD600_with_glu_DAY3[0],
            ]
        )
        self.pro_glu_05: np.ndarray = np.array(
            [
                self.data.OD600_with_glu_DAY1[1],
                self.data.OD600_with_glu_DAY2[1],
                self.data.OD600_with_glu_DAY3[1],
            ]
        )
        self.pro_glu_1: np.ndarray = np.array(
            [
                self.data.OD600_with_glu_DAY1[2],
                self.data.OD600_with_glu_DAY2[2],
                self.data.OD600_with_glu_DAY3[2],
            ]
        )
        self.pro_glu_15: np.ndarray = np.array(
            [
                self.data.OD600_with_glu_DAY1[3],
                self.data.OD600_with_glu_DAY2[3],
                self.data.OD600_with_glu_DAY3[3],
            ]
        )
        self.pro_glu_2: np.ndarray = np.array(
            [
                self.data.OD600_with_glu_DAY1[4],
                self.data.OD600_with_glu_DAY2[4],
                self.data.OD600_with_glu_DAY3[4],
            ]
        )
        self.pro_glu_3: np.ndarray = np.array(
            [
                self.data.OD600_with_glu_DAY1[5],
                self.data.OD600_with_glu_DAY2[5],
                self.data.OD600_with_glu_DAY3[5],
            ]
        )
        self.pro_without_glu_0: np.ndarray = np.array(
            [
                self.data.OD600_without_glu_DAY1[0],
                self.data.OD600_without_glu_DAY2[0],
                self.data.OD600_without_glu_DAY3[0],
            ]
        )
        self.pro_without_glu_05: np.ndarray = np.array(
            [
                self.data.OD600_without_glu_DAY1[1],
                self.data.OD600_without_glu_DAY2[1],
                self.data.OD600_without_glu_DAY3[1],
            ]
        )
        self.pro_without_glu_1: np.ndarray = np.array(
            [
                self.data.OD600_without_glu_DAY1[2],
                self.data.OD600_without_glu_DAY2[2],
                self.data.OD600_without_glu_DAY3[2],
            ]
        )
        self.pro_without_glu_15: np.ndarray = np.array(
            [
                self.data.OD600_without_glu_DAY1[3],
                self.data.OD600_without_glu_DAY2[3],
                self.data.OD600_without_glu_DAY3[3],
            ]
        )
        self.pro_without_glu_2: np.ndarray = np.array(
            [
                self.data.OD600_without_glu_DAY1[4],
                self.data.OD600_without_glu_DAY2[4],
                self.data.OD600_without_glu_DAY3[4],
            ]
        )
        self.pro_without_glu_3: np.ndarray = np.array(
            [
                self.data.OD600_without_glu_DAY1[5],
                self.data.OD600_without_glu_DAY2[5],
                self.data.OD600_without_glu_DAY3[5],
            ]
        )

        self.pro_glu_0_mu = round(
            (np.log(self.pro_glu_0[1]) - np.log(self.pro_glu_0[0])) / 1, 2
        )
        self.pro_glu_05_mu = round(
            (np.log(self.pro_glu_05[1]) - np.log(self.pro_glu_05[0])) / 1, 2
        )
        self.pro_glu_1_mu = round(
            (np.log(self.pro_glu_1[1]) - np.log(self.pro_glu_1[0])) / 1, 2
        )
        self.pro_glu_15_mu = round(
            (np.log(self.pro_glu_15[1]) - np.log(self.pro_glu_15[0])) / 1, 2
        )
        self.pro_glu_2_mu = round(
            (np.log(self.pro_glu_2[1]) - np.log(self.pro_glu_2[0])) / 1, 2
        )
        self.pro_glu_3_mu = round(
            (np.log(self.pro_glu_3[1]) - np.log(self.pro_glu_3[0])) / 1, 2
        )
        self.pro_without_glu_0_mu = round(
            (np.log(self.pro_without_glu_0[1]) - np.log(self.pro_without_glu_0[0])) / 1,
            2,
        )
        self.pro_without_glu_05_mu = round(
            (np.log(self.pro_without_glu_05[1]) - np.log(self.pro_without_glu_05[0]))
            / 1,
            2,
        )
        self.pro_without_glu_1_mu = round(
            (np.log(self.pro_without_glu_1[1]) - np.log(self.pro_without_glu_1[0])) / 1,
            2,
        )
        self.pro_without_glu_15_mu = round(
            (np.log(self.pro_without_glu_15[1]) - np.log(self.pro_without_glu_15[0]))
            / 1,
            2,
        )
        self.pro_without_glu_2_mu = round(
            (np.log(self.pro_without_glu_2[1]) - np.log(self.pro_without_glu_2[0])) / 1,
            2,
        )
        self.pro_without_glu_3_mu = round(
            (np.log(self.pro_without_glu_3[1]) - np.log(self.pro_without_glu_3[0])) / 1,
            2,
        )

        self.ph_with_glu_day1: list[float] = np.array(self.data.pH_glu_DAY1)
        self.ph_with_glu_day2: list[float] = np.array(self.data.pH_glu_DAY2)
        self.ph_with_glu_day3: list[float] = np.array(self.data.pH_glu_DAY3)

        self.ph_without_glu_day1: list[float] = np.array(self.data.pH_without_glu_DAY1)
        self.ph_without_glu_day2: list[float] = np.array(self.data.pH_without_glu_DAY2)
        self.ph_without_glu_day3: list[float] = np.array(self.data.pH_without_glu_DAY3)

        self.ph_pro_glu_0: np.ndarray = np.array(
            [
                self.ph_with_glu_day1[0],
                self.ph_with_glu_day2[0],
                self.ph_with_glu_day3[0],
            ]
        )
        self.ph_pro_glu_05: np.ndarray = np.array(
            [
                self.ph_with_glu_day1[1],
                self.ph_with_glu_day2[1],
                self.ph_with_glu_day3[1],
            ]
        )
        self.ph_pro_glu_1: np.ndarray = np.array(
            [
                self.ph_with_glu_day1[2],
                self.ph_with_glu_day2[2],
                self.ph_with_glu_day3[2],
            ]
        )
        self.ph_pro_glu_15: np.ndarray = np.array(
            [
                self.ph_with_glu_day1[3],
                self.ph_with_glu_day2[3],
                self.ph_with_glu_day3[3],
            ]
        )
        self.ph_pro_glu_2: np.ndarray = np.array(
            [
                self.ph_with_glu_day1[4],
                self.ph_with_glu_day2[4],
                self.ph_with_glu_day3[4],
            ]
        )
        self.ph_pro_glu_3: np.ndarray = np.array(
            [
                self.ph_with_glu_day1[5],
                self.ph_with_glu_day2[5],
                self.ph_with_glu_day3[5],
            ]
        )

        self.ph_pro_without_glu_0: np.ndarray = np.array(
            [
                self.ph_without_glu_day1[0],
                self.ph_without_glu_day2[0],
                self.ph_without_glu_day3[0],
            ]
        )
        self.ph_pro_without_glu_05: np.ndarray = np.array(
            [
                self.ph_without_glu_day1[1],
                self.ph_without_glu_day2[1],
                self.ph_without_glu_day3[1],
            ]
        )
        self.ph_pro_without_glu_1: np.ndarray = np.array(
            [
                self.ph_without_glu_day1[2],
                self.ph_without_glu_day2[2],
                self.ph_without_glu_day3[2],
            ]
        )

        self.ph_pro_without_glu_15: np.ndarray = np.array(
            [
                self.ph_without_glu_day1[3],
                self.ph_without_glu_day2[3],
                self.ph_without_glu_day3[3],
            ]
        )
        self.ph_pro_without_glu_2: np.ndarray = np.array(
            [
                self.ph_without_glu_day1[4],
                self.ph_without_glu_day2[4],
                self.ph_without_glu_day3[4],
            ]
        )
        self.ph_pro_without_glu_3: np.ndarray = np.array(
            [
                self.ph_without_glu_day1[5],
                self.ph_without_glu_day2[5],
                self.ph_without_glu_day3[5],
            ]
        )

    def __repr__(self) -> str:
        ret = ""
        return ret

    def plot_growth_with_glu(self) -> None:
        fig = plt.figure(figsize=(5, 5))
        plt.plot([0, 1, 4], self.pro_glu_0, color="#ADD8E6")
        plt.plot([0, 1, 4], self.pro_glu_05, color="#3399FF")
        plt.plot([0, 1, 4], self.pro_glu_1, color="#0000FF")
        plt.plot([0, 1, 4], self.pro_glu_15, color="#0000CC")
        plt.plot([0, 1, 4], self.pro_glu_2, color="#000099")
        plt.plot([0, 1, 4], self.pro_glu_3, color="#000066")

        plt.scatter(
            [0, 1, 4],
            self.pro_glu_0,
            color="#ADD8E6",
            zorder=10,
            label=f"0.0 M µ={self.pro_glu_0_mu} " + r"$day^{-1}$",
        )
        plt.scatter(
            [0, 1, 4],
            self.pro_glu_05,
            color="#3399FF",
            zorder=10,
            label=f"0.050 M µ={self.pro_glu_05_mu} " + r"$day^{-1}$",
        )
        plt.scatter(
            [0, 1, 4],
            self.pro_glu_1,
            color="#0000FF",
            zorder=10,
            label=f"0.10 M µ={self.pro_glu_1_mu} " + r"$day^{-1}$",
        )
        plt.scatter(
            [0, 1, 4],
            self.pro_glu_15,
            color="#0000CC",
            zorder=10,
            label=f"0.15 M µ={self.pro_glu_15_mu} " + r"$day^{-1}$",
        )

        plt.scatter(
            [0, 1, 4],
            self.pro_glu_2,
            color="#000099",
            zorder=10,
            label=f"0.20 M µ={self.pro_glu_2_mu} " + r"$day^{-1}$",
        )
        plt.scatter(
            [0, 1, 4],
            self.pro_glu_3,
            color="#000066",
            zorder=10,
            label=f"0.30 M µ={self.pro_glu_3_mu} " + r"$day^{-1}$",
        )
        plt.legend(title="Propionic acid conc. (M)", loc="upper left")
        plt.tick_params(direction="in")
        plt.xlabel("Time (day)")
        plt.ylabel("OD600 (-)")
        plt.yscale("log")
        fig.savefig("out_OD600_glu.png", dpi=600)
        fig.clf()

    def plot_growth_without_glu(self) -> None:
        fig = plt.figure(figsize=(5, 5))
        plt.plot([0, 1, 4], self.pro_without_glu_0, color="#FFA07A")
        plt.plot([0, 1, 4], self.pro_without_glu_05, color="#FF6347")
        plt.plot([0, 1, 4], self.pro_without_glu_1, color="#FF4500")
        plt.plot([0, 1, 4], self.pro_without_glu_15, color="#FF0000")
        plt.plot([0, 1, 4], self.pro_without_glu_2, color="#CC0000")
        plt.plot([0, 1, 4], self.pro_without_glu_3, color="#990000")

        plt.scatter(
            [0, 1, 4],
            self.pro_without_glu_0,
            color="#FFA07A",
            zorder=10,
            label=f"0.0 M µ={self.pro_without_glu_0_mu} " + r"$day^{-1}$",
        )
        plt.scatter(
            [0, 1, 4],
            self.pro_without_glu_05,
            color="#FF6347",
            zorder=10,
            label=f"0.050 M µ={self.pro_without_glu_05_mu} " + r"$day^{-1}$",
        )
        plt.scatter(
            [0, 1, 4],
            self.pro_without_glu_1,
            color="#FF4500",
            zorder=10,
            label=f"0.10 M µ={self.pro_without_glu_1_mu} " + r"$day^{-1}$",
        )
        plt.scatter(
            [0, 1, 4],
            self.pro_without_glu_15,
            color="#FF0000",
            zorder=10,
            label=f"0.15 M µ={self.pro_without_glu_15_mu} " + r"$day^{-1}$",
        )
        plt.scatter(
            [0, 1, 4],
            self.pro_without_glu_2,
            color="#CC0000",
            zorder=10,
            label=f"0.20 M µ={self.pro_without_glu_2_mu} " + r"$day^{-1}$",
        )
        plt.scatter(
            [0, 1, 4],
            self.pro_without_glu_3,
            color="#990000",
            zorder=10,
            label=f"0.30 M µ={self.pro_without_glu_3_mu} " + r"$day^{-1}$",
        )

        plt.legend(title="Propionic acid conc. (M)", loc="upper left")
        plt.tick_params(direction="in")
        plt.xlabel("Time (day)")
        plt.ylabel("OD600 (-)")
        plt.yscale("log")
        fig.savefig("out_OD600_without_glu.png", dpi=600)

    def plot_pH_with_glu(self) -> None:
        fig_ph = plt.figure(figsize=(5, 5))
        plt.plot([0, 1, 4], self.ph_pro_glu_0, color="#ADD8E6")
        plt.plot([0, 1, 4], self.ph_pro_glu_05, color="#3399FF")
        plt.plot([0, 1, 4], self.ph_pro_glu_1, color="#0000FF")
        plt.plot([0, 1, 4], self.ph_pro_glu_15, color="#0000CC")
        plt.plot([0, 1, 4], self.ph_pro_glu_2, color="#000099")
        plt.plot([0, 1, 4], self.ph_pro_glu_3, color="#000066")

        plt.scatter(
            [0, 1, 4],
            self.ph_pro_glu_0,
            color="#ADD8E6",
            zorder=10,
            label="0.0 M",
        )
        plt.scatter(
            [0, 1, 4],
            self.ph_pro_glu_05,
            color="#3399FF",
            zorder=10,
            label="0.050 M",
        )

        plt.scatter(
            [0, 1, 4],
            self.ph_pro_glu_1,
            color="#0000FF",
            zorder=10,
            label="0.10 M",
        )
        plt.scatter(
            [0, 1, 4],
            self.ph_pro_glu_15,
            color="#0000CC",
            zorder=10,
            label="0.15 M",
        )

        plt.scatter(
            [0, 1, 4],
            self.ph_pro_glu_2,
            color="#000099",
            zorder=10,
            label="0.20 M",
        )

        plt.scatter(
            [0, 1, 4],
            self.ph_pro_glu_3,
            color="#000066",
            zorder=10,
            label="0.30 M",
        )

        plt.legend(title="Propionic acid conc. (M)", loc="lower left")
        plt.tick_params(direction="in")
        plt.xlabel("Time (day)")
        plt.ylabel("pH (-)")

        fig_ph.savefig("out_pH_glu.png", dpi=600)
        fig_ph.clf()

    def plot_pH_without_glu(self) -> None:
        fig_ph = plt.figure(figsize=(5, 5))
        plt.plot([0, 1, 4], self.ph_pro_without_glu_0, color="#FFA07A")
        plt.plot([0, 1, 4], self.ph_pro_without_glu_05, color="#FF6347")
        plt.plot([0, 1, 4], self.ph_pro_without_glu_1, color="#FF4500")
        plt.plot([0, 1, 4], self.ph_pro_without_glu_15, color="#FF0000")
        plt.plot([0, 1, 4], self.ph_pro_without_glu_2, color="#CC0000")
        plt.plot([0, 1, 4], self.ph_pro_without_glu_3, color="#990000")

        plt.scatter(
            [0, 1, 4],
            self.ph_pro_without_glu_0,
            color="#FFA07A",
            zorder=10,
            label="0.0 M",
        )
        plt.scatter(
            [0, 1, 4],
            self.ph_pro_without_glu_05,
            color="#FF6347",
            zorder=10,
            label="0.050 M",
        )
        plt.scatter(
            [0, 1, 4],
            self.ph_pro_without_glu_1,
            color="#FF4500",
            zorder=10,
            label="0.10 M",
        )
        plt.scatter(
            [0, 1, 4],
            self.ph_pro_without_glu_15,
            color="#FF0000",
            zorder=10,
            label="0.15 M",
        )
        plt.scatter(
            [0, 1, 4],
            self.ph_pro_without_glu_2,
            color="#CC0000",
            zorder=10,
            label="0.20 M",
        )
        plt.scatter(
            [0, 1, 4],
            self.ph_pro_without_glu_3,
            color="#990000",
            zorder=10,
            label="0.30 M",
        )

        plt.legend(title="Propionic acid conc. (M)", loc="lower left")
        plt.tick_params(direction="in")
        plt.xlabel("Time (day)")
        plt.ylabel("pH (-)")

        fig_ph.savefig("out_pH_without_glu.png", dpi=600)
        fig_ph.clf()


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
vb12.plot_std()


# # 比増殖速度の計算例
# # 　実測値を以下のようにクラスに渡す
# propionic_acid_conc = [0, 0.05, 0.1, 0.15, 0.2, 0.3]
# od600_glu_day1 = [0.563, 0.5, 0.488, 0.481, 0.475, 0.492]
# od600_no_glu_day1 = [0.504, 0.504, 0.495, 0.491, 0.48, 0.491]
# ph_glu_day1 = [6.516, 6.439, 6.415, 6.477, 6.487, 6.602]
# ph_no_glu_day1 = [6.457, 6.426, 6.428, 6.529, 6.576, 6.587]

# od600_glu_day2 = [1.81, 0.764, 0.536, 0.592, 0.599, 0.519]
# od600_no_glu_day2 = [1.74, 0.475, 0.674, 0.628, 0.541, 0.683]
# ph_glu_day2 = [6.442, 6.44, 6.466, 6.519, 6.535, 6.651]
# ph_no_glu_day2 = [6.09, 6.641, 6.47, 6.57, 6.591, 6.422]

# od600_glu_final = [28.95, 12.2, 2.88, 1.152, 0.843, 0.693]
# od600_no_glu_final = [34.2, 15.45, 3.22, 1.152, 0.864, 0.693]
# ph_glu_final = [4.754, 5.303, 6.216, 6.532, 6.506, 6.638]
# ph_no_glu_final = [4.603, 5.11, 6.143, 6.44, 6.524, 6.88]

# data = GrowthData(
#     propionic_acid_conc=propionic_acid_conc,
#     OD600_with_glu_DAY1=od600_glu_day1,
#     OD600_without_glu_DAY1=od600_no_glu_day1,
#     pH_glu_DAY1=ph_glu_day1,
#     pH_without_glu_DAY1=ph_no_glu_day1,
#     OD600_with_glu_DAY2=od600_glu_day2,
#     OD600_without_glu_DAY2=od600_no_glu_day2,
#     pH_glu_DAY2=ph_glu_day2,
#     pH_without_glu_DAY2=ph_no_glu_day2,
#     OD600_with_glu_DAY3=od600_glu_final,
#     OD600_without_glu_DAY3=od600_no_glu_final,
#     pH_glu_DAY3=ph_glu_final,
#     pH_without_glu_DAY3=ph_no_glu_final,
# )

# # プロットの実行
# growth_rate = GrowthRate(data)
# growth_rate.plot_growth_with_glu()
# growth_rate.plot_growth_without_glu()
# growth_rate.plot_pH_with_glu()
# growth_rate.plot_pH_without_glu()
