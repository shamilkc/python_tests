# Find non-repeating value


arr = [1, 2, 3, 5, 3, 2, 1, 4, 5, 6, 6]

for i in arr:
    if arr.count(i) == 1:
        print(i)
