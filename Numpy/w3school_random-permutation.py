import numpy as np
from numpy import random
'''
Permutasi mengacu pada menyusun nilai sebuah element
misal array [3,2,1] adalah permutasi dari [1,2,3] dan vice-versa (Reverse)
'''

# Shuffling Arrays
# Shuffling adalah teknik untuk mengubah susunan elemen di tempat di array tersebut

print('----------------------------------')
arr = np.array([1,2,3,4,5])
grr = np.copy(arr)
print(arr)
print('----------------------------------')
random.shuffle(arr)
print("Random Shuffle sebuah array yang sudah ditentukan :", arr)
# Shuffle akan langsung mengubah susunan array secara permanen
print('----------------------------------')
# Generate sebuah permutasi acak dari elemen yang kita buat
print("Permutasi acak dari array yang telah kita tentukan :", random.permutation(grr))

