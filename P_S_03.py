
# day1 

OD360_000_day1 = 0.473
OD360_005_day1 = 0.483 
OD360_010_day1 = 0.463
OD360_015_day1 = 0.458
OD360_020_day1 = 0.474
OD360_030_day1 = 0.449

OD360_000_day1_GLC = 0.474

pH_000_day1 = 6.799
pH_005_day1 = 6.787
pH_010_day1 = 6.799
pH_015_day1 = 6.806
pH_020_day1 = 6.820
pH_030_day1 = 6.877

pH_000_day1_GLC = 6.767


# day2

OD360_000_day2 = 0.436
OD360_005_day2 = 0.801
OD360_010_day2 = 0.684
OD360_015_day2 = 0.651
OD360_020_day2 = 0.634
OD360_030_day2 = 0.558

OD360_000_day2_GLC = 0.426

pH_000_day2 = 5.911
pH_005_day2 = 6.609
pH_010_day2 = 6.654
pH_015_day2 = 6.658
pH_020_day2 = 6.701
pH_030_day2 = 6.760

pH_000_day2_GLC = 5.934


# day3

OD360_000_day3 = 21.8

OD360_000_day3_GLC = 28.4

pH_000_day3 = 4.986

pH_000_day3_GLC = 4.950

# day4

OD360_000_day4 = 30.8

OD360_000_day4_GLC = 25.3

pH_000_day4 = 4.447

pH_000_day4_GLC = 4.501

# day5(last day)

OD360_000_day5 = 28.4
OD360_005_day5 = 17.2
OD360_010_day5 = 2.81
OD360_015_day5 = 1.33
OD360_020_day5 = 1.10
OD360_030_day5 = 0.96

OD360_000_day5_GLC = 27.6

pH_000_day5 = 4.418
pH_005_day5 = 4.801
pH_010_day5 = 5.899
pH_015_day5 = 6.268
pH_020_day5 = 6.318
pH_030_day5 = 6.486

pH_000_day5_GLC = 4.465


import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6, 6))
# OD360
OD360_000s = [OD360_000_day1, OD360_000_day2, OD360_000_day3, OD360_000_day4, OD360_000_day5]
days = [1, 2, 3, 4, 5]
plt.plot(days, OD360_000s, label='OD360_000')

OD360_005s = [OD360_005_day1, OD360_005_day2, OD360_000_day5]
days = [1, 2, 5]

plt.plot(days, OD360_005s, label='OD360_005')

OD360_010s = [OD360_010_day1, OD360_010_day2, OD360_000_day5]
days = [1, 2, 5]

plt.plot(days, OD360_010s, label='OD360_010')

OD360_015s = [OD360_015_day1, OD360_015_day2, OD360_000_day5]
days = [1, 2, 5]

plt.plot(days, OD360_015s, label='OD360_015')

OD360_020s = [OD360_020_day1, OD360_020_day2, OD360_000_day5]
days = [1, 2, 5]

plt.plot(days, OD360_020s, label='OD360_020')

OD360_030s = [OD360_030_day1, OD360_030_day2, OD360_000_day5]
days = [1, 2, 5]

plt.plot(days, OD360_030s, label='OD360_030')

plt.xlabel('days')
plt.ylabel('OD360')
plt.legend()
fig.savefig('OD360_P_S_3.png')