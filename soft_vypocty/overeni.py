import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('volny_pad_vzor.csv')
t, s = df['t'], df['s']
print(s.mean(), s.max())
import matplotlib.pyplot as plt
plt.plot(t, s)
plt.xlabel('t [s]'); plt.ylabel('s [m]')
plt.grid(True); plt.show()

m = pd.read_csv('teplota_zpracovana.csv')
tm = m['t']
T = m['T']
T_filtr = T.rolling(9, center=True,
min_periods=1).mean()
plt.plot(tm, T, '.', tm, T_filtr, '-')
plt.xlabel('t [s]'); plt.ylabel('T [°C]')
plt.legend(['Původní', 'Filtrovaná'])
plt.grid(True); plt.show()
