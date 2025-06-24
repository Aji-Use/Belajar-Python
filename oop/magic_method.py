class Mangga:
    
    # Fungsi yang pertama kali akan dijalanka
    def __init__(self, name, jumlah):
        self.name = name
        self.jumlah = jumlah
        
    # Untuk mengatur output default (Biasanya digunakan untuk debug)
    def __repr__(self):
        return f"Mangga yang dibeli: {self.name} dengan jumlah: {self.jumlah}"
    
    # Untuk mengatur output default (Biasanya digunakan ketika sudah final)
    def __str__(self):
        return f"Mangga yang dibeli: {self.name} dengan jumlah: {self.jumlah}"
    
    # Magic method untuk operasi penjumlahan objek
    def __add__(self, objek):
        return self.jumlah + objek.jumlah
    
    # Mengatur output fungsi dict
    @property
    def __dict__(self):
        return "Objek ini mempunyai nama dan jumlah"
    
    
belanja1 = Mangga('arumanis', 10)
belanja2 = Mangga('arumanis', 25)
print(belanja1)
print(belanja2)

print(belanja1 + belanja2)

print(belanja1.__dict__)