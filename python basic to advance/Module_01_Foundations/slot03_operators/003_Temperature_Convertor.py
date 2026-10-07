# slot 03 - temperature convertor
# celsius to fahrenheit and back

celsius = float(input("Enter today's celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("temperature in celsius: ", celsius)
print("temperature in fahrenheit: ", fahrenheit)

# fahrenheit to celsius
f = float(input("Enter a fahrenheit value: "))
c = (f - 32) * 5 / 9
print(f, "F =", round(c, 2), "C")


# ================= Sheet program =================
# Program 3 — Guided Practice: Celsius to Fahrenheit
# Complete this temperature converter
celsius = input("Enter temperature in Celsius: ")
celsius_num = int(celsius)
fahrenheit = (celsius_num * 9 / 5) + 32
print(celsius_num, "°C =", fahrenheit, "°F")

# Test: If user enters 0, should output: 0 °C = 32.0 °F
