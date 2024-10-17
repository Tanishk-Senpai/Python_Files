import numpy as np

a = np.array([1,2,3,4,5])
print(a[:])

b = np.array([[1,2,3],
             [4,5,6]])

print(b[1])

print(b.shape)


c = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(c.ndim)
print(c.shape)
print(c.size)
print(c.dtype)