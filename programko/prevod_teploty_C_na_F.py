def celsius_to_fahrenheit(value):
    return (value * 9/5) + 32

def main():
    value = float(input("Temperature in Celsius: "))
    result = celsius_to_fahrenheit(value)
    print(result)

if __name__ == "__main__":
    main()