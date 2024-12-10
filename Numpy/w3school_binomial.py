import numpy as np
from numpy import random
'''
Distribusi Binomial adalah distribusi diskrit
dimana distribusi ini akan menghasilkan bilangan bulat dapat dihitung dan tidak negatif
atau bisa juga dalam bentuk boolean yaitu True atau False dimana hanya terdapat 2 pilihan
Pada numpy terdapat 3 Parameter untuk menggunakan fungsi ini
n : Nilai dari pilihan
p : probabilitas munculnya sebuah pilihan
size : Ukuran array atau percobaan yang akan dikembalikan
'''
x = random.binomial(n=2, p=0.5, size=20)

print(x)

