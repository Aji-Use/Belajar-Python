# Belajar continue dan pass

# pass ==> data dumy dan tidak akan melakukan aksi apapun
#continue ==> dengan continue, program dibawahnya tidak akan dieksekusi. Program akan meloncat langsung ke loop


# ======= While dangan logika if
print("While dangan logika if".center(40,"="))
data = 0 

while data < 5:
    data += 1
    
    if data == 3:
        print("Contoh penggunaan if dalam loop")
        
    print(f"Ini dalah data ke-{data}")


# ======= dengan pass =======, pass hanyalah dumy dan tidak ada aksi
print("\nWhile dangan logika if".center(40,"="))
data = 0

while data <= 5:
    data += 1
    
    if data == 3:
        pass
    
    print(f"data ke-{data}")
    
print("End program")


# ======== Contoh penggunaan continue =========
print("\n====Contoh penggunaan continu====")

data = 0

while data < 5:
    data += 1
    print(f"ini adalah data ke-{data}")
    
    if data == 3:
        print("Penggunaan if dalam while ketika data = 3")
        print(f"Uji data ke-3 akan di skip dengan 'continue'")
        continue #dengan continua, program dibawahnya tidak akan dieksekusi. Program akan meloncat langsung ke loop
    
    print(f"Uji data {data}")
    
print("End Program")