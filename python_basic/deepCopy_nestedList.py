# Belajar deep copy nested list
data0 = [1,2,3]
data1 = [4,5,6]

data_group = [data0,data1]

print(f"Data0 : {data0}")
print(f"Data1 : {data1}")
print(f"Data group : {data_group}")

# Merubah data

# ========= Data tidak akan berubah jika hanya dengan copy =======
print("\n========= Data tidak akan berubah jika hanya dengan copy =======")

data_group[0][1] = 6 #data yang dirubah
data_group_copy = data_group.copy() #data ikut beruah meski sudah menggunakan copy

print(f"Data Group Copy : {data_group}")
print(f"Data Group Copy : {data_group_copy}")

print("--- KARENA DATA MEMBER GROUP MASIH MEMILIKI ADDRESS YANG SAMA ---")

print(f"\n-- Address list group --")
print(f"Address Data Group asli : {hex(id(data_group))}")
print(f"Address Data Group copy : {hex(id(data_group_copy))}") #yang tercopy hanya list_groupnya,membernya tidak

print(f"\n-- Address Member list ke 1 (index 0) --")
print(f"Address Member Data Group Asli : {hex(id(data_group[0]))}")
print(f"Address Member Data Group Copy : {hex(id(data_group_copy[0]))}")


# ======= Cara melakukan copy nested list yang benar (deep copy) =======
print("\n======= Cara melakukan copy nested list yang benar (deep copy) =======")

from copy import deepcopy

data_group = [data0,data1]
data_group_deepcopy = deepcopy(data_group) #deep copy

print(f"\n-- Address list group --")
print(f"Address Data Group asli : {hex(id(data_group))}")
print(f"Address Data Group copy : {hex(id(data_group_deepcopy))}") 

print(f"\n-- Address Member list ke 1 (index 0) --") #Seluruh data telah tercopy dengan address yang berbeda 
print(f"Address Member Data Group Asli : {hex(id(data_group[0]))}")
print(f"Address Member Data Group Copy : {hex(id(data_group_deepcopy[0]))}")

# ---------- Merubah Data -----------
print(f"\n-- Data dapat dirubah --")
print(f"\n-- Merubah Data --")

data_group_deepcopy[0][2] = 200 #merubah data pada var (data0, index ke-2)

print(f"Data 0 \t\t: {data0}")
print(f"Data 1 \t\t: {data1}")

print(f"Data group \t\t: {data_group}")
print(f"Data Group Deep Copy \t: {data_group_deepcopy}") #data telah terganti