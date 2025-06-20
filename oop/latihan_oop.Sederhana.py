class Hero:
    
    def __init__(self,name,health,power,armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        
    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.power)
        
    def diserang(self, lawan, power_lawan):
        print(self.name + ' diserang ' + lawan.name)
        power = power_lawan / self.armor
        sisa_healt = self.health - power
        
        print('Power terasa: ', power)
        print('Sisa Health: ', sisa_healt)
        
iran = Hero('Iran', 5000, 2000, 1000)
israel = Hero('Israel', 500, 200, 100)

iran.serang(israel)
print('\n')
israel.serang(iran)