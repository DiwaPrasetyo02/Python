'''
nomor acak bukanlah nomor yang berbeda setiap waktu atau memiliki sebuah pola.
nomor acak atau random merupakan nomor yang secara logika tidak dapat diprediksi nilai selanjutnya
'''
import numpy as np
from numpy import random

x = random.randint(100)
print("------------------------------")
print("Nomor acak dari 0 sampai 100 :",x)
x = random.rand()
print("Generate nilai float dari 0 sampai 1 :", x)
print("------------------------------")

'''
Saat kita menggunakan numpy tentunya kita akan terlibat dengan array, kita bisa membuat sebuah array acak dengan menggunakan 2 metode
dengan menggunakan fungsi randint() membutuhkan parameter size sebagai penentu ukuran sebuah array
'''
x = random.randint(100, size=(5))

print("Generate 1D array yang menghasilnya 5 angka acak dari 0 sampai 100 :", x)
print("------------------------------")

x = random.randint(100, size=(3, 5))
print("Generate 2D aray dengan 3 baris mengandung nilai rentang 0 sampai 100 dengan bentuk 3 baris 5 kolom:\n", x)
print("------------------------------")

# Kita juga bisa menggunakan tipe data float untuk menentukan nilai yang pastinya antara 0 sampai 1

x = random.rand(5)
print("Menghasilkan 1D array dengan 5 baris nilai float :", x)
print("------------------------------")

x = random.rand(3,5)
print("Menghasilkan 2D array dengan baris 3 kolom 5 dengan nilai 0 sampai 1 :\n", x)
print("------------------------------")

# Metode lainnya adalah choice() dimana kita bisa menentukan nilai array berdasarkan nilai yang kita tentukan

x = random.choice([3,4,5,6])
print("Menghasilkan nilai array dengan parameter yang telah ditentukan :", x)

# Menambahkan size sebagai parameter bentuk array
x = random.choice([1,3,5,7], size=(3,5))
print("Menghasilkan nilai yang telah ditentukan dengan bentuk array 3,2 :\n", x)