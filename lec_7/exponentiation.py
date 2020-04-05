def pows(a, n):
    if n == 0:
        return 1
    elif n%2 == 1:
        return pows(a, n-1)*a
    else:
        return pows(a**2, n//2)


pows(2, 4)


def fast_pow():
    pass

fast_pow()
