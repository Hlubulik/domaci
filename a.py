

N = 5
total = 0

print("Enter 5 numbers:")
for i in range(1,N+1):
    num = float(input(f"Number {i}: "))
    total += i

average = total / N
print(f"The average of the entered numbers is: {average}")