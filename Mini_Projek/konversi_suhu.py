print("=" * 20, "KONVERSI SUHU", "=" * 20)

celcius = float(input("Masukkan suhu dalam celcius= "))
print("Suhu dalam Celsius= ", celcius, "C")

# fahrenheit
# print('-' * 40)
fahrenheit = (9/5) * celcius + 32
print("Suhu dalam Fahrenheit= ", fahrenheit, "F")

# reamur
# print('-' * 40)
reaumur = 4/5 * celcius
print("Suhu dalam Reaumur", reaumur, "R")

# kelvin
# print('-' * 40)
kelvin = celcius + 273
print("Suhu dalam Kelvin= ", kelvin, "K")