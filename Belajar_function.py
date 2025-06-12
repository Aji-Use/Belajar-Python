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