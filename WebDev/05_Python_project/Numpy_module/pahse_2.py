## Numpy Array operations

import numpy as np

arry = np.array([1,2,3,4,5,6,7,8,9,10])
print("Basic Slicing", arry[2:7])
print("with step",arry[2:8:2])
print("Negative indexing",arry[-4])

'''
Basic Slicing [3 4 5 6 7]
with step [3 5 7]
Negative indexing 7
'''
arry_2D = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])

print("Specific element", arry_2D[1,2])
print("entire row", arry_2D[0])
print("entire row", arry_2D[:,1])

'''
Specific element 6
entire row [1 2 3]
entire row [2 5 8]
'''

# Sorting 

unsorted = np.array([4,3,2,1,4,6,7,4,3,9,8])
print("Sorted Array", np.sort(unsorted))

arr_2d_unsorted = np.array([[1,5], [8,3], [4,2],[3,8]])
print("2D aray sort by column", np.sort(arr_2d_unsorted, axis =0))
print("2D aray sort by row", np.sort(arr_2d_unsorted, axis =1))

'''
Sorted Array [1 2 3 3 4 4 4 6 7 8 9]
2D aray sort by column [[1 2]
 [3 3]
 [4 5]
 [8 8]]
2D aray sort by row [[1 5]
 [3 8]
 [2 4]
 [3 8]]
'''

## filter  

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even_arry = numbers[numbers % 2 == 0]
print("Even numbers", even_arry)

#Even numbers [ 2  4  6  8 10]

## Filter with mask 

mask = numbers > 5
print("Numbers greater than 5", numbers[mask])

#Even numbers [ 2  4  6  8 10]


## fancy indexing vs nu.where()

indices = [0, 2, 4]
print(numbers[indices])

where_reuslt = np.where(numbers > 5)
print("NP where", numbers[where_reuslt])

'''(array([5, 6, 7, 8, 9]),)
NP where [ 6  7  8  9 10]
'''

condition_array = np.where(numbers > 5 , numbers*2, numbers)
condition_array = np.where(numbers > 5 , "true", "false")
print(condition_array)

'''
NP where [ 6  7  8  9 10]
['false' 'false' 'false' 'false' 'false' 'true' 'true' 'true' 'true'
 'true']'''


## Adding and removing data 

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

combined = np.concatenate((arr1, arr2))
print(combined)

# array compatibility

a = np.array([1,2,3])
b = np.array([4,5,6,7])
c = np.array([7,8,9])

print("Compatibility shapes", a.shape == b.shape)


original = np.array([[1,2], [3,4]])
new_row = np.array ([[5,6]])

with_new_row = np.vstack((original, new_row)) # to add new row
print(original)
new_col = np.array([[7],[8]])
with_new_col = np.hstack((original,new_col))
print(with_new_row,"\n")
print(with_new_col)

'''
 [3 4]]
[[1 2]
 [3 4]
 [5 6]] 

[[1 2 7]
 [3 4 8]]
'''

# deletion

arr = np.array([1,2,3,4])
deleted = np.delete(arr,2) # return updated array
print(deleted)