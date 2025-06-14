from crud import operation


DATABASE = "database.txt"
TEMPLATE = {
    "pk" : "XXXXXX",
    "judul" : 255*" ",
    "penulis" : 255*" ",
    "tahun_terbit" : "YYYY",
    "waktu_input" : "YYYY-MM-DD"
}


def init_db():
    try:
        with open(DATABASE, "r") as db:
            print("Database tersedia")
            
    except: # pylint: disable=bare-except
        print("Database tidak ada, database sedang dibuat\n")
        print("Database berhasil dibuat")
        
        with open(DATABASE, 'w', encoding="utf-8") as db:
            operation.create_data()