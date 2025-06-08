


# ========= latihan perulangan, membuat segitiga rata kiri

input_user = int(input("masukkan tinggi segitiga yang akan dibuat : "))
data = 0

while data < input_user:
    data += 1
    print("*" * data)
    
    
# ========== Latihan membuat segitiga rata kiriterbalik
input_user = int(input("Masukkan tinggi segitiga : "))
data = input_user

while data >= 1 :
    print("*" * data)
    data -= 1
    

# =======Latihan membuat segitiga rata kanan
tinggi = int(input("Masukkan berapa tinggi segitiga: "))
baris = 1

while baris <= tinggi:
    spasi = " " * (tinggi - baris)
    bintang = "*" * baris
    print(spasi + bintang)
    
    baris += 1

# =======Latihan membuat segitiga rata kanan terbalik
tinggi = int(input("Masukkan berapa tinggi segitiga: "))
baris = tinggi

while baris >= 1:
    bintang = "*" * baris 
    spasi = " " * (tinggi - baris)
    
    print(spasi + bintang)
    baris -= 1