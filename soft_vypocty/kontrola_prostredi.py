"""Úplná nehodnocená kontrola pro cvičení 2; zdrojová data nemění."""
from pathlib import Path
import sys

print("Python:", sys.executable)
print("Pracovní složka:", Path.cwd())
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError as chyba:
    raise SystemExit("Chybí knihovna v tomto Pythonu. Vyberte prostředí .venv "
                     "nebo použijte připravený Colab. Podrobnosti: " + str(chyba))

soubor = Path("mereni_teploty.csv")
if not soubor.is_file():
    raise SystemExit("Chybí mereni_teploty.csv v pracovní složce. "
                     "Rozbalte balíček, otevřete jeho složku nebo nahrajte CSV do Colabu.")
data = pd.read_csv(soubor)
assert list(data.columns) == ["t", "T"], "Očekáváme hlavičku t,T."
assert data.shape == (241, 2), "Očekáváme 241 řádků a dva sloupce."
hodnoty = data.to_numpy(dtype=float)
assert np.isfinite(hodnoty).all(), "Data musí být konečná čísla."
print("OK: NumPy, pandas, Matplotlib; sloupce t,T; 241 řádků.")
plt.plot(data["t"], data["T"], ".-")
plt.xlabel("t [s]")
plt.ylabel("T [°C]")
plt.title("Kontrola prostředí — dodané měření teploty")
plt.grid(True)
plt.show()
print("Pokud se zobrazil graf, kontrola je dokončena. Tento skript se neodevzdává.")
