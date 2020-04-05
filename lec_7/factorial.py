def factorial(n):
    assert n >= 0, "Factor of the negative isn't defined"
    if n == 0:
        return 1
    return factorial(n-1)*n
