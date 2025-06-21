# Latihan encapsulasi

class Hero:
    """class hero"""
    # class private variabel 
    _jumlah = 0
    
    def __init__(self, name, health, attack_power, armor):
        self.__name = name
        self.__health_base = health
        self.__power_base = attack_power
        self.__armor_base = armor
        self.__level = 1
        self.__exp = 0
        
        self.__health_max = self.__health_base * self.__level
        self.__power = self.__power_base * self.__level
        self.__armor = self.__armor_base * self.__level
        
        self.__health = self.__health_max
        
        Hero._jumlah += 1
        
    @property
    def info(self):
        """return info hero"""
        return (
            f"Hero: {self.__name} \n"
            f"\tLevel: {self.__level}\n"
            f"\tHealth: {self.__health}/{self.__health_max}\n"
            f"\tPower: {self.__power}\n"
            f"\tArmor: {self.__armor}\n"
            f"\tExp: {self.__exp}"
        )

    @property
    def gain_exp(self):
        """add property"""
    
    @gain_exp.setter
    def gain_exp(self,add_exp):
        self.__exp += add_exp
        
        if self.__exp >= 100:
            print("level up")
            self.__level += 1
            self.__exp -= 100
            
            self.__health_max = self.__health_base * self.__level
            self.__power = self.__power_base * self.__level
            self.__armor = self.__armor_base * self.__level
            
            self.__health = self.__health_max
    
hilda = Hero('hilda', 100, 5, 25)
print(hilda.info)
hilda.gain_exp = 150
print(hilda.info)
        