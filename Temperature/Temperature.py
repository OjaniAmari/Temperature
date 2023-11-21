def conv_temp(temperature, method):
    if method == "C_to_F":
        convert = temperature * 1.8 + 32
        return convert
    elif method == "F_to_C":
        convert = temperature -32 * (5 / 9) 
        return convert
    
    
print(conv_temp(32, "C_to_F")) # Converts 32 Celsius to Farenheit
print(conv_temp(100, "F_to_C")) # Converts 100 Farenheit to Celsius


