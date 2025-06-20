class Hero:
    
    # class variabel
    jumlah = 0
        
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
        # variabel instance private
        '''
            isi variabel tidak bisa dirubah
        '''
        self.__private = "private"
        
        # variabel protected
        '''
            isi variabel bisa dirubah, tetapi menandakan jangan mengubah isi variabel
        '''
        self._protected = "protected"
        
           
wowo = Hero('wowo', 100)

print(wowo.__dict__) 

# protected
print(wowo._protected)
wowo._protected = "testing"
print(wowo._protected)