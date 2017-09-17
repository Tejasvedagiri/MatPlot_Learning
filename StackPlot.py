# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]
sleeping = [8,7,6,7,8,7,8]
eating = [1,2,2,3,2,3,2]
working = [10,10,11,9,10,2,2]
playing = [5,5,5,5,4,12,12]

plt.plot([],[],color = "RED",label = "sleeping")
plt.plot([],[],color = "BLUE",label = "eating")
plt.plot([],[],color = "GREEN",label = "working")
plt.plot([],[],color = "BLACK",label = "playing")
plt.stackplot(days, sleeping ,eating , working , playing,colors = ["RED","BLUE","GREEN","BLACK"])



plt.xlabel('X-axis')
plt.ylabel("Y-axis")
plt.title("First graph")
plt.legend()
plt.show()