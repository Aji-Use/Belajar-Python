# Belajar Operasi Dictionary


"""
    => Membuat variabel constant di python dengan huruf UPPER_CASE 
    => read data dictionary .GET()                  ==> data_dic.get("key")
    => menambahkan/edit data dictionary .UPDATE()   ==> data_dic.update({"key":"value", "key":"value"})
    => menghapus data dictionary DEL                ==> del data_dic["key"] 
"""


data_dic = {
    "pirates" : "shanks",
    "admiral" : "Akainu",
    "yonko" : "shirohige",
    "shicibukai" : "mihawk"
}

# 
LENDICT = len(data_dic) #Uppercase berarti variabel tersebut constant

print(f"Panjang data dictionary = {LENDICT}")


# Mengecek key ada atau tidak
print("\n=======Mengecek key ada atau tidak=======")

KEY = "admiral"
CHECK_KEY = KEY in data_dic

print(f"apakah {KEY} ada didalam data_dic: {CHECK_KEY}")


# ====== Mengakses value (read) data pada dictionary ======
print("\n====== Mengakses value (read) data pada dictionary ======")

# Benar tapi kurang tepat
# Jika key tidak ditemukan maka sistem akan error
print(f"Menampilkan manual value dengan key: {data_dic["pirates"]}") # Mengakses(menampilkan) value dengan key


# Benar dan tepat
# Jika data tidak ada maka tidak akan menampilkan pesan error
# Bisa mengatur pesan jika data tidak ditemukan
print("\n--- data ada pada dic ---")
print(f"Menampilkand data dengan get(): {data_dic.get("pirates")}")

print("\n--- data tidak ada pada dic ---")
print(f"Menampilkan dengan get() jika data tidak ada pada dic: {data_dic.get("monkey")}")

print("\n--- data tidak ada pada dic, memberikan response ke UI ---")
print(f"Menampilkan dengan get() jika data tidak ada pada dic: {data_dic.get("monkey", "Key tidak ditemukan")}")


# =========== Update data pada dictionary ===========
print("\n=========== Update data pada dictionary ===========")


print(f"Sebelum update: {data_dic}")

# ---- MENGEDIT data berdasarkan KEY -----
print("\n---- Mengedit data berdasarkan KEY -----")

UPDATE = data_dic["shicibukai"] = "Moria"
print(f"Data 'Mihawk' diupdate dengan: {UPDATE}")
print(f"Sesudah update: {data_dic}")

# ---- MENAMBAHKAN data ----
print("\n---- Menambahkan data -----")

NEW_DATA = data_dic["lord"] = "usop"
print(f"Data baru: {NEW_DATA}")
print(data_dic)


# ---- Menambahkan dengan UPDATE() ----
# Cara yang lebih fleksibel, dan dapat menambahkan data banyak sekaligus dalam fungsi UPDATE()
print("\n---- Menambahkan dengan UPDATE() ----")

data_dic.update({"god" : "usop"})
print(data_dic)

data_dic.update({"lord" : "rangga"})
print(data_dic)


# ======== Mendelete data pada dictionary ========
print("======== Mendelete data pada dictionary ========")

del data_dic["lord"]
print(data_dic)