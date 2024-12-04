'''
Kita bisa mencari nilai dalam sebuah array dan mengembalikan nilai yang serupa dengan yang kita cari
kita akan menggunakan method where()
'''

import numpy as np

print('Temukan index dimana nilai 4 berada')
arr = np.array([1,2,3,4,5,4,4])
x = np.where(arr == 4)
print(x)
print("-----------------------------------")
# Dari nilai tersebut akan dikembalikan pada tipe tuple

print("Carilah index ke berapa yang terdapat nilai genapnya")
grr = np.array([1,2,3,4,5,6,7,8])
x = np.where(arr%2 == 0)
print(x)
print("-----------------------------------")

print("Carilah index ke berapa yang terdapat nilai ganjilnya")
jrr = np.array([1,2,3,4,5,6,7,8,9])
x = np.where(jrr%2 == 1)
print(x)
print("-----------------------------------")

#Search sorted merupakan sebuah metode untuk pencarian secara biner di sebuah array
#Metode searchsorted() mengasumsi untuk melakukan sorting array

print("Temukan di index berapa nilai 7 harus dimasukkan")
krr = np.array([6,7,8,9])
x = np.searchsorted(krr, 7)
print(x)
print("-----------------------------------")

print("Menemukan diindex berapa nilai 7 berada namun mencari dari sisi kanan")
y = np.searchsorted(krr, 7, side='right')
print(y)
print("-----------------------------------")

print("Temukan di index ke berapa nilai 123 dimasukkan")
z = np.searchsorted(krr, [1,2,3])
print(z)

