# NIM : 1124102195 
# NAMA : Scendy Aprianda Islamy

#Menginputkan bilangan

a = int(input('Masukkan bilangan pertama: '))
b = int(input('Masukkan bilangan kedua: '))

#Operasi aritmatika dengan assignment operator

penjumlahan = a 
penjumlahan += 10

pengurangan = a
pengurangan -= 5

perkalian = a
perkalian *= 2

pembagian = a
pembagian /= 3

modulus = a
modulus %= 6

pembagian_kebawah = a
pembagian_kebawah //= b

pangkat = a
pangkat **= b

precedence = a
precedence += b * 2

#Menampilkan hasil
print('Hasil penjumlahan :', penjumlahan)
print('Hasil pengurangan :', pengurangan)
print('Hasil perkalian :', perkalian)
print('Hasil pembagian :', pembagian)
print('Hasil modulus :', modulus)
print('Hasil pembagian kebawah :', pembagian_kebawah)
print('Hasil pangkat :', pangkat)
print('Hasil precedence :', precedence)