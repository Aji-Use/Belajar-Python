# Belajar nested list

data_0 = [1,2,3]
data_1 = [4,5,6]

data_gorup = [data_0, data_1]

print(f"Data 0 \t\t: {data_0}")
print(f"Data 1 \t\t: {data_1}")
print(f"Data group \t: {data_gorup}")


# ====== Mengambil data dari nested list ======
print("\n======= Mengambil data dari nested list =======")
data = data_gorup[0][1]

print(f"Nested list : {data_gorup}")
print(f"Data yang diambil index ke-0 dari nested list(data_0) dan data index ke-1 dari data_0(2) : {data}")


# ======= Contoh penggunaan =======
print("\n======= Contoh penggunaan =======")
pirates = ['luffy', 'zoro', 'sanji', 'usop']
yonko = ['shirohige', 'kaido', 'big mom', 'shanks']
admiral = ['akainu','aokiji',  'kizaru', 'ryokogyu']

one_piece = [pirates, yonko, admiral]

for karakter in one_piece:
    print(f"Kapten \t: {karakter[0]}")
    print(f"Wakil \t: {karakter[1]}")
    print(f"Anggota : {karakter[2:]} ")
    print(f"Anggota : {', '.join(karakter[2:])} \n")