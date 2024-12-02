import numpy as np

arr = np.array([1, 2, 3, 4])
# Get the first index of the array
print(arr[0])
# Get the second index of the array
print(arr[1])
# Get the third and fourth elements of the array
print(arr[2] + arr[3])

# Indexing 2D arrays
wrr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('2nd element on 1st row : ', wrr[0, 1])
# access the 2nd row of the 5th column
print('5th element on 2nd row: ', wrr[1, 4])

#Indexing 3D arrays
rrr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(rrr[0, 1, 2])

# Negative Indexing
nrr = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
print('The last element from the 2nd dim: ', nrr[1, -1])

