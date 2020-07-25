# Checking The Correctness Of The Breces Sequence

import stack

def is_breces_sequence_correct(s: str):
    """
    checks the correctness of the breces sequence 
    of parentheses and square brackets () []

    >>> is_breces_sequence_correct("(([()]))[]")
    True
    >>> is_breces_sequence_correct("([)]")
    False
    >>> is_breces_sequence_correct("(")
    False
    >>> is_breces_sequence_correct("]")
    False
    """
    for brace in s:
        if brace not in "()[]":
            continue
        if brace in "([":
            stack.push(brace)
        else:
            assert brace in ")]", "Closing braces expected: " + str(brace)
            if stack.is_empty():
                return False
            left = stack.pop()
            assert left in "([", "Opening braces expected: " + str(brace)
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            if right != brace:
                return False
    return stack.is_empty()            


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)