# - *- coding: utf- 8 - *-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# create fake data:
df = pd.DataFrame(np.random.randn(10,5),columns='Azja Europa Afryka Ameryka Australia'.split())
df.plot()
plt.show()
