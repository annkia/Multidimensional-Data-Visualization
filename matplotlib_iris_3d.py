# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import matplotlib
from matplotlib import rc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('iris.csv')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


x1 = df[df.Species=='setosa']['sepal_length']
y1 = df[df.Species=='setosa']['sepal_width']
z1 = df[df.Species=='setosa']['petal_length']

x2 = df[df.Species=='versicolor']['sepal_length']
y2 = df[df.Species=='versicolor']['sepal_width']
z2 = df[df.Species=='versicolor']['petal_length']

x3 = df[df.Species=='virginica']['sepal_length']
y3 = df[df.Species=='virginica']['sepal_width']
z3 = df[df.Species=='virginica']['petal_length']

ax.scatter(x1, y1, z1, c='blue', marker='o', label='Setosa')
ax.scatter(x2, y2, z2, c='orange', marker='o', label='Versicolor')
ax.scatter(x3, y3, z3, c='green', marker='o', label='Virginica')
ax.legend(loc='best', bbox_to_anchor=(1.1, 0.1))

ax.set_xlabel('Długość działki kielicha [cm]')
ax.set_ylabel('Szerokość działki kielicha [cm]')
ax.set_zlabel('Długość płatka korony [cm]')
ax.set_title('Stosunek długości działki kielicha do szerokości działki kielicha \n i długości płatka korony różnych odmian irysa')
# ax.set_title('Sepal length versus sepal width versus petal length for iris speciesąąąćććęęę')
plt.show()
