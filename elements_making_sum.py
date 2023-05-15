# Find the elements make a sum of s

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = 15

l1 = []
for i in range(len(A) + 1):
    for j in range(i):
        if sum(A[j:i]) == s:
            print("elements from position", j, "to", i, "are equal to ", s)
