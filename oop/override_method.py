'''
    Override
    method dengan nama yang sama di sub class akan melakukan override(menimpa) method di super class
'''

class Hero:
    '''Super Class'''
    
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def info(self):
        '''Hero Info'''
        print("Info dengan super class")
        print(f"Name: {self.name} \n\tHealth: {self.health}") 
        
class HeroMarksman(Hero):
    '''sublacc HeroMarksman'''
    def __init__(self, name):
        # inheritance
        super().__init__(name, 2700)
        
    # override
    def info(self):
        print("Info dengan override, subclass")
        print(f"Name: {self.name} \n\tHealth: {self.health}")
        
class HeroMagic(Hero):
    '''sublacc HeroMagic'''
    def __init__(self, name):
        # inheritance
        super().__init__(name, 3000)
        
miya = HeroMarksman('miya')
zask = HeroMagic('zask')

miya.info()
zask.info()