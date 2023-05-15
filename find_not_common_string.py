A = 'geeksforgeeks'
B = 'geeksquiz'


s = ""

for i in A:
    if i not in B:
        s += i

for j in B:
    if j not in A:
        s += j


print(s)



