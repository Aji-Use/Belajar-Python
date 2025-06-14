# Operator Bitwise dan Operasi Binary

a = 3
b = 9

c = a | b

print('Nilai : ', a , 'Binary : ', format(a, '08b'))
print('Nilai : ', b , 'Binary : ', format(b, '08b'))
print('--------------------------------(|)')
print('Nilai : ', c , 'Binary : ', format(c, '08b'))

print('\n======== Bitwise AND =========')
c = a & b

print('Nilai : ', a , 'Binary : ', format(a, '08b'))
print('Nilai : ', b , 'Binary : ', format(b, '08b'))
print('--------------------------------(&)')
print('Nilai : ', c , 'Binary : ', format(c, '08b'))

print('\n======== Bitwise XOR =========')
c = a ^ b

print('Nilai : ', a , 'Binary : ', format(a, '08b'))
print('Nilai : ', b , 'Binary : ', format(b, '08b'))
print('--------------------------------(&)')
print('Nilai : ', c , 'Binary : ', format(c, '08b'))