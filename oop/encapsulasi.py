# Belajar encapsulasi
'''
    ->Membuat semua variabel menjadi private, dengan tujuan untuk melindungi 
    isi agar tidak berubah saat dijalankan.
    ->Membuat fungsi Getter untuk mengambil nilai variabel
    ->Membuat Setter untuk mengubah isi dari variabel
'''

class Hero:
    
    def __init__(self,name,healt,attackPower):
        self.__name = name
        self.__health = healt
        self.__attPower = attackPower
        
    # Membuat fungsi Geter
    def geterName(self):
        return self.__name
    
    def geterHealth(self):
        return self.__health
    
    
    # Membuat fungsi setter untuk merubah isi variabel
    def diserang(self,power):
        self.__health -= power
        
    
# Awal Game
kaguya = Hero('kaguya',100,90)

# Game berjalan
print(kaguya.__dict__)

# ------- Mengubah nilai variabel seperti dibawah tidak bisa dilakukan
# kaguya.__health = 1000 #Tidak boleh dilakukan
# print(kaguya.__dict__) #health tidak berubah, malah menambah variabel baru


# -------- Cara yang BENAR menggunakan fungsi geter

# print(kaguya.__name) => tidak bisa dilakukan untuk mengambil nilai
print(kaguya.geterName()) #Bisa dilakukan untuk mengambil nilai
print(kaguya.geterHealth())
kaguya.diserang(10) #Menggunakan seter untuk merubah nilai variabel saat dijalankan
print(kaguya.geterHealth())