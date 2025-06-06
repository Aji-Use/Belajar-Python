# Operasi dan manipulasi string 2
"""
    1. .count()
    2. .lower()
    3. .upper()
    4. .isupper()
    5. .islower()
    6. .isalpha() #Cek semuanya huruf
    7. .isalnum() #Cek huruf dan angka
    8. .isdecimal() #Cek angka saja
    9. .isspace() #Cek spasi, tab, newline
    10. .istitle() #Cek semua kata  dimulai dengan huruf besar
    11. .startswith() #Cek kata awal
    12. .endswith() #Cek kata akhir
"""

"""
    Penggabungan Komponen
    1. join()
    2. split()
"""


# ======= Melihat Jumlah Karakter pada String =======
print("======= Melihat Jumlah Karakter pada String ========")

data = "Sedang merintis career"
jumlah_a = str(data.count("a"))

print("Kalimat :"+ data + "Memiliki huruf 'a' sebanyak : " + jumlah_a)


# ======= Merubah Menjadi Uppercase
print("\n======= Merubah Menjadi Uppercase ========")

data = "semarang"

print("Data sebelum diubah = " + data)
print("Data sesudah dirubah = " + data.upper())

# ======= Merubah Menjadi Lowercase
print("\n======= Merubah Menjadi Uppercase ========")

data = "SEMARANG"

print("Data sebelum diubah = " + data)
print("Data sesudah dirubah = " + data.lower())

# ======= Pengecekan Lower/Uppercase
print("\n======= Pengecekan Lower/Uppercase ========")

data = "SEMARANG"
is_lower = data.islower()
is_upper = data.isupper()

print("Apakah " +data+ " adalah uppercase ? " + str(is_upper))
print("Apakah " +data+ " adalah lowercase ? " + str(is_lower))

# ======= Pengecekan isalpha(huruf)
print("\n======= Pengecekan Pengecekan isalpha(huruf) ========")

data = "SEMARANG"
data1 = "SEMARANG 123"

cek_data = data.isalpha()
cek_data1 = data1.isalpha()

print("Apakah " +"'"+data+"'"+ " adalah hanya huruf ? " + str(cek_data))
print("Apakah " +"'"+data1+"'"+ " adalah hanya huruf ? " + str(cek_data1))

# ======= Pengecekan isalnum(huruf dan angka)
print("\n======= Pengecekan Pengecekan isalpha(huruf) ========")

data = "'SEMARANG 123'"
data1 = "SEMARANG123"

cek_data = data.isalnum()
cek_data1 = data1.isalnum()

print("Apakah " +"'"+data+"'"+ " adalah hanya huruf dan angka ? " + str(cek_data))
print("Apakah " +"'"+data1+"'"+ " adalah hanya huruf dan angka ? " + str(cek_data1))

# ======= Pengecekan startswith() dan endswith()
print("\n======= Pengecekan startswith() dan endswith() ========")

data = "SEMARANG 123"


cek_data = data.startswith("SEMARANG")
cek_data1 = data.endswith("123")

print("Apakah kalimat " +"'"+data+"'"+ " diawali dengan kata "'SEMARANG'" ? " + str(cek_data))
print("Apakah kalimat " +"'"+data+"'"+ " diakhiri dengan kata "'123'" ? " + str(cek_data1))


# ======= Penggabungan Komponen join()
print("\n======= Penggabungan Komponen join() ========")

data = ['anggur', 'manggis', 'melon']

join_koma = ",".join(data)
join_space = " ".join(data)

print("Sebelum dengan fungsi 'join' = ", data)
print("Sesudah dengan fungsi 'join' = ", join_koma)
print("Sesudah dengan fungsi 'join' = ", join_space)

# ======= Merubah string menjadi list dengan split()
print("\n======= Merubah string menjadi list dengan split() ========")

data = "Manusia dengan sifat serakahnya"


print("Sebelum dengan fungsi 'join' = ", data)
print("Contoh 1: Sesudah dengan fungsi 'split' = ", data.split())
print("Contoh 2: Sesudah dengan fungsi 'split' = ", data.split('dengan'))

data = "apeltestjeruktestanggur"
print("Contoh 3: ", data.split('test'))

# ======= Alokasi karakter dengan rjust(), ljust(), center()
print("\n======= Alokasi karakter dengan rjust(), ljust(), center() ========")

kiri = "Manusia".ljust(10)
print("'"+kiri+"'")

kanan = "Manusia".rjust(10)
print("'"+kanan+"'")

center = "Manusia".center(10)
print("'"+center+"'")

manipulasi_center = "Manusia".center(20,"=")
print("'"+manipulasi_center+"'")

# menghilangkan
data = manipulasi_center.strip("=")
print(data)




