'''
    Jika nama method sama, maka yang akan di eksekusi adalha urutan pertama dari peletakkan inheritance
'''
class A:
    
    def show(self):
        print("Method A")
        
class B:
    
    def show(self):
        print("Method B")
        
class C(A,B): #peletakan inheritance
    
    def show(self):
        print("Method C")
        
class D(B,A): #peletakan inheritance
    
    def show(self):
        print("Method D")
        
class E(B,A): #peletakan inheritance
    
    pass
        
tes = E()
tes.show()

cek = C()
cek.show()

hal = D()
hal.show()