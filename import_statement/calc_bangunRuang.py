# Membuat kalkulator untuk bangun ruang
import math
import pyfiglet

# banner
banner = pyfiglet.figlet_format("Kalkulator Bangun Ruang")
print(banner)
print("="*60)

# function
def tabung():
    print("\n")
    jari = float(input("Masukkan jari-jari lingkaran: "))
    tinggi = float(input("Masukkan tinggi lingkaran: "))
    
    keliling = 2 * math.pi * jari
    luas = 2 * math.pi * jari * (jari + tinggi)
    volume = math.pi * (jari**2) * tinggi
    
    print("\n===== Hasil Perhitungan Bangun Tabung =====")
    print(f"Keliling Tabung adalah\t: {keliling}")
    print(f"Luas Tabung adalah\t: {luas}")
    print(f"Volume Tabung adalah\t: {volume}")
    
def kubus():
    print("\n")
    sisi = float(input("Masukkan sisi kubus: "))
    
    volume = sisi**3
    luas = 6 * (sisi**2)
    keliling = 12 * sisi
    diagonal_ruang =  sisi *  math.sqrt(3)
    diagonal_bidang = sisi * math.sqrt(2)
    
    print("\n===== Hasil Perhitungan Bangun Kubus =====")
    print(f"Volume Kubus adalah\t\t: {volume}" )
    print(f"Volume Kubus adalah\t\t: {luas}")
    print(f"Keliling Kubus adalah\t\t: {keliling}")
    print(f"Diagonal runag Kubus adalah\t: {diagonal_ruang}")
    print(f"Diagonal bidang Kubus adalah\t: {diagonal_bidang}")

def balok():
    print("\n")
    panjang = float(input("Masukkan panjang\t: "))
    lebar = float(input("Masukkan lebar\t\t: "))
    tinggi = float(input("Masukkan tinggi\t\t: "))
    
    volume = panjang * lebar * tinggi
    
    print("\n===== Hasil Perhitungan Bangun Balok =====")
    print(f"Volume Balok adalah: {volume}")
    
def option():
    print("1. Tabung")
    print("2. Kubus")
    print("3. Balok")
    
    option = input("Silahkan masukkan pilihan anda: ")
    
    if option == "1":
        tabung()
    elif option == "2":
        kubus()
    elif option == "3":
        balok()
    else:
        print("Masukkan jawaban dengan benar")
        
# Main Sistem 
# while True:
#     option()
    
#     while True:
#         step = input("Apakah anda ingin lanjut (y/n): ").lower()
        
#         if step in ['y', 'n']:
#             break
#         print("Silahkan Masukkan jawaban dengan benar (y/n)!")
        
#     if step == 'n':
#         break
        
    


     
    