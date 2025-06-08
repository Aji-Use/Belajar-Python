# Belajar membuat list


# List number
list_number = [1,2,3,4,5,6]
print(list_number)

# List string
list_string = ["aku", "kamu", "dia", "saya", "kami"]
print(list_string)

# List boolean
list_bool = [True, False, False, True, True]
print(list_bool)


# list campuran
list_mix = ["aku", 1, True, "dia"]
print(list_mix)


# list data range
print("==== list dengan range ====")
data_range = range(0, 10)
data_list = list(data_range)
print(data_list)
print("==== list dengan range increment 2 ====")
data_range = range(0, 10, 2) #membuat range 0 - 10, dengan increment 2
data_list = list(data_range)
print(data_list)


# list dengan for loop
print("\n====Membuat list dengan for loop")

list_forLoop = [i for i in range(0,10)]
print("Contoh 1", list_forLoop)

list_forLoop1 = [i for i in range (0,20, 3)]
print("Contoh 2: ", list_forLoop1)

list_forLoop2 = [i**2 for i in range (0,20)]
print("Contoh 3 (dengan pangkat): ", list_forLoop2)


# list dengan for loop dan if
print("\n====List dengan for loop dan if====")
list_forIf = [i for i in range(0,20) if i%2 == 0]
print("Contoh 1 (List Genap): ", list_forIf)

list_forIf = [i for i in range(0,20) if i%2 != 0]
print("Contoh 1 (List Ganjil): ", list_forIf)