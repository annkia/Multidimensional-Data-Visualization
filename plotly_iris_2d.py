# - *- coding: utf- 8 - *-
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
df = pd.read_csv('iris.csv')
trace_1 = go.Scatter(
    x = df[df.Species=='setosa']['sepal_length'],
    y = df[df.Species=='setosa']['sepal_width'],
    mode = 'markers',
    marker = dict(
        size = 8,
        symbol = 'circle'
    ),
    name = 'Setosa'
)
trace_2 = go.Scatter(
    x = df[df.Species=='versicolor']['sepal_length'],
    y = df[df.Species=='versicolor']['sepal_width'],
    mode = 'markers',
    marker = dict(
        size = 8,
        symbol = 'circle'
    ),
    name = 'Versicolor'
)
trace_3 = go.Scatter(
    x = df[df.Species=='virginica']['sepal_length'],
    y = df[df.Species=='virginica']['sepal_width'],
    mode = 'markers',
    marker = dict(
        size = 8,
        symbol = 'circle'
    ),
    name = 'Virginica'
)
data= [trace_1, trace_2, trace_3]
layout = go.Layout(
    title='Stosunek długości działki kielicha do szerokości działki kielicha różnych odmian irysa',
    xaxis = dict(title = 'Długość działki kielicha [cm]'),
    yaxis = dict(title = 'Szerokość działki kielicha [cm]')
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='iris_2d.html')
python
