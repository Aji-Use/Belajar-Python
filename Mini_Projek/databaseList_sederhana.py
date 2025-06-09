# Lanjuytan dari belajar list
# Dalam program ini saya mengembangkan pembelajaran saya tentang list

# ========= Membuat database buku sederhana ==========

print("\n======= Database Sederhana ========")

list_buku = []

while True:
    print("\n")
    judul = input("Masukkan judul buku\t: ").title()
    penulis = input("Masukkan nama penulis\t: ").title()

    daftar_buku = [judul, penulis]
    list_buku.append(daftar_buku)

    print("======== Tabel List Buku ========")
    for index, buku in enumerate(list_buku):
        print(f"No\t\t: {index+1}\nJudul Buku\t: {buku[0]}\nPenulis\t\t: {buku[1]}")
        print("_"*40)
        
    
    while True:
        next_input = input("Lanjut input buku (y/n):  ").lower()
        
        if next_input in ['y', 'n']:
            break
        print("Masukkan jawaban dengan benar! (y/n)")

        
    if next_input == 'n':
        break 

print("PROGRAM SELESAI")