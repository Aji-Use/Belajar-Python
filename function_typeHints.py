# Belajar mengenal dan membuat function type hints


# Tidak menggunakan type hint
# jika function dihover, tidak memberi tahu tipe data parameter yang akan dimasukkan
def kurang(nilai1,nilai2):
    output = nilai1 - nilai2
    
    return output

hasil_kurang = kurang("usup","asep")
print(hasil_kurang)
print(type(hasil_kurang))



# Menggunakan type hint
# jika function dihover, akan memberi tahu tipe data parameter yang akan dimasukkan
def tambah(nilai1:int,nilai2:int) -> int: #:int dan -> int adalah type hint
    hasil = nilai1 + nilai2
    
    return hasil

HASIL_TAMBAH = tambah("usup","asep")
print(HASIL_TAMBAH)
print(type(HASIL_TAMBAH))