def convert_temperature(value, from_unit, to_unit):
    if from_unit == "C":
        if to_unit == "F":
            return value * 9/5 + 32
        elif to_unit == "K":
            return value + 273.15
    elif from_unit == "F":
        if to_unit == "C":
            return (value - 32) * 5/9
        elif to_unit == "K":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "K":
        if to_unit == "C":
            return value - 273.15
        elif to_unit == "F":
            return (value - 273.15) * 9/5 + 32
    return None

print(convert_temperature(100, 'C', 'F'))  # 212.0
print(convert_temperature(0, "K", "C"))  # -273.15
print(convert_temperature(-40, "C", "F"))  # -40.0
print(convert_temperature(20, "C", "X"))  #None