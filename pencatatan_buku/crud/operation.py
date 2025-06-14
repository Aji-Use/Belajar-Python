from database import database 
from . import view
import time
import random
import string


def random_string(lenth):
    char = string.ascii_uppercase + string.digits
    pk = "".join(random.choice(char) for i in range(lenth))
    
    return pk

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
def read():
    try:
        with open(database.DATABASE, 'r') as data:
            file = data.readlines()
            return file
    except:
        print("Data gagal ditampilkan")
        


def add(judul,penulis,thn_terbit):
    DATA = database.TEMPLATE.copy()
    
    DATA["pk"] = random_string(6)
    DATA["judul"] = judul + database.TEMPLATE["judul"][len(judul):]
    DATA["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis):]
    DATA["tahun_terbit"] = thn_terbit
    DATA["waktu_input"] = time.strftime("%Y-%m-%d | %H-%M-%S%z", time.gmtime())
    
    result = f"{DATA['pk']}, {DATA['judul']}, {DATA['penulis']}, {DATA['tahun_terbit']}, {DATA['waktu_input']}\n"
    print(result)
    try:
        with open(database.DATABASE, 'a', encoding='utf-8') as data:
            data.write(result)
            
    except Exception as e:
        print(f"Data gagal ditambahkan: {e}")
        
        
