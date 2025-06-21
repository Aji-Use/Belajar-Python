class Hero:
    
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "Name: {} : \n\thealth: {}".format(self.name, self.__health)
        
    
    # decorator
    '''
        dengan @property, method yang dibuat akan seolah menjadi atrribut(variabel)
        dengan ini, pengguna bisa merubah data
    '''
    @property
    def info(self):
        return "Name: {} : \n\thealth: {}".format(self.name, self.__health)
    
    # ========== Membuat getter pada python
    # Sebelum membuat getter dan setter, harus didefinisikan dahaulu menjadi properti
    @property
    def armor(self):
        pass
    
    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, inputArmor):
        self.__armor = inputArmor
        
    # deleter
    @armor.deleter
    def armor(self):
        print('armor di delete')
        self.__armor = None

# Meerubah info dari varibael menjadi properti 
badang = Hero('badang', 4200, 30)
print(badang.__dict__)
print(badang.info)

badang.name = "gatot"
print(badang.__dict__)
print(badang.info)
      
      
# Menggunakan getter dan setter
# Armor dari 30 dirubah menjadi 100
print(badang.armor)
badang.armor = 100
print(badang.armor)
print(badang.__dict__)

print('Delete Armor dengan DELETER')
del badang.armor
print(badang.__dict__)