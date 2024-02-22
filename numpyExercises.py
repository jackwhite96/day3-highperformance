''' Exercise 2 of Day 3 '''
import numpy as np

# a. Create a null vector of size 10 but the fifth value which is 1
vect_a = np.zeros(10, dtype=int)
vect_a[4] = 1 # 5th element is index 4
print(vect_a)

# b. Create a vector with values ranging from 10 to 49
vect_b = np.arange(10,50) # includes 49, but not 50
print(vect_b)

# c. Reverse a vector (first element becomes last)
vect_c = np.array(vect_b[::-1])
print(vect_c)

# d. Create a 3x3 matrix with values ranging from 0 to 8
mat_d = np.arange(9).reshape(3,3)
print(mat_d)

# e. Find indices of non-zero elements from [1,2,0,0,4,0]
vect_e = [1,2,0,0,4,0]
print(np.nonzero(vect_e))

# f. Create a random vector of size 30 and find the mean value
vect_f = np.random.random(30)
print(np.mean(vect_f))

# g. Create a 2d array with 1 on the border and 0 inside
vect_g = np.zeros(9, dtype=int)
vect_g[0] = 1
vect_g[-1] = 1
mat_g = vect_g.reshape(3,3) # Could've reshaped first but this works
print(mat_g)

# h. Create a 8x8 matrix and fill it with a checkerboard pattern
mat_h = np.zeros((8,8), dtype=int)
mat_h[1::2,::2] = 1
mat_h[::2,1::2] = 1
print(mat_h)

# i. Create a checkerboard 8x8 matrix using the tile function
mat_i1 = np.array([[1,0],[0,1]])
mat_i2 = np.tile(mat_i1, (8,8))

# j. Given a 1D array, negate all elements which are between 3 and 8, in place
vect_j = np.arange(11)
vect_j[3:9] = -1 * vect_j[3:9]
print(vect_j)

# k. Create a random vector of size 10 and sort it
vect_k = np.random.random(10)
vect_k[:] = np.sort(vect_k) # sorted in-place as I don't need the unsorted array

# l. Consider two random arrays A and B, check if they are equal
vect_l1 = np.random.randint(0,2,5)
vect_l2 = np.random.randint(0,2,5)
equal = np.array_equal(vect_l1, vect_l2)
print(equal)

# m. How to convert an integer (32 bits) array into a float (32 bits) in place?
vect_m = np.arange(10, dtype=np.int32)
print(vect_m.dtype)
vect_m = vect_m.astype(np.float32, copy=False)
print(vect_m.dtype)

# n. How to get the diagonal of a dot product?
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.trace(C) # Assuming trace of the matrix is the same as the diagonal
print(D)