data_nama = "Zilong"
data_umur = 17
data_tb = 170
data_alamat = "Semarang"


# ======= String standart
print("String Standart".center(40,"="))
print(f"Nama : {data_nama}, Umur : {data_umur}, Tinggi Badan : {data_tb}, Alamat : {data_alamat}")

# ======= String mengunakan enter/newline
print("String mengunakan enter/newline".center(40,"="))
print(f"Nama : {data_nama} \nUmur : {data_umur}, \nTinggi Badan : {data_tb}, \nAlamat : {data_alamat}")

#  ======= String menggunakan multiline triplets quote
print("String menggunakan multiline triplets quote".center(40,"="))
data_string = f"""
nama = {data_nama}
umur = {data_umur}
tb = {data_tb}
alamat = {data_alamat}
"""

print(data_string)

#  ======= Mengatur lebar string
print("Mengatur lebar string".center(40,"="))
data_string = f"""
nama = {data_nama:>10}
umur = {data_umur:>10}
tb = {data_tb:>10}
alamat = {data_alamat:>10}
"""

print(data_string)