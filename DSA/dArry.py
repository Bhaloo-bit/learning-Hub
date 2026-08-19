import numpy as np

# val = np.array([1,2,3,4,5.0, 'a'])
# val = np.array([1,2,3,4], float)  #type casting to assing datatype of arry

# val1 = np.linspace(10,20,2)
# val2 = np.arange(10,20,2)
# for x in val1:
    # print(x , end=", ");

# val = np.zeros(10)
# print(val)
#** Numpy offer hetrogenous array **#
# 
#***********  mutli dimensions array ***********
# 1-D
zero = np.array(10)
# print(zero)

one = np.array([1,2,3,4,5,6])
# print(one)

# 2-D : collection of 1-D array

two = np.array([ [1,2,3],[4,5,6],[7,8,9] ])
print(two)

# 3-D : collection of 2-D array
# dimension should be in equilibrium

three = np.array([ [[1,2],[3,4]], [[5,6],[7,8]] ])
print(three)
