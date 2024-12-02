import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print (arr)
print(np.__version__)
print(type(arr))

trr = np.array((1, 2, 3, 4, 5))
print(trr)

#0D arrays 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
zrr = np.array(42)
print(zrr)

#1D arrays An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
orr = np.array([1, 2, 3, 4, 5])
print(orr)

#2D Arrays An array that has 1-D arrays as its elements is called a 2-D array.
wrr = np.array([[1, 2, 3], [4, 5, 6]])
print(wrr)

#3D Arrays An array that has 2-D arrays (matrices) as its elements is called 3-D array.
rrr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(rrr)

#Check Number of Dimensions
print(trr.ndim)
print(zrr.ndim)
print(orr.ndim)
print(wrr.ndim)
print(rrr.ndim)

#Higher dimensional arrays, we can define the number of dimensions by using the ndim argument

hrr = np.array([1,2,3,4], ndmin=5)
print(hrr)
print('Number of dimensions :', arr.ndim)