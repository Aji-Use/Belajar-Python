# Belajar memahami __init__ pada class python

# membuat class
class Hero: #template
    
    """
        __init__ merupakan program yang pertama kali akan dijalankan
        __init__ akan melakukan inisialisasi ke object atau variabel
        self, menginisialisasi variabel sebagai objeknya
    """
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        
# variabel akan di inisialisasi dengan fungsi __init__
hero1 = Hero("sniper", 100, 70, 21)
hero2 = Hero("assassin", 100, 100, 10)
hero3 = Hero("tank", 500, 40, 40)

# mengambil data sesuai dengan atribut
print(hero1.name)
print(hero2.power)
print(hero3.armor)

# mengambil seluruh data dalam bentuk dict
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__) 
    
    