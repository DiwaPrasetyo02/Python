'''
ukuran sebuah array merupakan angka sebuah elemen dalam setiap dimensi
'''
# Mendapatkan ukuram sebuah array
import numpy as np
arr = np.array([[1,2,3,4], [5,6,7,8]])
print(arr.shape)
trr = np.array([[1,2,3,4,10], [5,6,7,8,11]])
print(trr.shape)
yrr = np.array([[1,2,3,4,10], [13,14,15,16,17], [5,6,7,8,11]])
print(yrr.shape)
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)
