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
        
    # function / method (tanpa parameter dan return)
    def siapa(self):
        print("namaku adalah " + self.name)
        
    # function / method (dengan parameter tanpa return)
    def healtUp(self, up):
        self.health += up
        
    # function / method (tanpa parameter dengan return)
    def getHealth(self):
        return self.health
        
    
# variabel akan di inisialisasi dengan fungsi __init__
hero1 = Hero("sniper", 100, 70, 21)
hero2 = Hero("assassin", 100, 100, 10)
hero3 = Hero("tank", 500, 40, 40)


# akses method
hero1.siapa()

hero2.healtUp(30)
print(hero2.health)
print(hero3.getHealth())
    