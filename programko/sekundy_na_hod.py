
sek = input("Zadej počet sekund: ")
prevod_casu = int(sek)
den = prevod_casu // 86400
hod = (prevod_casu // 3600) % 24
min = (prevod_casu % 3600) // 60
sec = prevod_casu % 60
print(f"{den:02d}:{hod:02d}:{min:02d}:{sec:02d}")
