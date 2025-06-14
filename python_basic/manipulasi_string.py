# Manipulasi String

# Menyambung string (string concate)
print('======= Menyambung String ========')
nama_depan = "Uzumaki"
nama_belakang = "Naruto"

nama_lengkap = nama_depan + " " + nama_belakang

print("Nama Depan :", nama_depan)
print("Nama Belakang :", nama_belakang)
print("Nama Lengkap =", nama_lengkap)

# Menghuting Pnajang String
print('\n======= Menghuting Pnajang String ========')
panjang_string = len(nama_lengkap)
print(panjang_string)

# Mengecek apakah karakter ada didalam string
print('\n======= Menghuting Pnajang String ========')

char = "z"
hasil = char in nama_lengkap
print("Cek apakah huruf 'z' ada didalam string", nama_lengkap, "\nhasil =",hasil)

# Indexing
print('\n======= Indexing ========')

print("Nama Lengkap :", nama_lengkap)
print("Index ke [0] :", nama_lengkap[0])
print("Index ke [1] :", nama_lengkap[1])
print("Index ke [-1] :", nama_lengkap[-1])
print("Index ke [-2] :", nama_lengkap[-2])
print("Index ke [0:3] :"+ nama_lengkap[0:4])
print("Index ke [2:8] :"+ nama_lengkap[2:9])
print("Index ke [0,2,4,6,8,10] :"+ nama_lengkap[0:10:2]) #[0:10:2] artinya, ambil index dari 0 sampai 10 dan kasih increment/jeda 2


# ========== Cek nilai item berdasar ASCII ============
print('\n======= Cek nilai item berdasar ASCII ========')
# Item paling Kecil
print("Item paling kecil dari " + nama_lengkap + "adalah =", min(nama_lengkap))

# Item Paling Besar
print("Item paling besar dari " + nama_lengkap + "adalah =", max(nama_lengkap))

print('\n======= Cek nilai ASCII ========')
ascii_code = ord(" ")
print("ASCII Code untuk spasi adalah =", str(ascii_code))

ascii_code = ord("z")
print("ASCII Code untuk spasi adalah =", str(ascii_code))

data = 120
print("Char untuk ASCII 120 adalah =", chr(data))
