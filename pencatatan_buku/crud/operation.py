from database import database 

import time
import random
import string


def random_string(lenth):
    char = string.ascii_uppercase + string.digits
    pk = "".join(random.choice(char) for i in range(lenth))
    
    return pk


# update data
def update_data(no_buku,pk,judul,penulis,thn_terbit,waktu_input):
    DATA = database.TEMPLATE.copy()

    DATA["pk"] = pk
    DATA["judul"] = judul + database.TEMPLATE["judul"][len(judul):]
    DATA["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis):]
    DATA["tahun_terbit"] = thn_terbit
    DATA["waktu_input"] = waktu_input
    
    result = f"{DATA['pk']}, {DATA['judul']}, {DATA['penulis']}, {DATA['tahun_terbit']}, {DATA['waktu_input']}"
    length = len(result)
    try:
        with open(database.DATABASE, 'r+', encoding='utf-8') as data:
            data.seek(length * (no_buku-1))
            data.write(result)
    except Exception as e:
        print(f"Gagal melakukan update: {e}")

# function create database
def create_data():
    
    judul = input("Masukkan judul\t\t: ")
    penulis = input("Masukkan Penulis\t: ")
    thn_terbit = input("Masukkan tahun terbit\t: ")

    DATA = database.TEMPLATE.copy()

    DATA["pk"] = random_string(6)
    DATA["judul"] = judul + database.TEMPLATE["judul"][len(judul):]
    DATA["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis):]
    DATA["tahun_terbit"] = thn_terbit
    DATA["waktu_input"] = time.strftime("%Y-%m-%d | %H-%M-%S%z", time.gmtime())
    
    result = f"{DATA['pk']}, {DATA['judul']}, {DATA['penulis']}, {DATA['tahun_terbit']}, {DATA['waktu_input']}"
    
    try:
        with open(database.DATABASE, 'w', encoding='utf-8') as data:
            data.write(result)
    except: #except
        print("Data gagal tersimpan")
   
   
# Function read data backend
def read(**kwargs):
    try:
        with open(database.DATABASE, 'r') as data:
            content = data.readlines()
            jumlah_buku = len(content)
            
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else: 
                return content
    except Exception as e:
        print(f"Data gagal ditampilkan: {e}")    


def add(judul,penulis,thn_terbit):
    DATA = database.TEMPLATE.copy()
    
    DATA["pk"] = random_string(6)
    DATA["judul"] = judul + database.TEMPLATE["judul"][len(judul):]
    DATA["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis):]
    DATA["tahun_terbit"] = thn_terbit
    DATA["waktu_input"] = time.strftime("%Y-%m-%d | %H-%M-%S%z", time.gmtime())
    
    result = f"{DATA['pk']}, {DATA['judul']}, {DATA['penulis']}, {DATA['tahun_terbit']}, {DATA['waktu_input']}\n"
  
    try:
        with open(database.DATABASE, 'a', encoding='utf-8') as data:
            data.write(result)
    except Exception as e:
        print(f"Data gagal ditambahkan: {e}")
        
        
