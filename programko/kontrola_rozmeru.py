
diameters = [25.01, 24.97, 25.06, 25.00, 24.94, 25.03, 25.05, 24.95, 25.10, 24.99]
dobry = 0
spatny = 0

for d in range(len(diameters)):
    if diameters[d] > 25.05:
        v = "velky"
        spatny += 1
    elif diameters[d] < 24.95:
        v = "maly"
        spatny += 1
    else:
        v = "OK"
        dobry += 1
    print(f"{d+1}: {diameters[d]} - {v}")
print(f"Pocet zmetku: {int(spatny / len(diameters) * 100)}%")
