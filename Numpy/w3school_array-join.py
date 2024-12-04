'''
menggabungkan array dari satu atau lebih array.
Di SQL untuk menggabungkan array kita melakukannya berdasarkan key sedangkan di numpy kita akan menggunakan axes
dengan menggunakan fungsi concatenate(). Jika axis tidak di inisialisasi maka akan diberikan nilai default yaitu 0
'''
import numpy as np

#Join dua array
print("---------------------------")
print("Menggabungkan 2 array 1D menjadi 1 array 1D")
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1, arr2))
print(arr)
print("---------------------------")

#Menggabungkan 2 Array 2D dengan baris (axis = 1)
print("Menggabungkan 2 array 2D berdasarkan baris")
drr1 = np.array([[1,2], [3,4]])
drr2 = np.array([[5,6], [7,8]])
drr = np.concatenate((drr1, drr2), axis = 1)
print(drr)
print("---------------------------")

'''
Mengabungkan array dengan menggunakan fungsi fungsi stack. stacking hampir sama dengan concatenate namun perbedaannya adalah
stacking akan membuat axis baru.
'''
print("Menggabungkan array 1D dengan menggunakan fungsi stacking")
srr1 = arr1.copy()
srr2 = arr2.copy()
srr = np.stack((srr1, srr2), axis = 1)
print(srr)
print("---------------------------")

# untuk melakukan stacking berdasarkan baris kita akan menggunakan fungsi hstack()
print("Menggabungkan 2 array menjadi 1 berdasarkan baris dengan fungsi hstack")
hrr1 = arr1.copy()
hrr2 = arr2.copy()
hrr = np.hstack((hrr1, hrr2))
print(hrr)
print("---------------------------")

# Untuk menggabungkan 2 array menjadi 1 berdasarkan column kita bisa menggunakan fungsi vstack()
print("Menggabungkan 2 array menjadi satu berdasarkan kolom")
vrr1 = arr1.copy()
vrr2 = arr2.copy()
vrr = np.vstack((vrr1, vrr2))
print(vrr)
print("---------------------------")

# Library Numpy menyediakan fungsi bantuan lainnya yaitu dstack berdasarkan tinggi ukuran array yang akan sama dengan
# kedalaman array tersebut
print("Menggunakan fungsi dstack()")
krr1 = arr1.copy()
krr2 = arr2.copy()
krr = np.dstack((krr1, krr2))
print(krr)

