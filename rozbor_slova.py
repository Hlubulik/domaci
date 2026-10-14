
slovo = input("Zadejte slovo: ")
print(str(slovo))
print(f"Počet znaků: {int(len(slovo))}")
print(f"První znak: {slovo[0]}")
print(f"Poslední znak: {slovo[-1]}")
print(f"Slovo pozpátku: {slovo[::-1]}")
print(f"Velkymi písmeny: {slovo.upper()}")
if slovo == slovo[::-1]:
    print(f"Palindrom: True")
else:
    print(f"Palindrom: False")

