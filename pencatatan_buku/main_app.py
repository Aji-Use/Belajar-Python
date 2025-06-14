# main App
import database.database as database

from crud import view

print("\nSelamat Datang di Sistem Pencatatan Buku")

if __name__ == "__main__":
    
    while True:

        view.option_console()
        # Header
        print("="*85)
        print(f"{'NO':^7} | {'JUDUL BUKU':^30} | {'NAMA PENULIS':^25} | {'TAHUN TERBIT':^5}")
        print("="*85)
        
        # Data result
        view.read_console()

        # Footer
        print("="*85)
        
        # view.create_console()
        
        break