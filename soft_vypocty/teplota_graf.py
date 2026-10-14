import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('volny_pad_552201.csv')
t, s = df['t'], df['s']
print(s.mean(), s.max())
import matplotlib.pyplot as plt
plt.plot(t, s)
plt.xlabel('t [s]'); plt.ylabel('s [m]')
plt.grid(True); plt.show()

m = pd.read_csv('mereni_teploty.csv')
tm = m['t']
T = m['T']
T_filtr = T.rolling(9, center=True,
min_periods=1).mean()
plt.plot(tm, T, '.', tm, T_filtr, '-')
plt.xlabel('t [s]'); plt.ylabel('T [°C]')
plt.legend(['Původní', 'Filtrovaná'])
plt.grid(True); plt.show()

vystup = m.copy()
vystup['T_filtr'] = T_filtr
vystup.to_csv('teplota_zpracovana.csv', index=False)
np.savez('teplota_zpracovana.npz', t=tm.to_numpy(),
T=T.to_numpy(), T_filtr=T_filtr.to_numpy())