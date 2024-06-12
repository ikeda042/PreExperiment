# Day 0, Day 1, Day 4 data
group_1_glu_p = [270.2, 306.8, 260.0]
group_1_pro_p = [44.2, 53.8, 147.2]
group_1_acet_p = [0, 0, 0]

group_1_glu_n = [244.0, 296.6, 236.0]
group_1_pro_n = [0, 12.4, 114.4]
group_1_acet_n = [0, 4.6, 0]

group_2_glu_p = [263.8, 227.8, 305.2]
group_2_pro_p = [89.6, 79.8, 135.0]
group_2_acet_p = [0, 0, 10.6]

group_2_glu_n = [236.6, 285.8, 236.8]
group_2_pro_n = [0, 15.8, 106.2]
group_2_acet_n = [0, 6.0, 0]

group_3_glu_p = [292.6, 256.6, 305.4]
group_3_pro_p = [149.6, 137.8, 167.0]
group_3_acet_p = [0, 0, 0]

group_3_glu_n = [249.4, 355.0, 254.6]
group_3_pro_n = [0, 18.8, 107.2]
group_3_acet_n = [0, 0, 34.4]

group_4_glu_p = [260.6, 360.4, 317.0]
group_4_pro_p = [179.8, 255.0, 228.6]
group_4_acet_p = [0, 0, 0]

group_4_glu_n = [219.8, 353.2, 254.6]
group_4_pro_n = [0, 16.2, 106.2]
group_4_acet_n = [0, 0, 0]

group_5_glu_p = [298.4, 254.0, 317.0]
group_5_pro_p = [308.8, 264.4, 337.4]
group_5_acet_p = [0, 0, 0]

group_5_glu_n = [263.2, 333.0, 0]
group_5_pro_n = [0, 12.8, 0]
group_5_acet_n = [0, 0, 0]

group_6_glu_p = [295.6, 275.2, 272.2]
group_6_pro_p = [42.4, 42.8, 130.6]
group_6_acet_p = [0, 0, 0]

group_6_glu_n = [234.2, 314.4, 0]
group_6_pro_n = [0, 26.2, 0]
group_6_acet_n = [0, 0, 0]

group_7_glu_p = [277.0, 276.2, 293.6]
group_7_pro_p = [94.0, 93.8, 153.6]
group_7_acet_p = [0, 0, 0]

group_7_glu_n = [341.0, 344.8, 0]
group_7_pro_n = [0, 19.2, 0]
group_7_acet_n = [0, 0, 0]

group_8_glu_p = [250.6, 245.6, 299.6]
group_8_pro_p = [127.6, 127.2, 171.6]
group_8_acet_p = [0, 0, 0]

group_8_glu_n = [336.2, 360.4, 0]
group_8_pro_n = [0, 19.8, 0]
group_8_acet_n = [0, 8.0, 0]

group_9_glu_p = [251.2, 249.0, 329.0]
group_9_pro_p = [0, 172.8, 237.8]
group_9_acet_p = [0, 0, 2.6]

group_9_glu_n = [376.2, 385.2, 0]
group_9_pro_n = [260.4, 14.6, 0]
group_9_acet_n = [0, 0, 0]

group_10_glu_p = [291.0, 298.6, 309.4]
group_10_pro_p = [312.2, 323.6, 346.4]
group_10_acet_p = [0, 0, 0]

group_10_glu_n = [296.8, 282.8, 0]
group_10_pro_n = [0, 19.2, 0]
group_10_acet_n = [0, 7.6, 0]


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Days
days = [0, 1, 4]

# Glucose data
group_glu_p = [
    [270.2, 306.8, 260.0],  # group 1
    [263.8, 227.8, 305.2],  # group 2
    [292.6, 256.6, 305.4],  # group 3
    [260.6, 360.4, 317.0],  # group 4
    [298.4, 254.0, 317.0],  # group 5
    [295.6, 275.2, 272.2],  # group 6
    [277.0, 276.2, 293.6],  # group 7
    [250.6, 245.6, 299.6],  # group 8
    [251.2, 249.0, 329.0],  # group 9
    [291.0, 298.6, 309.4],  # group 10
]

# Plotting the glucose levels
plt.figure(figsize=(10, 6))

for i, group in enumerate(group_glu_p, start=1):
    plt.plot(days, group, marker="o", label=f"Group {i}")

plt.xlabel("Days")
plt.ylabel("Glucose (M)")
plt.legend()
plt.savefig("images/glucose_levels.png", dpi=500)
plt.close()
plt.clf()

# Glucose n data
group_glu_n = [
    [244.0, 296.6, 236.0],  # group 1
    [236.6, 285.8, 236.8],  # group 2
    [249.4, 355.0, 254.6],  # group 3
    [219.8, 353.2, 254.6],  # group 4
    [263.2, 333.0, 0],  # group 5
    [234.2, 314.4, 0],  # group 6
    [341.0, 344.8, 0],  # group 7
    [336.2, 360.4, 0],  # group 8
    [376.2, 385.2, 0],  # group 9
    [296.8, 282.8, 0],  # group 10
]

plt.figure(figsize=(10, 6))

for i, group in enumerate(group_glu_n, start=1):
    plt.plot(days, group, marker="o", label=f"Group {i}")

plt.xlabel("Days")
plt.ylabel("Glucose (M)")
plt.legend()
plt.savefig("images/glucose_levels_n.png", dpi=500)
plt.close()
plt.clf()
