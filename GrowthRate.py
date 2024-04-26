propionic_acid_conc = [0, 0.05, 0.1, 0.15, 0.2, 0.3]
od600_glu_day1 = [0.563, 0.5, 0.488, 0.481, 0.475, 0.492]
od600_no_glu_day1 = [0.504, 0.504, 0.495, 0.491, 0.48, 0.491]
ph_glu_day1 = [6.516, 6.439, 6.415, 6.477, 6.487, 6.602]
ph_no_glu_day1 = [6.457, 6.426, 6.428, 6.529, 6.576, 6.587]

od600_glu_day2 = [1.81, 0.764, 0.536, 0.592, 0.599, 0.519]
od600_no_glu_day2 = [1.74, 0.475, 0.674, 0.628, 0.541, 0.683]
ph_glu_day2 = [6.442, 6.44, 6.466, 6.519, 6.535, 6.651]
ph_no_glu_day2 = [6.09, 6.641, 6.47, 6.57, 6.591, 6.422]

od600_glu_final = [28.95, 12.2, 2.88, 1.152, 0.843, 0.693]
od600_no_glu_final = [34.2, 15.45, 3.22, 1.152, 0.864, 0.693]
ph_glu_final = [4.754, 5.303, 6.216, 6.532, 6.506, 6.638]
ph_no_glu_final = [4.603, 5.11, 6.143, 6.44, 6.524, 6.88]

import matplotlib.pyplot as plt
import numpy as np

pro_glu_0 = np.array([od600_glu_day1[0], od600_glu_day2[0], od600_glu_final[0]])
pro_glu_05 = np.array([od600_glu_day1[1], od600_glu_day2[1], od600_glu_final[1]])
pro_glu_1 = np.array([od600_glu_day1[2], od600_glu_day2[2], od600_glu_final[2]])
pro_glu_15 = np.array([od600_glu_day1[3], od600_glu_day2[3], od600_glu_final[3]])
pro_glu_2 = np.array([od600_glu_day1[4], od600_glu_day2[4], od600_glu_final[4]])
pro_glu_3 = np.array([od600_glu_day1[5], od600_glu_day2[5], od600_glu_final[5]])

pro_no_glu_0 = np.array(
    [od600_no_glu_day1[0], od600_no_glu_day2[0], od600_no_glu_final[0]]
)
pro_no_glu_05 = np.array(
    [od600_no_glu_day1[1], od600_no_glu_day2[1], od600_no_glu_final[1]]
)
pro_no_glu_1 = np.array(
    [od600_no_glu_day1[2], od600_no_glu_day2[2], od600_no_glu_final[2]]
)
pro_no_glu_15 = np.array(
    [od600_no_glu_day1[3], od600_no_glu_day2[3], od600_no_glu_final[3]]
)
pro_no_glu_2 = np.array(
    [od600_no_glu_day1[4], od600_no_glu_day2[4], od600_no_glu_final[4]]
)
pro_no_glu_3 = np.array(
    [od600_no_glu_day1[5], od600_no_glu_day2[5], od600_no_glu_final[5]]
)

fig = plt.figure(figsize=(5, 5))


plt.plot([0, 1, 4], pro_glu_0, color="#ADD8E6")
plt.plot([0, 1, 4], pro_glu_05, color="#3399FF")
plt.plot([0, 1, 4], pro_glu_1, color="#0000FF")
plt.plot([0, 1, 4], pro_glu_15, color="#0000CC")
plt.plot([0, 1, 4], pro_glu_2, color="#000099")
plt.plot([0, 1, 4], pro_glu_3, color="#000066")

plt.scatter([0, 1, 4], pro_glu_0, color="#ADD8E6", zorder=10, label="0.0 M")
plt.scatter([0, 1, 4], pro_glu_05, color="#3399FF", zorder=10, label="0.050 M")
plt.scatter([0, 1, 4], pro_glu_1, color="#0000FF", zorder=10, label="0.10 M")
plt.scatter([0, 1, 4], pro_glu_15, color="#0000CC", zorder=10, label="0.15 M")
plt.scatter([0, 1, 4], pro_glu_2, color="#000099", zorder=10, label="0.20 M")
plt.scatter([0, 1, 4], pro_glu_3, color="#000066", zorder=10, label="0.30 M")

plt.legend(title="Propionic acid conc. (M)", loc="upper left")
plt.tick_params(direction="in")
plt.xlabel("Time (day)")
plt.ylabel("OD600 (-)")

fig.savefig("images/OD600_glu.png", dpi=600)

fig = plt.figure(figsize=(5, 5))

plt.plot([0, 1, 4], pro_no_glu_0, color="#FFA07A")
plt.plot([0, 1, 4], pro_no_glu_05, color="#FF6347")
plt.plot([0, 1, 4], pro_no_glu_1, color="#FF4500")
plt.plot([0, 1, 4], pro_no_glu_15, color="#FF0000")
plt.plot([0, 1, 4], pro_no_glu_2, color="#CC0000")
plt.plot([0, 1, 4], pro_no_glu_3, color="#990000")


