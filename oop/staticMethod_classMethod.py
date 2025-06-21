# Belajar membuat static method
'''
    Tidak harus dengan self, bisa juga diganti dengan yang lain
    EX: 
        def getName(self) => def getName(cls)
'''

class Hero:
    
    # class rivate variabel
    __jumlah = 0
    
    def __init__(self,name):
        self.__name = name
        
        Hero.__jumlah += 1
        
    # ---------Membuat geter untuk mengambil nilai
    # Methodini hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah
    
    # Tidak berlaku untuk objek, BERLAKU untuk Class
    def getJumlah1():
        return Hero.__jumlah

    # Gunakan Static Method (decorator) untuk dapat digunakan pada class dan objek
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
        
    # Gunakan Class Method (decotator) untuk dapat digunakan pada class dan objek
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
    
saskeh = Hero('saskeh')
print(saskeh.__dict__)
print(saskeh.getJumlah())
ino = Hero('ino')
print(Hero.getJumlah1())
# penggunaan static method
print(saskeh.getJumlah2())
king = Hero('king')
print(Hero.getJumlah2())
print(king.getJumlah2())
temari = Hero('temari')
print(Hero.getJumlah3())
print(temari.getJumlah3())