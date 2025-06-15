# Belajar Write External File
"""
    Mode:
        w = write (untuk membuat file yang belum ada)
        a = append (untuk menambahkan baris data)
"""


# =========== Menulis File ============
print("\n=========== Menulis File ============")

# Dengan WITH otomatis akan membuka dan menutup file
# Membuat file yang sebelumnya belum ada
with open("file.txt", mode='w', encoding="utf-8") as file: #harus menggunakan encoding
    file.write("Jhon Doe") #Meunulis file dengan data "Jhon Doe"

# Jika menulis perintah ini lagi, tidak aka nmenambah baris data MELAINKAN akan menulisulang
with open("file.txt", mode='w', encoding="utf-8") as file: #harus menggunakan encoding
    file.write("Ichi bosss") #Meunulis file dengan data "Jhon Doe"
    
    
    
# ========= Bagaimana caranya menambahkan data ============

with open("file_2.txt", 'w', encoding="utf-8") as file2:
    file2.write("Ini adalah file yang dibuat\n")

# Menambahkand data file dengan mode 'a' (append)
with open("file_2.txt", 'a', encoding="utf-8") as file2:
    file2.write("Ini adalah data ke 2 yang ditambahkan pada file_2.txt\n")

# Menambahkand data file dengan mode 'a' (append)
with open("file_2.txt", 'a', encoding="utf-8") as file2:
    file2.write("Ini adalah data ke 3 yang ditambahkan pada file_2.txt")




