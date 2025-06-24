class A:
    
    def show(self):
        print("Print A")
        
class B(A):
    
    def show(self):
        print("Print B")
        
class C(A):
    
    def show(self):
        print("Print C")
        
class D(B,C):
    pass


# eksekusi akan dimulai sesuai urutan (D,B,C,A)
objek = D()
objek.show()
help(objek)