# Looping dictionary

data_dic = {
    "makan" : "rendang",
    "minum" : "kopi",
    "buah" : "anggur",
    "sayur" : "tomat",
    "cemilan" : "coklat"
}


# hanya akan menampilkan key
print("\n============ hanya akan menampilkan key ============")
for i in data_dic:
    print(i)
    
    
#  Looping menampilkan key, dengan fungsi KEYS()
print("======== Looping menampilkan value dengan (keys())==========") 

KEYS = data_dic.keys()

for i in KEYS:
    print(i)
    
#  Looping menampilkan value, dengan fungsi VALUES()
print("======== Looping menampilkan value ==========") 

# ---- Cara 1 (dengan get())----
print("---- Cara 1 (dengan get)----")

for i in data_dic:
    print(f"Data: {data_dic.get(i)}")
    

# ---- Cara 2 (dengan value()) ----   
print("\n---- Cara 2 ----")

for i in data_dic.values():
    print(f"Value : {i}")

    
# ---- Cara 3 ----
print("\n---- Cara 3 ----")

NUMBER = 1
for i in data_dic.values():
    print(f"{NUMBER} : {i}")
    NUMBER +=1
    