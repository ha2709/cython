def factorial(x):
    f = 1
    for i in range(x):
        f *= (x-i)
    # print(5, f)
    return f
