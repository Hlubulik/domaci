
n = int(input("Zadejte číslo: "))
for n in range(1, 101):
    if n % n == 0 and n % 1 == 0 and n >1 and n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0 or n == 2 or n == 3 or n == 5 or n == 7:
        i = "je prvočíslo"
        print(f"{n} {i}.")
    else:
        i = "není prvočíslo"
   
