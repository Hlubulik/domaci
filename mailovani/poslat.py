import smtplib
from email.mime.text import MIMEText
import pandas as pd

# ==========================================
# NASTAVENÍ E-MAILU A TEXTU
# ==========================================
MOJE_ADRESA = "honza.zilina@gmail.com"
MOJE_HESLO = "buoe sawk tnnq iyne"  # Heslo aplikace z účtu Google

PREDMET = "Nabídka spolupráce pro {firma}"

TEXT_ZPRAVY = """Dobrý den,

rád bych oslovil společnost {firma} s nabídkou spolupráce.

S pozdravem,
Jan Zilina
"""

# ==========================================
# NAČTENÍ A ODESÍLÁNÍ
# ==========================================
# Načtení Excelu
df = pd.read_excel("kontakty.xlsx", engine="openpyxl")
# Připojení k SMTP serveru Gmailu
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(MOJE_ADRESA, MOJE_HESLO)

# Odesílání po jednotlivých řádcích
for index, row in df.iterrows():
    firma = str(row["firma"]).strip()
    prijemce = str(row["email"]).strip()

    # Vytvoření zprávy s úpravou jména firmy
    msg = MIMEText(TEXT_ZPRAVY.format(firma=firma), "plain", "utf-8")
    msg["From"] = MOJE_ADRESA
    msg["To"] = prijemce
    msg["Subject"] = PREDMET.format(firma=firma)

    # Odeslání
    server.send_message(msg)
    print(f"[OK] Odesláno na: {prijemce} ({firma})")

server.quit()
print("\n[HOTOVO] Všechny e-maily byly odeslány.")