# main App
import os
import database.database as database
from crud import view

print("\nSelamat Datang di Sistem Pencatatan Buku")
print("="*85)


if __name__ == "__main__": 
    
    while True:
        print("\n")
        print("Silahkan pilih menu di bawah:")
        
        print("1. Create Data")
        print("2. Read Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Exit")
        
        
        while True:
            print("\n")
            option = input("Masukkan Pilihan: ")
            
            if option in ['1','2','3','4','5']:
                break
            print("Masukkan jawaban dengan benar")
            
        match option:
            case '1': view.create_console()
            case '2': 
                print("\n")
                print("="*85)
                print(f"{'NO':^7} | {'JUDUL BUKU':^30} | {'NAMA PENULIS':^25} | {'TAHUN TERBIT':^5}")
                print("="*85)
                view.read_console()
            case '3': view.update_console()
            case '4': pass
            case '5': break
                
        while True:
            print("\n")
            select = input("Apakah anda ingin lanjut (y/n): ").lower()
            
            if select in ['y', 'n']:
                break
            print("Masukkan jawaban dengan benar (y/n)")
            
        if select == 'n':
            break
        
        # Header
        # print("="*85)
        # print(f"{'NO':^7} | {'JUDUL BUKU':^30} | {'NAMA PENULIS':^25} | {'TAHUN TERBIT':^5}")
        # print("="*85)
        
        # # Data result
        # view.read_console()

        # # Footer
        # print("="*85)
        
        # view.create_console()
        
     