# Belajar membuat function dengan **kwargs

"""
    1. **kwargs => bersifat dictionary {}
    2. bisa digabungkan dengan *args => bersifat tuple ()
"""

# Function biasa
print("======= Function biasa ========")
def sapa(nama,umur,tinggi):
    print(f"Halo {nama.title()} dengan umur {umur} dan tinggi {tinggi} cm")
    
sapa("luffy",21,211)


# ============= Function dengan **kwargs ===============
print("\n======= Function dengan **kwargs ========")
def hallo(**kwargs):
    print(kwargs)
    
    nama = kwargs['nama']
    umur = kwargs['umur']
    tinggi = kwargs['tinggi']
    
    print(f"Halo {nama.title()} dengan umur {umur} dan tinggi badan {tinggi}")
    
hallo(nama="andi",umur=21,tinggi=222) #cara memasukkan nilai ke dalam parameter kwargs, karena bersifat dictionary


# =========== Studi Kasus ============
print("\n======= Studi Kasus ========")
def operasi(*args, **kwargs):
    
    if kwargs["option"] == "kali":
        output = 1
        
        for i in args:
            output *= i
            print(output)
            
    elif kwargs["option"] == "tambah":
        output = 0
        
        for i in args:
            output += i
            print(output)
    else:
        print("Tidak ada operasi")
    
operasi(1,2,3,4, option="tambah")
