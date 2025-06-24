# Belaar menggunkan class abstrak dan decorator
from abc import ABC, abstractmethod

class Button(ABC):
    
    def __init__(self, set_link):
        self.link = set_link
    
    @abstractmethod
    def click(self):
        pass
    
    # Peletakkan decorator harus urut
    @property
    @abstractmethod
    def link(self):
        pass
    
    
class PushButton(Button):
    
    def click(self):
        print(f"Go to: {self.link}")
        
    @Button.link.setter
    def link(self, input):
        self.__link = input
        
        
    @link.getter
    def link(self):
        return self.__link
        
        
tombol1 = PushButton("www.google.com")
tombol1.click()