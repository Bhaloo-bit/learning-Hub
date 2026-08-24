# final chapter

import numpy as np
import matplotlib as plt

array1 = np.array([[1,2,3],[4,5,6]])
array2 = np.random.rand(3,3)
array3 =np.zeros(4,4)

np.save('array1.npy', array1)
np.save('array2.npy', array2)
np.save('array3.npy', array3)


loaded_array1 = np.load('array.npy')
print(loaded_array1)