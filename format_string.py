# formating string
"""
    1. f = format
    2. .d = desimal
    3. .f = float
"""

# ======= Generic =======
print("GENERIC".center(30, "="))
first_name = "Hasirama"
last_name = "Zilong"
full_name = f"Nama : {first_name} {last_name}"

print(full_name)

# ======= Angka =======
print("ANGKA".center(30, "="))
angka = 2500.50
name = f"Angka anda : {angka}"

print(name)

# ======= Bilangan Bulat=======
print("BILANGAN BULAT".center(30, "="))
angka = 2500
name = f"Angka anda : {angka:d}"

print(name)

# ======= Bilangan Dengan Ordo Ribuan =======
print("BILANGAN DENGAN ORDO RIBUAN".center(30, "="))
angka = 25000000000
name = f"Angka anda : {angka:,}"

print(name)

# ======= Bilangan Desimal =======
print("BILANGAN DESIMAL".center(30, "="))
angka = 2500.92348
angka1 = 2500.92348

name = f"Contoh 1 : {angka:.2f}" #2 => tiga angka dibelakang koma | f => float
name1 = f"Contoh 2 : {angka:.4f}" #4 => tiga angka dibelakang koma | f => float

print(name)
print(name1)

# ========== Menampilkan tanda - atau +
print("Menampilkan tanda - atau +".center(30, "="))
angka_minus = -10
angka_plus = 20
angka_ribuan = 190.0131
format_minus = f"Angka Minus = {angka_minus:+}"
format_plus = f"Angka Plus = {angka_plus:+}"
format_ribuan = f"Angka Ribuan = {angka_ribuan:+.3f}"

print(format_minus)
print(format_plus)
print(format_ribuan)

# ========== Format Persentase
print("Format Persentase".center(30, "="))

data = 0.23727
print(f"Contoh 1 Data anda : {data:%}")
data1 = 0.23727
print(f"Contoh 2 Data anda : {data1:.2%}")


# =========== Menampilkan Leading Zero
print("Menampilkan Leading Zero".center(30, "="))
data = 2003.0803
ex_1 = f"Contoh 1 : {data:.3f}"
ex_2 = f"Contoh 2 : {data:10.3f}"
ex_3 = f"Contoh 3 : {data:010.3f}"
ex_4 = f"Contoh 4 : {data:110.3f}"

print(ex_1)
print(ex_2)
print(ex_3)
print(ex_4)


# ======= Format angka dalam hexadecimal, binary, octal
print("Format angka dalam hexadecimal, binary, octal".center(30, "="))

data = 255

data1 = {bin(data)}
data2 = {hex(data)}
data3 = {oct(data)}

print(f"Format angka dalam Binary : {data1}")
print(f"Format angka dalam Hexa : {data2}")
print(f"Format angka dalam Octal : {data3}")