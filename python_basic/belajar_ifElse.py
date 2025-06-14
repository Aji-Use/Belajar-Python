# Belajar if else

# ==========Belajar if inline
print("Belajar if inline".center(40, "="))

data = "koruptor"

if data == "koruptor": print("Musnahkan koruptor")
print("Akhir program")

# ======== Belajar if indentation (space kosong sebelah kiri)
print("Belajar if indentation".center(40, "="))

data = int(input("Masukkan angka lebih dari 5 : "))

if data <= 5 : 
    print("Angka yang anda masukkan salah")
print("Akhir dari program")


# Else statement
print("Belajar Else statement".center(40, "="))

data = input("Apakah anda koruptor (y/n) ? ")

if data == "y":
    print(f"Silahkan mati saja")
else :
    print("Baik, saya menghormati anda")
    