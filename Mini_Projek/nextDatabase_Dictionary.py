# Mengembangkan projek sebelumnya (database_dictionary)
# Membuat input user, dan menyimpnnya dalam dictionary

import datetime


database ={}

while True:
    name = input("Masukkan nama anggota\t\t: ").title()
    id = input("Masukkan id anggota\t\t: ").upper()
    address = input("Masukkan alamat tugas\t\t: ")
    time_born =input("Masukkan waktu lahir YYYY-MM-DD\t: ")
    
    born = datetime.datetime.strptime(time_born, "%Y-%m-%d")
    
    tbl_user = {
        'id' : id,
        'name' : name,
        'address' : address,
        'born' : born
    }
    
    database.update({id : tbl_user})
    
     # Dumpa data
    print("\n")
    print(f"{'ID':<8} {'NAME':<20} {'ADDRESS':<20} {'BORN':<10}")
    print("="*60)
    
    for key,value in database.items():
        ID = value['id']
        NAME = value['name']
        ADDRESS = value['address']
        BORN = value['born'].strftime("%Y-%m-%d")
        print(f"{ID:<8}{NAME:<20}{ADDRESS:<20}{BORN:<10}")
         
    print("="*60)
    
    # error handling next program
    while True:
        choise = input("Ingin melanjutkan registrasi (y/n): ").lower()
        
        if choise in ['y', 'n']:
            break
        print("Masukkan jawaban dengan benar!")
        
    if choise == 'n':
        break
    
print("PROGRAM SELESAI") 