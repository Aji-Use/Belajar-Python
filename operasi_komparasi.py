# Operasi Komparasi

# Operasi Komparasi dengan >, <, <=, >=, !=, ==
a = 5
b = 7

# Komparasi dengan ">"
hasil = a > b
print('a =', a, '\nb =', b)
print('a > b =', hasil)

print('=' * 20) 

# Komparasi dengan "<"
hasil = a < b
print('a =', a, '\nb =', b)
print('a < b =', hasil)

print('=' * 20) 

# Komparasi dengan ">="
hasil = a >= b
print('a =', a, '\nb =', b)
print('a >= b =', hasil)

print('=' * 20) 

# Komparasi dengan ">="
hasil = a <= b
print('a =', a, '\nb =', b)
print('a <= b =', hasil)

print('=' * 20) 

# Komparasi dengan ">="
hasil = a != b
print('a =', a, '\nb =', b)
print('a != b =', hasil)

print('=' * 20) 

# Komparasi dengan ">="
hasil = a == 7
print('a =', a, '\n 7')
print('a == 7 =', hasil)

print('='*10, 'OPERASI KOMPARASI OBJEK IDENTITY', '='*10 )

# Operasi Komparasi [Objek Identity]-> (ex: 0x7ff9d7030a38) dengan "is"
# Objek Identity yang dimaksud adalah nilai dariVARIABEL

# Komparasi dengan is TIDAK bisa dilakukan jika menggunakan nilai Object dengan Literal
# contoh OI dengan Literal, a=5, a is 5

# Komparasi dengan is hanya bisa dengan sesama OI
# contoh, a=5 b=5, a is b

# contoh
x = 5
y = 5
hasil = x is y
print('Nilai x =', x, 'Object Identity =', hex(id(x))) # mengetahui Object Identity dengan hex()
print('Nilai y =', y, 'Object Identity =', hex(id(y)))
print("hasil komparasi =", hasil)

