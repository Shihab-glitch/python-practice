# Problem 25 - Convert Temperature 

# Celsius to Fahrenheit

c = float(input("Enter the temperature in Celsius : "))
f = (c * 9/5) + 32
print("The temperature in Fahrenheit is :", f)

# Celciius to Kelvin
k = c + 273.15
print("The temperature in Kelvin is :", k)

# Fahrenheit to Celsius
f = float(input("Enter the temperature in Fahrenheit : "))
c = (f - 32) * 5/9
print("The temperature in Celsius is :", c)

# Fahrenheit to Kelvin
k = (f - 32) * 5/9 + 273.15
print("The temperature in Kelvin is :", k)

# Kelvin to Celsius
k = float(input("Enter the temperature in Kelvin : "))
c = k - 273.15
print("The temperature in Celsius is :", c)

# Kelvin to Fahrenheit
f = (k - 273.15) * 9/5 + 32
print("The temperature in Fahrenheit is :", f)