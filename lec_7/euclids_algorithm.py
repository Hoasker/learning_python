def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    

gcd(4, 5)


def alter_gcd(a, b):
    return a if b == 0 else gcd(b, a%b)


alter_gcd(4, 5)
