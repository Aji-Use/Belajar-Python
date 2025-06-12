# Belajar args dalam pembuatan function

'''
    Bagaimana jika memasukkan banyak nilai parameter tanpa membuat banyak parameter (Dinamicx Parameter)
    Menggunkan => *args
    data (args) berbentuk tuple, dan bisa digunakan untuk iterasi
'''

# manual function dengan banyak parameter (parameter static)
print("======== manual function dengan banyak parameter (parameter static) =======")

def fungsi(nama,umur,tinggi): #parameter static, hanya dapat memuat beebrapa parameter yang telah ditentukan
    print(f"halo {nama.title()} dengan umur {umur} dan tinggi badan {tinggi}")
    
fungsi("asek",21,121)


# ===========================================================
# function dengan banyak parameter (parameter dinamis) otomatis bertambah sesuai nilai yang diinputkan

print("\n======== function dengan banyak parameter (parameter dinamis) otomatis bertambah sesuai nilai yang diinputkan =======")

def user(*args): #Parameter dinamis dengan *args, akan otomatis bertambah sesuai banyaknya nilai yang dimasukkan user

    nama =  args[0] #contoh pemanggilan
    umur = args[1] #args, berbentuk tuple
    tinggi = args[2]
    
    print(f"Halo {nama} dengan umur {umur} dan tinggi badan {tinggi}")
    
user("umar",21,190)


# iterasi dengan args tipenya adalah tuple
def customer(*cust):
    for i in cust:
        print(i)
    
customer(1,2,3,4,5)


