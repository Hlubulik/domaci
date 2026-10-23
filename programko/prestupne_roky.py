rok = (1890, 2031)
for rok in range(rok[0], rok[1]+1):
    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
        print(f"{rok} je přestupný rok.")