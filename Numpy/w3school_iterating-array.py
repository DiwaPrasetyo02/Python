'''
dengan menggunakan iterasi dalam array kita akan lebih mudah untuk mengidentifikasi
tiap elemen yang ada pada multidimensional array di numpy. kita akan menggunakan for loop python
jika kita melakukan iterasi di 1D array maka itu akan bekerja pada elemen 1 per satu
'''
import numpy as np

#iterasi array 1 dimensi
arr = np.array([1,2,3])
print('iterasi array 1D')
for x in arr:
    print(x)
print('----------------------')

#iterasi array 2D
trr = np.array([[1,2,3], [4,5,6]])
print('Iterasi array 2D')
for x in trr:
    print(x)
print('----------------------')

# Iterate on each scalar element of the 2-D array:
w = trr.copy()
for x in w:
    for y in x:
        print(y)
print('----------------------')

# Iterasi array 3D
# pada iterasi 3D array kita akan melalui 2D array

hrr = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
for x in hrr:
    print(x)
print('----------------------')
# untuk mengembalikan nilai asli untuk sklaar kita akan iterasi aray dengan tiap dimensi
q = hrr.copy()
for x in q:
    for y in x:
        for z in y:
            print(z)
print('----------------------')
'''
Iterasi Array Menggunakan nditer()
Fungsi nditer() adalah fungsi bantuan yang dapat digunakan dari iterasi paling dasar hingga sangat lanjut.
Ini memecahkan beberapa masalah dasar yang kita hadapi dalam iterasi, mari kita bahas dengan contoh.

Iterasi pada Setiap Elemen Skalar
Dalam perulangan for dasar, melakukan iterasi melalui setiap skalar array kita perlu
menggunakan n perulangan for yang mungkin sulit untuk ditulis untuk array dengan dimensi yang sangat tinggi.
'''
# Iterasi menggunakan nditer di array 3D
prr = np.array([[[1,2], [3,4]], [[5,6],[7,8]]])
for x in np.nditer(prr):
    print(x)
print('----------------------')

#Iterasi array dengan tipe data yang berbeda
'''
Kita bisa mengguankan argunmen op_dtypes ke tipe data yang kita inginkan saat melakukan iterasi
Numpy tidak merubah tipe data elemen langsung di array tersebut sehingga kita membutuhkan tempat untuk melakukan aksi ini
tempat ini disebut dengan buffer, untuk menggunakannya kita juga harus menggunakan nditer() dan flags=['buffered]
'''
# Iterasi array mengubah nilai menjadi string
arr = np.array([1,2,3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)
print('----------------------')

# Iterasi dengan ukuran langkah yang berbeda
lrr = np.array([[1,2,3,4], [5,6,7,8]])

for x in np.nditer(lrr[:, ::2]):
    print(x)
print('----------------------')

# Menghitung iterasi menggunakan ndumerate()
'''
enumarasi maksudnya adalah mentioning sekuens nomor sesuatu satu persatu
'''
# Enumatasi 1D array
drr = np.array([1,2,3])
for idx, x in np.ndenumerate(drr):
    print(idx, x)
print('----------------------')

#Enumarasi 2D array
jrr = lrr.copy()

for idx, x in np.ndenumerate(jrr):
    print(idx, x)
print('----------------------')
print(' S E L E S A I ')

