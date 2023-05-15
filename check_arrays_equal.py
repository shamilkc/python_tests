# check arrays are equal
# Explanation: Both the array can be
# rearranged to {0,1,2,4,5}

def array_equal_check(a, b):
    if sorted(a) == sorted(b):
        return "equal"
    else:
        return "not equal"


print(array_equal_check([1, 2, 5, 4, 0], [2, 4, 5, 0, 1]))
