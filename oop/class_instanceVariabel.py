# Belajar memahami __init__ pada class python
"""
    __init__ merupakan program yang pertama kali akan dijalankan
    __init__ akan melakukan inisialisasi ke object atau variabel
    Cara akses variabel di class = nameClass.variabel (Hero.jumlah)
"""
# membuat class
class Hero: #/template
    # class variabel
    jumlah =0
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        
        Hero.jumlah += 1
        print("Membuat hero dengan nama", inputName)  
             
             
# variabel akan di inisialisasi dengan fungsi __init__
hero1 = Hero("sniper", 100, 70, 21)
print(Hero.jumlah)
hero2 = Hero("assassin", 100, 100, 10)
print(Hero.jumlah)
hero3 = Hero("tank", 500, 40, 40)
print(Hero.jumlah)

    
    