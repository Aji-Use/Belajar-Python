# pengembangan dari Mini Project Konversi Suhu
# Dalam latihan ini saya menambhakan logika pengkondisian if, elif, dan else

import pyfiglet

banner = pyfiglet.figlet_format("KONVERSI SUHU")
print((banner))
print("Made by : @bagusk._aji")
print("="*80)


# Function from celcius
def celcius(suhu):
    print("Konversi suhu dari Celcius".center(40, "="))
    
    reamur = (4/5)*suhu
    fahrenheit = (9/5 * suhu)+32
    kelvin = suhu + 273
    
    print(f"Suhu Celcius ke Reamur \t\t: {reamur} R")
    print(f"Suhu Celcius ke Fahrenheit \t: {fahrenheit} F")
    print(f"Suhu Celcius ke Kelvin \t\t: {kelvin} K")
    
    
# Function from reamur
def reamur(suhu):
    print("Konversi suhu dari Reamur".center(40, "="))
    
    celcius = (5/4)*suhu
    fahrenheit = (9/4)*suhu + 32
    kelvin = (5/4)*suhu + 273
    
    print(f"Suhu Reamur ke Celcius \t\t: {celcius} C")
    print(f"Suhu Reamur ke Fahrenheit \t: {fahrenheit} F")
    print(f"Suhu Reamur ke Kelvin \t\t: {kelvin} K")
    
# Function from Fahrenheit
def fahrenheit (suhu):
    print("Konversi suhu dari Fahrenheit".center(40, "="))
    
    celcius = (5/9)*(suhu-32)
    reamur = (4/9)*(suhu-32)
    
    print(f"Suhu Fahrenheit ke Celcius \t: {celcius:.2f} C")
    print(f"Suhu Fahrenheit ke Reamur \t: {reamur:.2f} R")
    
# Function from Kelvin
def kelvin(suhu):
    print("Konversi suhu dari Kelvin".center(40, "="))
    
    celcius = suhu - 273
    reamur = (4/5)*(suhu-275)
    
    print(f"Suhu Kelvin ke Celcius \t: {celcius} C")
    print(f"Suhu Kelvin ke Reamur \t: {reamur} R")

satuan_suhu = input("Masukkan satuan suhu awal yang ingin dikonversi: ").lower()


if satuan_suhu == "c":
    print("Celcius")
    input_user = float(input("Masukkan suhu (C) : "))
    celcius(input_user)
elif satuan_suhu == "f":
    print("Fahrenheit")
    input_user = float(input("Masukkan suhu (F) : "))
    fahrenheit(input_user)
elif satuan_suhu == "r":
    print("Reamur")
    input_user = float(input("Masukkan suhu (R) : "))
    reamur(input_user)
elif satuan_suhu == "k":
    print("Kelvin")
    input_user = float(input("Masukkan suhu (K) : "))
    kelvin(input_user)
else:
    print("Silahkan masukkan satuan suhu dengan benar!")
    
    

    
    

    