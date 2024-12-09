'''
Dengan menggunakan tambahan parameter yaitu p maka kita bisa membuat sebuah probabilitas
seberapa sering sebuah nomor itu muncul di nilai acak yang akan kita buat
'''

import numpy as np
from numpy import random

x = random.choice([1,2,3,4], p=[0.5, 0.2, 0.3, 0.0], size=(100))
print("Menghaslikan 1D Array nilai probalitas yang telah ditentukan :\n", x)
print("-----------------------------------------------------------------")

# Menghasilkan nilai 2D array dengan cara yang sama

x = random.choice([4,5,6,69], p = [0.0, 0.1, 0.05, 0.85], size=(2,3))
print('Menghasilkan 2D array dengan nilai probabilitas yang telah ditentukan :\n', x)

