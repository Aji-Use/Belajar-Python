# exception akan terjadi saat program mengalamai error saat runtime

"""
    Contoh program error saat runtime
    saat user memasukkan angka 0, maka program akan error karena hasilnya tidak terdefinisi
"""

# input_user = int(input("Masukkan angka: "))

# hasil = 10/input_user
# print(hasil)


"""
    Bagaimana cara agar progam tetap berjalan ketika mengalami error saat runtime
    atau cara menangani error tersebut.
    dengan try except
"""

#=========== CONTOH SEDERHANA ===========
input_user = int(input("Masukkan angka: "))
hasil = None

try:
    hasil = 10/input_user #berikan kondisi yang membuat error
except:
    print("input tidak boleh 0") #tampilkan pesan kesalahan/penanganan
    
print(f"hasil: {hasil}")



# ============ CONTOH PENERAPAN =============
while True:
    input_data = int(input("Masukkan angka pembagi: "))
    
    try:
        hasil = 10/input_data
        print(f"Hasil: {hasil}")
        
        is_next = input("Apakah anda ingin lanjut (y/n): ")
        if is_next == 'n':
            break
    except:
        print("angka yang dimasukkan tidak boleh 0")
        

# ========= Mengambil Keterangan Errornya dan menjadikannya sebagai pesan ========
"""
    Exception = mengambil pesan (penyebab error nya)
    as error_message = memasukkkan pesan erro ke dalam variabel error_message
    print(error_message) = mencetak pesan errornya
"""
angka = 0

print("-------- cara 1 --------")
try:
    hasil = 10/angka
except Exception as error_message:
    print(error_message)


print("-------- cara 2 --------")
"""
    ZeroDivisionError = keterangan error dari sistemnya
"""
try:
    hasil = 10/angka
except ZeroDivisionError as error_message:
    print(error_message)
    
