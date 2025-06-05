# Bebebrapa metode pembuatan string

# === Menggunakan Single Quote ===
print('\n======= Single Quote =======')
data = 'String dengan single quote'
ex = '"Contoh dengan Single Quote"'
print('Data = ', data, '\nContoh = ', ex)

# === Menggunakan Double Quote ===
print('\n======= Double Quote =======')
data = "String dengan Double Quote"
ex = "'String dengan double quote'"
ex1 = "Ini haru jum'at"
print('data =', data, '\nContoh 1= ', ex, '\nContoh 2 = ', ex1)


# Menggunakan \
print('\n======= Menggunakan \ =========')
# data ='Hari Jum'at' => ini akan error
data ='Hari Jum\'at'
print('Contoh 1 = ', data)

# backslash
# data1 = "C:\usr\share" #Syntax error
data1 = "C:\\usr\\share"
print('Contoh 2 =', data1)

# Tab
print('\n======= Menggunakan "\\t (Tab)"  =========')
sebelum = "Adit Denis"
sesudah = "Adit \tDenis => memberikan efek tab"
print("Sebelum =", sebelum, "\nSesudah =", sesudah)

# Backspace
print('\n======= Menggunakan "\\b (Tab)"  =========')
sebelum = "Adit Denis"
sesudah = "Adit \bDenis => memberikan efek backspace"
print("Sebelum =", sebelum, "\nSesudah =", sesudah)

# Backspace
print('\n======= Menggunakan "\\r (Escape Charakter)"  =========')
sebelum = "Adit Denis"
sesudah = "Adit \rDenis => memberikan efek backspace"
print("Sebelum =", sebelum, "\nSesudah =", sesudah)

# Syntax Error
print('\n======= Syntax Salah  =========')
print('C:\new folder')

# Raw String
print('\n======= Menggunakan "r (Raw String)"  =========')
print(r'C:\new folder')

# Multiline Literal String
print('\n======= Multiline Literal String  =========')
data = """
Nama    : Ucup
Hobi    : Mancing
Umur    : 1 bulan
"""
print(data)




