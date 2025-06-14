# Belajar looping list dan enumerate

# ====== for loop ======
print("====== for loop ======")

data = ['apel', 'manggis', 'jeruk', 'melon', 'anggur']

for i in data:
    print(f"buah : {i}")

# ====== for loop with range ======
print("\n====== for loop with range ======")

data = ['apel', 'manggis', 'jeruk', 'melon', 'anggur']
panjang = len(data)

for i in range(panjang):
    print(f"buah : {data[i]}")
    

# ====== while loop ======
print("\n====== while loop ======")

data = ['apel', 'manggis', 'jeruk', 'melon', 'anggur']

panjang = len(data)
index = 0

while index < panjang:
    print(f"Buah : {data[index]}")
    index +=1


# ====== Loop Comprehension ======
print("\n====== Loop Comprehension ======")

data = ['apel', 'manggis', 'jeruk', 'melon', 'anggur']

[print(f"Buah : {i}") for i in data]


# ====== List Enumerate ======
print("\n====== List Enumerate ======")

data = ['apel', 'manggis', 'jeruk', 'melon', 'anggur']

for index, data in enumerate(data):
    print(f"index : {index}, data : {data}")
    
# Tidak bisa, karena tidak menggunakan index
for data in enumerate(data):
    print(f"Data : {data}")
    
   
# ====== for loop nested list ======
print("\n====== for loop nested list ======") 
peserta0 = ["luffy", 21, "konoha"]
peserta1 = ["zoro", 22, "iwagakure"]
peserta2 = ["naruto", 21, "sunagakure"]

peserta = [peserta0, peserta1, peserta2]

for i in peserta:
    print(f"Nama \t: {i[0]}")
    print(f"Umur \t: {i[1]}")
    print(f"Alamat \t: {i[2]}\n")