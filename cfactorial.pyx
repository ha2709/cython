# cython: language_level=3

cpdef int factorial(int x):
    cdef int f = 1
    cdef int i

    for i in range(x):
        f *= ( x - i)
    # print(9, f)
    return f
