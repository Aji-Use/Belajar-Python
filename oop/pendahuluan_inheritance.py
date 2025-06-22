# Belajar inheritance python
class Hero:
    
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
# Membuat child class yang mewarisi parent class(Hero)
class HeroMarksman(Hero):
    '''pass'''
    
class HeroMagic(Hero):
    '''pass'''
    
    
# Super class, parent
print('----- Super Class -----')
gatot = Hero('gatot', 5000)
print(gatot.name)
print(gatot.__dict__)

# Inheritance, child
'''
    Child class akan memilii atribut dan method yang sama dengan parent class (Hero)
'''

print('----- Child Class -----')
miya = HeroMarksman('Miya', 2800)
print(miya.name)
print(miya.__dict__)

cyclops = HeroMagic('Cyclops',2900)
print(cyclops.name)
print(cyclops.__dict__)