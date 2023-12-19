from timeit import timeit

t1 = timeit(
    'factorial(1000)',
    setup="from factorial import factorial",
    number=100000,
)

t2 = timeit('factorial(1000)',
    setup="from cfactorial import factorial",
    number=100000,
)

print(f"Python : {t1:.3f}")
print(f"Cython : {t2:.3f}")
print(f"Cython is: {t1/ t2:.3f}x faster")