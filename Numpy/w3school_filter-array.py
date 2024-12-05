'''
filtering merupakan salah satu kondisi untuk hanya memasukkan elemen yang dipilih
jika elemen tersebut tidak dipilih maka akan dikeluarkan
'''
import numpy as np
arr = np.array([41,42,43,44])

x = [True, False, True, False]
print("Elemen pilihan")
newarr = arr[x]
print(newarr)
print('**************************')

'''
Pada kode diatas untuk melakukan filtering kita menggunakannya dengan kode langsung
akan tetapi sebenanrnya untuk melakukan filtering kita akan membuat sebuah kondisi
jika kondisi terpenuhi maka nilai akan tetap bertahan
jika kondisi tidak terpenuhi maka nilai akan dikeluarkan
'''
#Buat sebuah array kosong untuk menampung hasil
filter_arr = []

# Menelusuri tiap nilai di dalam array
for element in arr:
    # jika elemen tersebut lebih dari 42 maka akan set nilai true, sebaliknya adalah false
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
print("!!!!!!!!!!!!!!!!!!!!!!!!!")

# Membuat sebuah filter array dimana hanya nilai genap yang berasal dari array asli yang akan ditampilkan

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
print("!!!!!!!!!!!!!!!!!!!!!!!!!")

# Kita juga bisa menggunakan cara instant dengan langsung membuat kondisinya
print('filter array nilai > 42')
arr = np.array([41,42,43,44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
print("!!!!!!!!!!!!!!!!!!!!!!!!!")

# Langsung membuat sebuah kondisi bilangnan ganjil
print('array filter ganjil only')
grr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
filter_grr = grr % 2 == 1
new_grr = grr[filter_grr]
print(filter_grr)
print(new_grr)
