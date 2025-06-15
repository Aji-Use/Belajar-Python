from . import operation



def update_console():
    read_console()
    while True:
        print("Silahkan masukkkan nomor buku yang ingin di update: ")
        no_buku = int(input("Masukkan nomor buku: "))
        data_buku = operation.read(index=no_buku)
        
        if data_buku:
            break
        else:
            print("Nomor yang anda masukkan tidak ada")
    
    data_break = data_buku.split(",")
    
    pk = data_break[0]
    judul = data_break[1]
    penulis = data_break[2]
    thn_terbit = data_break[3]
    waktu_input = data_break[4][:-1]
    
    while True:
        print("Silahkan pilih data yang  ingin dirubah:")
        print(f"1. Judul \t\t: {judul:.40}")
        print(f"2. Penulis \t\t: {penulis:.40}")
        print(f"3. Tahun Terbit \t: {thn_terbit}")
        
        while True:
            option = input("Pilih data: ")
            
            match option:
                case '1': judul = input("Masukkan judul baru: ").title()
                case '2': penulis = input("Masukkan penulis baru: ").title()
                case '3': thn_terbit = input("Masukkan tahun terbit baru: ")
                case _:
                    print("Nomor yang anda masukkan tidak cocok")
                    
            
            select = input("Apakah ingin lanjut mengedit data (y/n): ").lower()
            while True:
                
                if select in ['y','n']:
                    operation.update_data(no_buku,pk,judul,penulis,thn_terbit,waktu_input)
                    read_console()
                    break
                print("Masukkan jawaban dengan benar")

            
            if select == 'n':
                break

        break

    
def read_console():
    data1 = operation.read()
    
    for index,value in enumerate(data1):
            data = value.split(",")
            
            pk = data[0]
            judul = data[1]
            penulis = data[2]
            thn_terbit = data[3]
            wkt_input = data[4]
            
            print(f"{index+1:^7} | {judul:.30} | {penulis:.25} | {thn_terbit:5}")

# create console

def create_console():
        
    print("\n")
    print("Silahkan tambahkan data buku")

    judul = input("Judul\t\t: ").title()
    penulis = input("Penulis\t\t: ").title()
    thn_terbit = input("Tahun Terbit\t: ")
    
    operation.add(judul,penulis,thn_terbit)
    


    