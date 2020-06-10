import numpy as np
iteration = 1000

# initialize the matrix
A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])
# initialize the RHS vector
b = np.array([6., 25., -11., 15.])

# prints the system
print("System:")
for i in range(A.shape[0]):
    row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print(" + ".join(row), "=", b[i])
print()

x = np.zeros_like(b)
for i in range(iteration):
    print("Current solution:", x)
    x_new = np.zeros_like(x)

    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]

    if np.allclose(x, x_new, rtol=1e-10):
        break

    x = x_new

print("Solution:")
print(x)
error = np.dot(A, x) - b
print("Error:")
print(error)

import timeit
setup = '''
import random

random.seed('slartibartfast')
s = [random.random() for i in range(1000)]
timsort = list.sort
'''
print(min(timeit.Timer('a=s[:]; timsort(a)', setup=setup).repeat(7, 1000)))

"""Using timeit function (Measure execution time of small code snippets)"""

import timeit
def main():
    # code to be executed as setup (must include import statement)
    init = "import numpy; nd = numpy.arange(100).reshape((10,10))"

    t = timeit.Timer(stmt= "nd[5][5]", setup= init)
    print(t.repeat(repeat= 3, number= 10000000))

    t = timeit.Timer(stmt= "nd[5,5]", setup= init)
    print(t.repeat(repeat = 3, number= 10000000))

if __name__ == "__main__":

    main()