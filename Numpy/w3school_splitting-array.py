'''
Memisahkan array merupakan operasi yang berkebalikan dengan operasi menggabungkan array
dengan menggunakan array_split() kita akan memisahkan sebuah array menjadi yang kita mau
'''

import numpy as np
print("---------------------------")
print("Split array menjadi 3 kolom")
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])
print("---------------------------")

# Jika sebuah array memiliki elemen yang lebih kecil dari persyaratan maka hal itu akan menyesuaikan dengan yang tertera di akhir
print("Split array menjadi 4 bagian")
frr = arr.copy()
frr = np.array_split(frr, 4)
print(frr)
print("---------------------------")
print("Jika melebihi yang ditentukan maka numpy akan memperhitungkannya sendiri")
srr = ([7,8,9])
srr = np.concatenate((arr, srr))
srr = np.array_split(srr, 9)
print(srr)
print("---------------------------")

#Splitting 2D array
print("Split 1 array 2D menjadi 3 array 2D")
drr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
drr = np.array_split(drr, 3)
print(drr)
print("---------------------------")

print("Split 2D array yang terdapat 3 kolom dibagi menjadi 3 array")
trr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(trr, 3)
print(newarr)
print("---------------------------")

# split array dengan axis = 1 atau berdasarkan baris
brr = trr.copy()
brr = np.array_split(brr, 3, axis = 1)
print(brr)
print("---------------------------")

#Kita juga bisa menggunakan hsplit dan hstack sebagai alternatif
print("Menggunakan hsplit() untuk split array brdsrkan baris")
hrr = trr.copy()
hrr = np.hsplit(hrr, 3)
print(hrr)
for x in hrr:
    print(f"array ke {x}", x)
print("---------------------------")

#Kita juga bisa menggunakan vstack dstack jika di split namanya adalah vsplit dan dsplit