plt.scatter([0, 1, 4], pro_no_glu_0, color="#FFA07A", zorder=10, label="0.0 M")
plt.scatter([0, 1, 4], pro_no_glu_05, color="#FF6347", zorder=10, label="0.050 M")
plt.scatter([0, 1, 4], pro_no_glu_1, color="#FF4500", zorder=10, label="0.10 M")
plt.scatter([0, 1, 4], pro_no_glu_15, color="#FF0000", zorder=10, label="0.15 M")
plt.scatter([0, 1, 4], pro_no_glu_2, color="#CC0000", zorder=10, label="0.20 M")
plt.scatter([0, 1, 4], pro_no_glu_3, color="#990000", zorder=10, label="0.30 M")

plt.legend(title="Propionic acid conc. (M)", loc="upper left")
plt.tick_params(direction="in")
plt.xlabel("Time (day)")
plt.ylabel("OD600 (-)")

fig.savefig("images/OD600_no_glu.png", dpi=600)

# with glu/without glu
fig = plt.figure(figsize=(5, 5))

plt.plot([0, 1, 4], pro_glu_0 / pro_no_glu_0, color="#ADD8E6")
plt.plot([0, 1, 4], pro_glu_05 / pro_no_glu_05, color="#3399FF")
plt.plot([0, 1, 4], pro_glu_1 / pro_no_glu_1, color="#0000FF")
plt.plot([0, 1, 4], pro_glu_15 / pro_no_glu_15, color="#0000CC")
plt.plot([0, 1, 4], pro_glu_2 / pro_no_glu_2, color="#000099")
plt.plot([0, 1, 4], pro_glu_3 / pro_no_glu_3, color="#000066")

plt.scatter(
    [0, 1, 4], pro_glu_0 / pro_no_glu_0, color="#ADD8E6", zorder=10, label="0.0 M"
)
plt.scatter(
    [0, 1, 4], pro_glu_05 / pro_no_glu_05, color="#3399FF", zorder=10, label="0.050 M"
)
plt.scatter(
    [0, 1, 4], pro_glu_1 / pro_no_glu_1, color="#0000FF", zorder=10, label="0.10 M"
)
plt.scatter(
    [0, 1, 4], pro_glu_15 / pro_no_glu_15, color="#0000CC", zorder=10, label="0.15 M"
)
plt.scatter(
    [0, 1, 4], pro_glu_2 / pro_no_glu_2, color="#000099", zorder=10, label="0.20 M"
)
plt.scatter(
    [0, 1, 4], pro_glu_3 / pro_no_glu_3, color="#000066", zorder=10, label="0.30 M"
)

plt.legend(title="Propionic acid conc. (M)", loc="upper left")
plt.tick_params(direction="in")
plt.xlabel("Time (day)")
plt.ylabel("Relative OD600 (-)")

fig.savefig("images/OD600_ratio.png", dpi=600)


# # overlay
# fig = plt.figure(figsize=(5, 5))

# plt.plot([0, 1, 4], pro_glu_0, color="#ADD8E6")
# plt.plot([0, 1, 4], pro_glu_05, color="#3399FF")
# plt.plot([0, 1, 4], pro_glu_1, color="#0000FF")
# plt.plot([0, 1, 4], pro_glu_15, color="#0000CC")
# plt.plot([0, 1, 4], pro_glu_2, color="#000099")
# plt.plot([0, 1, 4], pro_glu_3, color="#000066")

# plt.scatter([0, 1, 4], pro_glu_0, color="#ADD8E6", zorder=10, label="0.0 M")
# plt.scatter([0, 1, 4], pro_glu_05, color="#3399FF", zorder=10, label="0.050 M")
# plt.scatter([0, 1, 4], pro_glu_1, color="#0000FF", zorder=10, label="0.10 M")
# plt.scatter([0, 1, 4], pro_glu_15, color="#0000CC", zorder=10, label="0.15 M")
# plt.scatter([0, 1, 4], pro_glu_2, color="#000099", zorder=10, label="0.20 M")
# plt.scatter([0, 1, 4], pro_glu_3, color="#000066", zorder=10, label="0.30 M")

# plt.plot([0, 1, 4], pro_no_glu_0, color="#FFA07A")
# plt.plot([0, 1, 4], pro_no_glu_05, color="#FF6347")
# plt.plot([0, 1, 4], pro_no_glu_1, color="#FF4500")
# plt.plot([0, 1, 4], pro_no_glu_15, color="#FF0000")
# plt.plot([0, 1, 4], pro_no_glu_2, color="#CC0000")
# plt.plot([0, 1, 4], pro_no_glu_3, color="#990000")

# plt.scatter([0, 1, 4], pro_no_glu_0, color="#FFA07A", zorder=10, label="0.0 M")
# plt.scatter([0, 1, 4], pro_no_glu_05, color="#FF6347", zorder=10, label="0.050 M")
# plt.scatter([0, 1, 4], pro_no_glu_1, color="#FF4500", zorder=10, label="0.10 M")
# plt.scatter([0, 1, 4], pro_no_glu_15, color="#FF0000", zorder=10, label="0.15 M")
# plt.scatter([0, 1, 4], pro_no_glu_2, color="#CC0000", zorder=10, label="0.20 M")
# plt.scatter([0, 1, 4], pro_no_glu_3, color="#990000", zorder=10, label="0.30 M")

# plt.legend(title="Propionic acid conc. (M)", loc="upper left")
# plt.tick_params(direction="in")
# plt.xlabel("Time (day)")
# plt.ylabel("OD600 (-)")

# fig.savefig("images/OD600_overlay.png", dpi=600)
# # End GrowthRate.py
