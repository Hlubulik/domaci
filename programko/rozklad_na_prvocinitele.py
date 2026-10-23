
n = 360
def rozklad(n):
    while n % 2 == 0:
        return(2)
    else:
        n = n // 2          
    if n % 3 == 0:
        return(3)
    else:
        n = n // 3
    if n % 5 == 0:
        return(5)
    else:
        n = n // 5
    if n % 7 == 0:
        return(7)
    else:
        n = n // 7

print(f"Rozklad čísla {n} na prvočinitele je:{rozklad(n)}")