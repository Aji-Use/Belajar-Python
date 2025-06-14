from . import operation


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

    judul = input("Judul\t\t: ")
    penulis = input("Penulis\t\t: ")
    thn_terbit = input("Tahun Terbit\t: ")
    
    operation.add(judul,penulis,thn_terbit)
    
def option_console():
    print("Silahkan pilih menu di bawah ini\n")
    
    print("1. Create Data")
    print("2. Read Data")
    
    select = input("Pilih menu: ")
    
    match select:
        case "1":
            create_console()
        case "2":
            read_console()
        case _:
            print("Masukkan pilihan dengan benar")
    

    
    

    