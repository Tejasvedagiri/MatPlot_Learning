# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

x = [1,2,3]
y = [3,4,5]

x1 = [11,22,33]
y1 = [33,44,55]


plt.plot(x, y, label="First")
plt.plot(x1, y1, label="Second")
plt.xlabel('X-axis')
plt.ylabel("Y-axis")
plt.title("First graph")
plt.legend()
plt.show()