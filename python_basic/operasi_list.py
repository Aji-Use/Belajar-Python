# Belajar operasi list
"""
    1. .count() => Mengetahu jumlah data yang sama pada list    EX: list_name.count("nama_data")
    2. .index() => Mengetahui posisi index data berdasar nama   EX: list_name.index("nama_data")
    3. .sort()  => Mengurutkan data dari kecil ke besar         EX: list_name.sort()
    4. .reverse => mengurutkan data dari besar ke kecil (setelah di sort)   EX: list_name.reverse()
"""
# ========= mengetahui jumlah data yang sama pada list ==========
print("=======mengetahui jumlah data yang sama pada list========")

data = [1,6,2,5,2,6,3,6,9,5,3,4,4,6,3,7,2,6,1,2,3]

print(f"List data: {data}")

data_3 = data.count(3)
data_2 = data.count(2)

print(f"Jumlah data 3 adalah : {data_3}")
print(f"Jumlah data 2 adalah : {data_2}")


# ======= Mengetahui posisi index data berdasar nama =========
print("\n======= Mengetahui posisi index data berdasar nama =========")

data = ["roger", "gaban", "rayleight", "shirohige", "joyboy"]

index_joyboy = data.index("joyboy")
index_gaban = data.index("gaban")
print(f"Gaban berada di index ke: {index_joyboy}")
print(f"Gaban berada di index ke: {index_gaban}")


# ========= Mengurutkan data ===========
print("\n======= Mengurutkan data =========")

data = [1,6,2,5,2,6,3,6,9,5,3,4,4,6,3,7,2,6,1,2,3]
pirates = ["roger", "gaban", "rayleight", "shirohige", "joyboy"]

print(f"Data sebelum diurutkan: {data}")
print(f"Data sebelum diurutkan: {pirates}")

# Mengurutkan dari Kecil ke Besar
print("\n")

data.sort()
pirates.sort()

print(f"Data setelah diurutkan (Kecil - Besar): {data}")
print(f"Data setelah diurutkan (Kecil - Besar): {pirates}")

# Mengurutkan dari Besar ke Kecil (Harus setelah di sort)
print("\n")

data.reverse()
pirates.reverse()

print(f"Data setelah disort dari Besar ke Kecil: {data}")
print(f"Data setelah disort dari Besar ke Kecil: {pirates}")

# === atau ===
print("\n=== ATAU ===")

data = [1,6,2,5,2,6,3,6,9,5,3,4,4,6,3,7,2,6,1,2,3]
pirates = ["roger", "gaban", "rayleight", "shirohige", "joyboy"]

data.sort(reverse=True)
pirates.sort(reverse=True)

print(f"Data setelah disort dari Besar ke Kecil: {data}")
print(f"Data setelah disort dari Besar ke Kecil: {pirates}")

