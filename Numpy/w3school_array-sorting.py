'''
sorting array merupakan sebuah metode untuk melakukan pengurutan nomor, perubahan alfabet
dll.
untuk menggunakan sorting array di numpy kita akan menggunakan fungsi sort()
'''
import numpy as np
print("=========================")
arr = np.array([12,4,15,21])
print(np.sort(arr))
print("=========================")
#metode ini tidak akan mengganti nilai dari array kita sehingga hanya melakukan pengurutan

print('sorting dengan alfabet')
brr = np.array(['Pisang', 'Mangga', 'Jeruk', 'Kurma'])
print(np.sort(brr))
print("=========================")

print('Melakukan sorting dengan nilai boolean')
orr = np.array([False, True, False])
print(np.sort(orr))
print("=========================")

print('Sorting array 2D')
trr = np.array([[2,1,9,0], [7,5,1,0.3]])
print(np.sort(trr))
print("=========================")


