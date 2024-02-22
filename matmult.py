# Program to multiply two matrices using nested loops
import numpy as np

N = 250

# NxN matrix
X = np.random.randint(0,100,(N,N))

# NxN matrix
Y = np.random.randint(0,100,(N,N+1))

# result is Nx(N+1)
result = np.matmul(X,Y)

for r in result:
    print(r)