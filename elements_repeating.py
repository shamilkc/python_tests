# Return the elements repeating K times.

def check_repeat(k, a):
    l1 = []
    for i in a:
        if a.count(i) == k:
            l1.append(i)

    ans = set([x for x in l1])
    return ans


print(check_repeat(2, [1, 7, 4, 1, 4, 8, 7]))
