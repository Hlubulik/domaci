import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = "volny_pad.csv"
df = pd.read_csv(file_path)
t = df["t"]
s = df["s"]
prumer = s.mean()
maximum = s.max()

plt.plot(t, s)
plt.xlabel("t [s]")
plt.ylabel("s [m]")
plt.grid(True)
plt.show()

m = pd.read_csv('mereni_teploty.csv')
tm = m['t']
T = m['T']
T_filtr = T.rolling(9, center=True, min_periods=1).mean()

plt.plot(tm, T, tm, T_filtr)
plt.xlabel('t [s]')
plt.ylabel('T [°C]')
plt.grid(True)
plt.show()

vystup = m.copy()
vystup['T_filtr'] = T_filtr
vystup.to_csv('teplota_zpracovana.csv', index=False)
np.savez('teplota_zpracovana.npz', t=tm.to_numpy(),
         T=T.to_numpy(), T_filtr=T_filtr.to_numpy())

# znovu načtítá
csv = pd.read_csv("teplota_zpracovana.csv")
npz = np.load("teplota_zpracovana.npz")

print("CSV_INFO")
print("CSV řádky:", len(csv))
print("CSV sloupce:", list(csv.columns))
print("CSV hodnoty sedí:", np.allclose(csv, vystup, atol=1e-10)) 
#np.allclose(a,b) - porovná prvky v polích a, b
#atol - absolute tolerance (absolutní odchylka)

print("NZP_INFO")
print("NZP řádky:", len(npz["t"]))
print("NZP sloupce:", list(npz.files))
print("NZP hondoty sedí:", np.allclose(npz["t"], tm) and np.allclose(npz["T"], T) and np.allclose(npz["T_filtr"], T_filtr))

print("VELIKOSTI")
print("Velikost CSV:", open("teplota_zpracovana.csv", "rb").seek(0, 2), "bajtů")
print("Velikost NPZ:", open("teplota_zpracovana.npz", "rb").seek(0, 2), "bajtů")

#porovnání čitelnosti a velikosti
#velikost csv: 6763 bajtů
#velikost nzp: 6520 bajtů
#csv - textový soubor, lze přečíst člověkem a je větší 
# #nzp - binární formát, nemůže jednodušše přečíst člověk, rychleji se načítá a má menší velikost