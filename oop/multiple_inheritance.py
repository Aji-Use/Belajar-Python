class Team:
    
    def set_team(self, team):
        self.team = team
        print(self.team)
        
class Tipe:
    
    def set_tipe(self, tipe):
        self.tipe = tipe
        print(self.tipe)
        
class Hero(Team,Tipe):
    
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
layla = Hero('layla', 1000)

layla.set_team('Blue Team')

layla.set_tipe('Marksman')