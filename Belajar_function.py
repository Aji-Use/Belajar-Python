# Belajar membuat fungsi

# =========== FUNCTION TANPA PARAMETER ===========
print("=========== FUNCTION TANPA PARAMETER ===========")

def option():
    print("Ini adalah function tanpa parameter ")
    
option()

# =========== FUNCTION DENGAN PARAMETER ===========
print("=========== FUNCTION DENGAN PARAMETER ===========")

# function tanpa return, hanya menampilkan pesan
# Membuat fungsi sederhana dengan nama sapa()
def sapa(nama):
    print(f"Halo, {nama}")
    
sapa("aji")


# function dengan return
def tambah(angka_1,angka_2):
    hasil = angka_1 + angka_2
    
    return hasil #return, akan mengembalikan hasil kedalam syntax sebelum function

HASIL = tambah(7,9) #akan mereturn hasil dari function tambah ke variabel HASIL
print(tambah(5,7)) 

print("---- Function dengan parameter lebih dari 1, dan cara mengambilnya ---")
def tiga_parameter(nilai1,nilai2,nilai3):
    hasil1 = nilai1**2
    hasil2 = nilai2**2
    hasil3 = nilai3**2
    
    return hasil1,hasil2,hasil3

HASIL1,HASIL2,HASIL3 = tiga_parameter(2,4,6)

print(HASIL1)
print(HASIL2)
print(HASIL3)