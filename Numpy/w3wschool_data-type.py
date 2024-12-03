'''
Secara default python memiliki beberapa jenis tipe data
string : untuk mempresentasikan data text, dan text diberikan tanda petik dua
integer : untuk mempresentasikan bilangan bulat seperti 1 2 -1 -2
boolean : untuk mempresentasikan keadaan True atau False
complex : untuk memrpresentasikan bilangan complex seperti 1.0 + 2.0j

Pada numpy terdapat tambahan tipe data yang diisyaratkan dengan satu huruf saja
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - Object
S - String
U - Unicode String
V - Fixed chink of memory for other type (Void)
'''

# Memeriksa tipe data sebuah array
import numpy as np
arr = np.array([1,2,3,4])
print (arr.dtype)
srr = np.array(['Apple', 'Banana', 'Cherry'])
print(srr.dtype)

#Membuat arrays dengan tipe data yang terdefinisi
# Membuat array dengan tipe data string
trr = np.array([1,2,3,4], dtype='S')
print(trr)
print(trr.dtype)
# Membuat array dengan tipe data 4bytes integer
irr = np.array([1,2,3,4], dtype='i4')
print(irr)
print(irr.dtype)

