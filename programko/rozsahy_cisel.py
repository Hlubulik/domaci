
bit = int(input("Zadejte počet bitů: "))
print(f"Rozsah čísel: {bit - bit:,d} až {2**bit - 1:,d}, {int(-2**bit / 2):,d} až {int(2**bit / 2 - 1):,d}")