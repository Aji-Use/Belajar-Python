# Belajar membuat database sederhana dengan dictionary tamplate
import datetime
import random
import string

# tamplate dictionary
alamat_tamplate = {
    'provinsi' : 'provinsi',
    'kabupaten' : 'kabupaten',
    'kecamatan' : 'kecamatan',
    'desa' : 'desa',
    'rw' : 'rw',
    'rt' : 'rt',
    'jalan' : 'jalan'
}

customer_tamplate = {
    'id' : 'id',
    'nama' : 'nama',
    'tgl_lahir' : datetime.datetime(1111,1,11),
    'email' : 'email',
    'no_telp' : 'no_telp',
    'alamat' : 'alamat',
    'kode_pos' : 'kode_pos',
    'produk' : 'produk'
}

database = {}

alamat = dict.fromkeys(alamat_tamplate.keys())


while True:
    customer = dict.fromkeys(customer_tamplate.keys())
    
    LEN_CHAR = 8
    char = string.ascii_uppercase + string.digits
    id_customer = ''.join(random.choice(char) for i in range(LEN_CHAR))
    
    customer['id'] = id_customer
    customer['nama'] = input("Masukkan nama lengkap \t\t: ").title()
    tahun_lahir = int(input("Masukkan tahun lahir (yyyy) \t: "))
    bulan_lahir = int(input("Masukkan bulan lahir (1-12) \t: "))
    tanggal_lahir = int(input("Masukkan tanggal lahir (1-31) \t: "))
    customer['tgl_lahir'] = datetime.datetime(tahun_lahir,bulan_lahir,tanggal_lahir)
    customer['email'] = input("Masukkan email \t\t\t: ")
    customer['no_telp'] = input("Masukkan nomor telepon \t\t: ")
    customer['alamat'] = input("Masukkan alamat \t\t: ")
    customer['kode_pos'] = input("Masukkan kode pos \t\t: ")
    customer['produk'] = input("Masukkan nama produk \t\t: ")

    database.update({id_customer : customer})
    
    print("\n")
    print(f"{'ID':<9} {'NAMA':<15} {'TGL_LAHIR':<10} {'EMAIL':<15} {'NO_TELP':<15} {'ALAMAT':<20} {'KODE_POS':<8} {'PRODUK':<10}")
    print("="*120)
    for key, value in database.items():
        key = key
        
        id = database[key]['id']
        nama = database[key]['nama']
        tgl_lahir = database[key]['tgl_lahir'].strftime("%x")
        email = database[key]['email']
        no_telp = database[key]['no_telp']
        alamat = database[key]['alamat']
        kode_pos = database[key]['kode_pos']
        produk = database[key]['produk']
        
        print(f"{id:<9} {nama:<15} {tgl_lahir:<10} {email:<15} {no_telp:<15} {alamat:<20} {kode_pos:<8} {produk:<10}")
        print("="*120)
    while True:
        next_step = input("Apakah anda ingin lanjut (y/n)? ")
        
        if next_step in ["y", "n"]:
            break
        print("Silahkan masukkan jawaban dengan benar!")
        
    if next_step == "n":
        break
    
print("PROGRAM SELESAI")