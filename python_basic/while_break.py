# Belajar while loopdengan break

# break, looping akan berhenti ketika memenuhi kondisi

# Penggunaan break dalam while loop
print("=======Penggunaan break dalam while loop=======")
data = 0

while data < 5:
    data += 1
    print(f"data ke - {data}")
    
    if data == 3:
        print ("data ke-3, sistem berhenti")
        break #program akan berhenti ketika memenuhi kondisi
    
    print(f"uji data ke- {data}")
    
print("selesai")



# ========== Contoh program 1

print("======Contoh Penggunaan while true dan break======")
username = "admin"
password = "123456"

while True:
    usr = input("Masukkan username : ")
    pwd = input("Masukkan password : ")
    
    if usr == username and pwd == password:
        print("Username dan password valid")
        break
        
    else:
        print("Username atau password salah, silahkan masukkan lagi")
        print("="*40)
  
print(f"Terimakasih {usr} sudah berhasil login")      



# ========== Contoh program 2
print("======Contoh program======")

input_user = float(input("Masukkan jumlah looping : "))

cut = input_user // 2
data = 0

while True:
    data += 1
    print(f"Data ke-{data}")
    
    if data == cut:
        print("Program berhenti")
        break
    
    print(f"Uji data ke-{data}")
    
print("Program Selesai")