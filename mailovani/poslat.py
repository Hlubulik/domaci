import random
import smtplib
import time
from email.mime.text import MIMEText
import pandas as pd

# ==========================================
# 1. NASTAVENÍ E-MAILU A TEXTU
# ==========================================
MOJE_ADRESA = "honza.zilina@gmail.com"
MOJE_HESLO = "buoe sawk tnnq iyne"  # Heslo aplikace z účtu Google

PREDMET = "Nabídka spolupráce pro {firma}"

TEXT_ZPRAVY = """Dobrý den,

rád bych oslovil společnost {firma} s nabídkou spolupráce.

S pozdravem,
Tvoje Jméno
"""

# ==========================================
# 2. NAČTENÍ EXCELU
# ==========================================
try:
    df = pd.read_excel("kontakty.xlsx", engine="openpyxl")
    celkem_kontaktů = len(df)
    print(f"Úspěšně načteno {celkem_kontaktů} kontaktů z Excelu.\n")
except Exception as e:
    print(f"[CHYBA] Nepodařilo se načíst Excel: {e}")
    exit()

# ==========================================
# 3. ODESÍLÁNÍ E-MAILŮ (Samostatné připojení)
# ==========================================
for index, row in df.iterrows():
    firma = str(row["firma"]).strip()
    prijemce = str(row["email"]).strip()

    # Vytvoření e-mailu
    msg = MIMEText(TEXT_ZPRAVY.format(firma=firma), "plain", "utf-8")
    msg["From"] = MOJE_ADRESA
    msg["To"] = prijemce
    msg["Subject"] = PREDMET.format(firma=firma)

    # Připojení a odeslání pro každý e-mail zvlášť
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(MOJE_ADRESA, MOJE_HESLO)
        
        server.send_message(msg)
        server.quit()  # Řádné ukončení po odeslání

        print(f"[{index + 1}/{celkem_kontaktů}] OK: Odesláno pro {firma} ({prijemce})")

    except Exception as e:
        print(f"[{index + 1}/{celkem_kontaktů}] CHYBA při odesílání na {prijemce}: {e}")

    # Pauza před dalším e-mailem (mimo otevřené SMTP spojení)
    if index + 1 < celkem_kontaktů:
        pauza = random.randint(15, 35)
        print(f"   -> Čekám {pauza} sekund před dalším e-mailem...")
        time.sleep(pauza)

print("\n[HOTOVO] Zpracování všech kontaktů dokončeno!")