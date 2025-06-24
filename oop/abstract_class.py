# Menggunakan library abstrak class
# abs = abstrak base class
from abc import ABC,abstractmethod

class Button(ABC):
    
    # method click akan dipaksa untuk dijalankan di class yang melakukan inheritance
    # Jika tidak dijalankan maka akan error
    @abstractmethod
    def click(self):
        pass
    
class PushButton(Button):
    
    def click(self):
        print("Push Button Click")
    
class RadioButton(Button):
    
    def click(self):
        print("Push Radio Button Click")
    
    
tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.click()
tombol2.click()
