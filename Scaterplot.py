# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt

x= [2,3,5,6,1,4,5,8,2,4,5,7,3]
y= [2,3,5,6,1,4,5,8,2,4,5,7,3]

plt.scatter(x, y, label="Test", color = "RED" , s = 200)
plt.xlabel('X-axis')
plt.ylabel("Y-axis")
plt.title("First graph")
plt.legend()
plt.show()