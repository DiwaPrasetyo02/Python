'''
Perbedaan utama antara copy dan view pada numpy adalah bahwa copy akan membuat sebuah array baru.
sedangkan view hanya akan melihat array asli.
copy akan membuat array baru dan bisa dirubah tanpa mempengaruhi array asli atau yang di copy
view tidak akan membuat array baru, dan perubahan yang terjadi pada view akan mempengaruhi array
asli
'''
import numpy as np
# Membuat copy sebuah array asli dan menampilkan keduanya
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
#Copy tidak akan terpengaruh dengan perubahan yang dilakukan oleh array asli

#Membuat sebuah view dan mengganti array asli dan menampilkan keduanya
vrr = np.array([1,2,3,4,5])
x = vrr.view()
vrr[0] = 42
print(vrr)
print(x)
print('Mencoba mengubah nilai di view apakah akan berpengaruh pada nilai asli')
x[1] = 30
print(vrr)
print(x)

# Melihat apakah array memiliki hak milik data tersebut
'''
Seperti yang sudah di mention diatas bahwa. melakukan copy akan membuat copy memiliki data dan tidak memiliki original object.
view sebaliknya. bagaimana cara untuk mengecek hal ini? di numpy kita bisa menggunakan atribut base
yang akan mengembalikan nilai None jika array tidak memiliki data tersebut.
Base merujuk pada original object.
'''
# Print nilai atribut base untuk melihat sebuah kepemilikan array
orr = np.array([1,2,3,4,5])
x = orr.copy()
y = orr.view()
print(x.base)
print(y.base)
