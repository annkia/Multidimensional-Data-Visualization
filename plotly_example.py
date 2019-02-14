import numpy as np
import pandas as pd
import plotly.offline as pyo
# create fake data:
df = pd.DataFrame(np.random.randn(10,5),columns='Azja Europa Afryka Ameryka Australia'.split())

pyo.plot([{
'x': df.index,
'y': df[col],
'name': col
} for col in df.columns])
