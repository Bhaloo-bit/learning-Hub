import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5,])
print("1D array: ", arr_1d)

arr_2d = np.array([[1,2,3], [4,5,6]])
print("2D array:", arr_2d)

''' 1D array:  [1 2 3 4 5]
    2D array: [[1 2 3]
    [4 5 6]]
'''


# list vs Numpy array

py_list = [1,2,3]
print("python list multiplicatin", py_list*2)

np_array = np.array([1,2,3])  # element wise multiplication
print("python list multiplicatin", np_array*2)

'''python list multiplicatin [1, 2, 3, 1, 2, 3]
   python list multiplicatin [2 4 6]'''

import time
start = time.time()
pylist = [i*2 for i in range(1000000)]
print("\n list operation time", time.time() - start)
#list operation time 0.06967687606811523

start2 = time.time()
np_arry = np.arange(1000000) * 2
#print("\n Numpy array operation time", time.time() - start2)

# Numpy array operation time 0.005514621734619141

# ***** Creating array form scratch 

zeros = np.zeros((3,4)) # (row, columns)
print("zeros array : \n", zeros)

ones = np.ones((2,3))
print("ones array : \n", ones)

full = np.full((3,4),13)  # ((dimension rows colums) parameter)
print("full array : \n", full)

random = np.random.random((2,3))
print("random array matrix \n", random)

sequence = np.arange(0, 11, 2)
print("sequence array \n", sequence)


##** Vector, Matrix , Tensor

vector = np.array([1,2,3,4])
print("vetor \n", vector)

matrix = np.array([
                    [1,2,3],
                    [4,5,6]
                ])
print("Matix :", matrix)


tensor = np.array([
                    [[1,2], [3,4]],
                    [[5,6], [7,8]]
                ])
print("tensor \n", tensor)


# Array propertites

arr = np.array([[1,2,3],
                [4,5,6]])

print("shape of array", arr.shape)
print("dimension", arr.ndim)
print("Size", arr.size)
print("Dtype", arr.dtype)

'''
shape of array (2, 3)
dimension 2
Size 6
Dtype int64
'''

### Array Reshapping

arr = np.arange(9)
print("Original array", arr)
#Original array [ 0  1  2  3  4  5  6  7  8 ]

reshaped = arr.reshape((3,3))
print("reshaped array \n ", reshaped)
'''
reshaped array 
  [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

# flatten( return copy)
flattened = reshaped.flatten()
print("flattend  array ", flattened)
# flattend  array  [ 0  1  2  3  4  5  6  7  8  9 10 11]

# ravel (return view, instead of copy)
raveled = reshaped.ravel()
print("\n raveledd aray", raveled)


# transpose

transpose = reshaped.T
print("\n Transpose array", transpose)
