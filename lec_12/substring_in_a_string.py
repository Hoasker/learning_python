# search for a substring in a string

# s = "abacabadabacabafabacabadabacabadabacabafaba"
# sub = 'dabac'

def equal(A, B):
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True


def  search_substring(s, sub):
    for i in range(0, len(s)-len(sub)):
        if equal(s[i:i+len(sub)], sub):
            print(i)
