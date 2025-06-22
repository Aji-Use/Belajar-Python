class Hero:
    '''Super Class Hero'''
    
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor
  
    def info(self):
        '''Show Info Hero'''
        print(f"Nama: {self.name}, Health: {self.health}, Armor: {self.armor}")
        
class HeroMarksman(Hero):
    '''Define Hero Marksman, default attribut'''
    def __init__(self, name):
        super().__init__(name, 2800, 15)
        super().info()
    
class HeroMagic(Hero):
    '''Define Hero Magic, default attribut'''
    def __init__(self, name):
        super().__init__(name, 3100, 20)  
        super().info()  
        

layla = HeroMarksman('layla')
zask = HeroMagic('zask')