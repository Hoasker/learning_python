def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
        return
    # for digit in "0", "1":
    # gen_bin(M-1, prefix+digit)
    gen_bin(M-1, prefix+"0")
    gen_bin(M-1, prefix+"1")


def generate_numbers(N, M, prefix=None):
    """
    Generates all numbers (with leading insignificant zeros)
    in the N number system (N <= 10)
    of length M
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()
    
# for binary system
gen_bin(5)

# dyal arbitrary number system
generate_numbers(3, 3)
