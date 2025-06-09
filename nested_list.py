# Belajar nested list

data_0 = [1,2,3]
data_1 = [4,5,6]

data_gorup = [data_0, data_1]

print(f"Data 0 \t\t: {data_0}")
print(f"Data 1 \t\t: {data_1}")
print(f"Data group \t: {data_gorup}")


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