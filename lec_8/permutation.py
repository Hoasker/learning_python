def find(number, A):
    """
    Searches for a number in the A and returns True, if any
    False, if none exist
    """
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
            #return True
    return flag
    #return False
            

def generate_permutations(N, M=-1, prefix=None):
    """
    Generate all permutations of N numbers in M ​​positions,
    starting with the prefix
    """
    M = N if M == -1 else M # default N numbers in M ​​positions
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()


generate_permutations(3, 3)
