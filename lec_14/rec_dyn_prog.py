# Recursion and dynamic programming

F = [None] * 10000


def fib(n:int) -> int:
    assert n >= 0 and n < 10000
    if F[n] is None:
        if n <=1:
            F[n] = n
        else:
            F[n] = fib(n-1) + fib(n-2)
    return F[n]


def fib2(n:int) -> int:
    assert n >= 0
    fib_arr = [None] * (n+1)
    fib_arr[:2] = [0, 1]
    for k in range(2, n+1):
        fib_arr[k] = fib_arr[k-1] + fib_arr[k-2]
    return fib_arr[n]