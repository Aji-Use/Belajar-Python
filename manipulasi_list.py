# Belajar manipulasi list

"""
    1) .insert => menambah data berdasarkan index           EX: name_list.insert(no_index, "name_index")
    2) .append => menambah data diakhir list                EX: name_list.append("name list")
    3) .extend => menggabungkan beberapa data pada list     EX: name_list1.extend(name_list2)
    4) .remove => menghapus data pada list                  EX: name_list.remove("nama_data")
    5) update data => nama_list[no_index] = "nama index"
"""

# indexing 0/-4       1/-3      2/-2      3/-1
data = ["luffy", "zoro", "sanji", "usop"]

print("data zoro (index 1): ", data[1])
print("data zoro (index -3): ", data[-3])



# Manipulasi data list

# ======== Mengetahui panjang data pada list ===========
print("\n==== Mengetahui panjang data pada list ====")
uzumaki = ["naruto", "minato", "mito"]
print(f"Panjang data : {len(uzumaki)}")

# ============ Menambahkan item pada list =============
print("\n==== Menambahkan item pada list ====")

name = ["shanks", "kaido", "lin-lin", "shirohige"]

before = print(f"Data sebelum diupdate : {name}")

# Menmbahkan data berdasar index dengan .insert(index_keBerapa, nama_data)
# EX: name.insert(1, luffy)
name.insert(1, "luffy")
print(f"Data setelah diupdate dengan .insert: {name}")


# Menmbahkan data diakhir list dengan .append(nama_data) 
# EX: name.append("luffy")
name.append("joyboy")
print(f"Data setelah diupdate dengan .append: {name}")


# ========= Menggabungkan data list datu dengan list yang lain =========
# EX: name.extend(data_yangLain)
print("\n==== Menggabungkan list dengan extend()")
yonko = ["shanks", "kurohige", "luffy", "buggy"]
admiral = ["akainu", "aokiji", "borsalino"]

print(f"Data yonko : {yonko}")
print(f"Data admiral : {admiral}")

yonko.extend(admiral)
print(f"Kedua data setelah digabung : {yonko}")


# ========= Menghapus data pada list ==========
print("\n==== Mengahpus data pada list ====")

pirates = ["luffy", "buggy", "bonney", "kid"]
print(f"Data sebelum dihapus: {pirates}")

pirates.remove("buggy") #data harus sesuai,sensitive case
print(f"Data setelah dihapus: {pirates}")

# Menghapus data terakhir dengn pop
pirates.pop()
print(f"Data setelah dihapus dengan pop: {pirates}")



# ========= update data ============
print("\n==== update data list ====")
legend = ["garp", "roger", "gaban", "rayleight"]
print(f"Data sebelum di update: {legend}")

legend[0] = "joyboy"
print(f"Data sesudah di update: {legend}")


