# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

population = [22,32,41,42,54,65,45,33,66,75,44,46,88,76,55,88,99]

bins = [10,20,30,40,50,60,70,80,90,100]

plt.hist(population, bins, label="Test", color = "RED")
plt.xlabel('X-axis')
plt.ylabel("Y-axis")
plt.title("First graph")
plt.legend()
plt.show()