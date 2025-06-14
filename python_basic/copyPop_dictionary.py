# Belajar copy dan pop dictionary

"""
    1. melakukan copy data: .copy()     
        EX: data_copy = data.copy()
    2. mengambil/mentransfer data dictionary berdasar (key): .pop()     
        EX: data = data_dic.pop()
    3. Mengambil/mentransfer data terakhir dictionary (key/value): .popitems()
        EX: last_data = data.popitems()
"""


data_dic = {
    "makan" : "rendang",
    "minum" : "kopi",
    "buah" : "anggur",
    "sayur" : "tomat",
    "cemilan" : "coklat"
}


# ========= Copy Data =========
print("\n========= Copy Data =========")
data_copy = data_dic

print(f"Data asli: {data_dic}")
print(f"Data Copy: {data_copy}")

print("\n---- Update data asli, akan merubah data copy ----") # hal yang tidak diinginkan
data_dic["sayur"] = "wortel"

print(f"Data asli: {data_dic}")
print(f"Data Copy: {data_copy}")

# ---- SOLUSI ----
data_dic = {
    "makan" : "rendang",
    "minum" : "kopi",
    "buah" : "anggur",
    "sayur" : "tomat",
    "cemilan" : "coklat"
}

print("\n--- Solusi ---")

copy_data = data_dic.copy() # merubah data asli, tidak akan merubah data copy

print(f"Data asli: {data_dic}")
print(f"Data Copy: {copy_data}")

print("\n---- Update data asli, akan merubah data copy ----") # hal yang tidak diinginkan
data_dic["sayur"] = "wortel"

print(f"Data asli: {data_dic}")
print(f"Data Copy: {copy_data}")


# =========== Transfer data, atau mengambil data dengan pop dan pop item ============
print("\n=========== Transfer data, atau mengambil data dengan pop dan pop item ============")

# ---- Dengan POP ----
# Mengambil data berdasarkan key
print("\n---- Dengan POP () ----")

print(f"Data asli\t\t\t: {data_dic}")

data1 = data_dic.pop("makan")

print(f"Data yang diambil\t\t: {data1}")
print(f"Data asli setelah diambil\t: {data_dic}") # data yang diambil akan hilang dari dict

# ---- Dengan POPITEMS ----
# Mengambil data terakhir
print("\n---- Dengan POPITEM() ----")

print(f"Data asli\t\t\t: {data_dic}")

data_terakhir = data_dic.popitem()

print(f"Data yang diambil\t\t: {data_terakhir}")
print(f"Data asli setelah diambil\t: {data_dic}") # data yang diambil akan hilang dari dict
