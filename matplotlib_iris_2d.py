# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()
ax = fig.add_subplot(111)
df = pd.read_csv('iris.csv')


x1 = df[df.Species=='setosa']['sepal_length']
y1 = df[df.Species=='setosa']['sepal_width']

x2 = df[df.Species=='versicolor']['sepal_length'],
y2 = df[df.Species=='versicolor']['sepal_width'],

x3 = df[df.Species=='virginica']['sepal_length'],
y3 = df[df.Species=='virginica']['sepal_width'],

ax.scatter(x1, y1,  c='blue', marker='o', label='Setosa')
ax.scatter(x2, y2, c='orange', marker='o', label='Versicolor')
ax.scatter(x3, y3,  c='green', marker='o', label='Virginica')
ax.legend(loc='best')


ax.set_xlabel('Długość działki kielicha [cm]')
ax.set_ylabel('Szerokość działki kielicha [cm]')
ax.set_title('Stosunek długości działki kielicha do szerokości \n działki kielicha różnych odmian irysa')

plt.show()
