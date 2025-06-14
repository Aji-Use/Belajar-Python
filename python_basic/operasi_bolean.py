# Operasi Logika dengan Boolean "or, and, not, xor"

# =============== Operasi NOT ==================
print('='* 5, 'Operasi dengan NOT', '='*5)
a = False
hasil = not a
print('a =', a)
print('-'*10, 'NOT')
print('a =', hasil)

#==================== Operasi OR ===============
print('='* 5, 'Operasi dengan OR', '='*5)
a = False
b = True
hasil = a or b
print(a, 'OR', b, ' =', hasil)

a = False
b = False
hasil = a or b
print(a, 'OR', b, '=', hasil)

a = True
b = False
hasil = a or b
print(a, 'OR', b, ' =', hasil)

a = True
b = True
hasil = a or b
print(a, 'OR', b, '  =', hasil)


# ================ Operasi dengan AND ================

print('='* 5, 'Operasi dengan and', '='*5)
a = False
b = True
hasil = a and b
print(a, 'AND', b, ' =', hasil)

a = False
b = False
hasil = a and b
print(a, 'XOR', b, '=', hasil)

a = True
b = False
hasil = a and b
print(a, 'XOR', b, ' =', hasil)

a = True
b = True
hasil = a and b
print(a, 'XOR', b, '  =', hasil)

# ================ Operasi XOR =================

print('='* 5, 'Operasi dengan XOR', '='*5)
a = False
b = True
hasil = a ^ b
print(a, 'XOR', b, ' =', hasil)

a = False
b = False
hasil = a ^ b
print(a, 'XOR', b, '=', hasil)

a = True
b = False
hasil = a ^ b
print(a, 'XOR', b, ' =', hasil)

a = True
b = True
hasil = a ^ b
print(a, 'XOR', b, '  =', hasil)