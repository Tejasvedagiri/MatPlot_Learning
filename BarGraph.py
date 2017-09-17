# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


x = [1,3,5,7,9]
y = [6,7,8,2,4]

x1 = [10,8,6,4,2]
y1 = [4,2,8,7,6]


plt.bar(x, y, label="Test", color = "RED")
plt.bar(x1, y1, label="Test1", color = "Blue")

plt.xlabel('X-axis')
plt.ylabel("Y-axis")
plt.title("First graph")
plt.legend()
plt.show()
