# Belajar membuat function dengan almbda dan anonymous funcion

# Function Biasa

print("========== Function Biasa =========")
def pangkat(nilai,pangkat):
    hasil = nilai**pangkat
    
    return hasil

print(pangkat(4,2))


# ========== Lambda Function =========
print("========== Lambda Function =========")

"""
    kuadarat = nama function
    lambda = inisialisasi Lambda Function
    nilai,pangkat = nama Parameter
"""

kuadrat = lambda nilai,pangkat:nilai**pangkat
print(kuadrat(5,3)) 


# ======== Studi Kasus ========
print("======== Studi Kasus ========")

data = [1,2,3,4,5,6,7,8,9,10,11,12]

# Filter data genap
data_genap = list(filter(lambda x:x%2 == 0, data))
print(f"Data angka genap: {data_genap}")

# Filter data genap
data_ganjil = list(filter(lambda x:x%2 != 0, data))
print(f"Data angka ganjil: {data_ganjil}")


# =========== Anonymous Function ==========
print("=========== Anonymous Function ==========")

print("---------- Function Biasa ----------")
def kali(nilai,kali):
    hasil = nilai**kali
    
    return hasil

print(kali(4,2))


print("---------- Anonymous Function ----------")

def kuadratt(n):
    return lambda angka:angka**n

kali2 = kuadratt(2)
print(f"Kuadrat 2 {kali2(6)}")

print(f"Kuadrat 2 {kuadratt(2)(3)}")