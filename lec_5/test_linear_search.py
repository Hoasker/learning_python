def array_search(A:list, N:int, x:int):
    """
    Searches for the number x in array A
    from 0 to N-1 index inclusive.
    Returns the index of element x in array A.
    Or -1 if there is none.
    If there are several identical elements in the array,
    equal to x, then return the index of the first in a row.
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1


def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print("#test1 - ok")
    else:
        print("#test1 - fail")


    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print("#test2 - ok")
    else:
        print("#test2 - fail")


    A3 = [10, 20, 30, 10, 10]
    m = array_search(A3, 5, 10)
    if m == 0:
        print("#test3 - ok")
    else:
        print("#test3 - fail")


test_array_search()
