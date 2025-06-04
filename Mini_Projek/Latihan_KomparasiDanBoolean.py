# Latihan Operasi Komparasi dan Boolean

# +++++++++3----------10++++++++++
# buat program dengan komparasi, input kurang dari 3 atau lebih dari 10
# Contoh dengan komparasi OR
inputUser = float(input("Masukkan angka kurang dari 3 atau lebih dari 10 = "))

# ++++++++3-------
resultA = inputUser < 3
print('Kurang dari 3 =', resultA)

# --------10+++++++++
resultB = inputUser >  10
print('lebih dari 10 =', resultB)

hasil = resultA or resultB
print('Angka yang anda masukkan =', hasil)




# ===================== Contoh dengan komparasi AND =========================
print('='*40)
# -------3+++++++10--------
# ambil nilai antara 3 sampai 10, jika benar maka Trua
inputUser = float(input("Masukkan angka lebih dari 3 dan kurang dari 10 ="))

# --------3+++++++
lebihDari = inputUser > 3
print("Lebih dari 3=", lebihDari)

# +++++++10---------
kurangDari = inputUser < 10
print("Kurang dari 10 =", kurangDari)

hasil = lebihDari and kurangDari

print("Nilai yang anda masukkan =", hasil)



