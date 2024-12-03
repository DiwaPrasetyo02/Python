'''
reshape merupakan merubah bentuk ukuran sebuah array
ukuran sebuah array merupakan sebuah elemen dari tiap dimensi
dengan melakukan reshaping kita bisa menambahkan atau menghapus dimensi atau mengganti nomor
elemen setiap dimensi
'''

import numpy as np

# convert 1d array dengan 12 elemen ke 2D array
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)
print(newarr)
print(newarr.shape)
print('---------------------------------')

#Reshape dari 1D ke 3D
x = arr.copy()
x = x.reshape(2,3,2)
print(x)
print(x.shape)
print('---------------------------------')
'''
Apakah kita bisa melakukan reshape ke semua ukuran? 
ya selama element array yang kita miliki bisa masuk ke ukuran yang kita inginkan
kita bisa melakukan reshape 8 elemen 1D array ke 4 elemen di 2 baris 2D array. Akan tetapi
kita tidak bisa reshape ke 3element 3 baris karena 3 elemen dan 3 baris dibutuhkan 3x3 = 9 elemen
'''
# Periksa apakah array yang sudah kita reshape itu masuk ke copy atau view
arr = np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4).base)
print('---------------------------------')

# unknown dimension
'''
kita diperbolehkan untuk memiliki 1 dimensi yangtidak diketahui
yang dimaksud adalah kita tidak perlu menspesifikkan sebuah nomor untuk mengatur dimensi di reshape
berikan nilai -1 maka numpy akan melakukan kalkulasi nomor ini. kita hanya bisa memberikan nilai -1
sebanyak 1 kali
'''
urr = np.array([1,2,3,4,5,6,7,8])
urr = urr.reshape(2,2,-1)
print(urr)
print(urr.shape)
print('---------------------------------')

# Flattening array
'''
Flattening array merupakan suatu teknik untuk melakukan konversi multidimensional array ke 1D array
kita bisa menggunakan reshape(-1) untuk melakukan ini
'''
frr = np.array([[1,2,3], [4,5,6]])
frr = frr.reshape(-1)
print(frr)
print(frr.shape)

