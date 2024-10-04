import time
import json
import numpy as np
import matplotlib.pyplot as plt


# def check(col, row):
#     for i in range(row):
#         if res[i] == col or res[i] + i == row + col or res[i] - i == col - row:
#             return False
#     return True
#
#
# def dfs(row):
#     if row == size:
#         return
#     for col in range(size):
#         if check(col, row):
#             res[row] = col
#             dfs(row + 1)
#             res[row] = -1


# elapsed_times = []
# for size in range(14):
#     res = [-1] * size
#     elapsed_time = 0
#     for i in range(3):
#         start_time = time.time()
#         dfs(0)
#         end_time = time.time()
#         elapsed_time += end_time - start_time
#     print(elapsed_time)
#     elapsed_times.append(elapsed_time)
# json.dump(elapsed_times, open('times.json', 'w'))
times = json.load(open('times.json'))
print(times)

plt.figure(figsize=(10, 10))
axes1 = plt.subplot(121)
plt.plot(times, color='#57A9D1', label='time', linewidth=3)
plt.ylim(times[0], times[-1])
plt.xlabel('queen', fontsize=14)
plt.ylabel('time(sec)', fontsize=14)
[axes1.spines[loc_axis].set_visible(False) for loc_axis in ['top', 'right']]
plt.show()