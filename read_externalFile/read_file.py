# Belajar melakukan read external file

"""
    dalam latihan ini, belajar membuat
    => membuka file
    => membaca file
    => menulis file
    => melihat status file bisa terbaca atau tidak
    => menutup file
    
    file yang telah buka harus tertutup kembali diakhir program
"""

# =========== Membaca File ============
print("=========== Membaca File ============")

read_file = open("file.txt", mode='r')


# Baca semua baris isi dari file, output berbentuk list
print("\n--------Baca semua baris isi dari file--------")
print(f"Membaca semua baris isi file: \n{read_file.readlines()}")

# Cek Status file bisa dibaca atau tidak
print("--------Cek Status file bisa dibaca atau tidak--------")
print(f"Apakah file bisa dibaca: {read_file.readable()}")

# Baca seluruh baris isi file
print("\n--------Baca seluruh baris isi file--------")
print(f"Ini adalah isi dari file 'file.txt': \n{read_file.read()}")

# Baca satu baris isi dari file
print("\n--------Baca satu baris isi dari file--------")
print(f"Ini adalah isi dari baris pertama file: {read_file.readline()}")


# =========== Menulis File ============
print("\n=========== Menulis File ============")

write_file = open("file.txt", mode='w')

# Cek Status file bisa ditulis atau tidak
print("--------------- Cek Status file bisa ditulis atau tidak--------------")
print(f"Apakah file bisa ditulis: {write_file.writable()}")

# Menulis file
# isi file sebelumnya akan hilang
# print("--------Menulis File--------")
# print(f"Menulis file: {write_file.write()}")


# ========== Menutup File Secara Manual ===========
# Manual dan TIDAK EFEKTIF
print(f"Apakah read_file sudah ditutup: {read_file.closed}")
print(f"Apakah write_file sudah ditutup: {write_file.closed}")

# tutup file
read_file.close()
write_file.close()

print(f"Apakah read_file sudah ditutup: {read_file.closed}")
print(f"Apakah write_file sudah ditutup: {write_file.closed}")


# Cara tepat menutup file adalah dengan perintah WITH
# === Contoh dengan with ====

# Dengan cara ini file akan MEMBUKA DAN MENUTUP OTOMATIS
with open("file1.txt", "r") as read_file:
    # Reset pointer ke awal (jika perlu)
    lines = read_file.readlines()
    print(f"Membaca semua baris isi file: \n{lines}")

