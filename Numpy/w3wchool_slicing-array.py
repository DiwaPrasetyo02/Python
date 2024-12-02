# Slicing adalah teknik untuk mengambil suatu index sampai ke index yang dituju
# Kita akan melakukan slicing dengan konteks seperti ini [Start:End]
# Selain itu kita juga bisa menambahkan step : [Start:End:Step]
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
trr = np.array([[1, 2, 3, 4, 5, 6], [7, 8 , 9, 10 , 11, 12]])

print ('array arr : ', arr)
# Kita akan mengambil index 1 hingga index ke 5

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print('Index pertama hingga index ke 5',arr[1:5])
# Hasil nya akan mengambil start index dan tidak menyertakan end index

# Slice index ke 4 hingga akhir array
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print('Index ke 4 hingga akhir array : ', arr[4:])

#Slice element dari awal sampai ke index ke 4 tentu index ke empat tidak termasuk
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print('Slice dari awal hingga index ke 4{index ke 4 tidak termasuk}: ', arr[:4])

# Negative slicing

# menggunakan tanda negatif untuk mengawali dari akhir array
# SLice dari index ke 3 sampai akhir dari akhir
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print('Slice from index 3 from the end to index 1 from the end : ', arr[-3:-1])

#Step

# Gunakan step untuk mendefinisikan langkah slicing
# Mengembalikan semua element dari 1 sampai 5
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print('elemen 1 sampai 5 menggunakan step 2: ', arr[1:5:2])

#Mengembalikan semua elemen selain 2 dari semua array
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])

# Slicing 2D array
print ('array trr : ', trr)
# Dari elemen ke 2, slice elemen tersebut dari index pertama sampai index ke 4 (index ke 4 tidak akan masuk)
trr = np.array([[1, 2, 3, 4, 5, 6], [7, 8 , 9, 10 , 11, 12]])
print('Akan mengambil elemen kedua, slice index 1 sampai index 4: ', trr[1, 1:4])

# Dari kedua elemen, mengembalikan index ke 2
trr = np.array([[1, 2, 3, 4, 5, 6], [7, 8 , 9, 10 , 11, 12]])
print('Mengambil kedua elemen dan mengembalikan index ke 2: ', trr[0:2, 2])

#Dari kedua elemen, slice index 1 sampai index ke 4, ini akan mengembalikan 2D array
trr = np.array([[1, 2, 3, 4, 5, 6], [7, 8 , 9, 10 , 11, 12]])
print('Mengambil kedua elemen dan index 1 sampai index ke 4: ', trr[0:2, 1:4])



