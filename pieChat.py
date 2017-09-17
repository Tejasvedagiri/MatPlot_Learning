# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt



slices = [7,2,2,13]
color = ["RED","BLUE","GREEN","Yellow"]
activities = ['Sleeping','Eating','Working','Playing']
plt.pie(slices,
        labels = activities,
        colors = color,
        startangle = 90, 
        shadow= True,
        explode = (0,0.1,0.2,0),
        autopct = "%1.1f%%")




plt.title("First graph")
plt.legend()
plt.show()