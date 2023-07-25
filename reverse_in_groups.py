# Reverse in group s

a = [1, 2, 3, 4, 5, 6, 6, 8, 9, 0, 6, 7, 8, 4]

s = 3
i = 0

while i < len(a):

    print(a[i:i + s][::-1])

    i += s
print(a[::-1])