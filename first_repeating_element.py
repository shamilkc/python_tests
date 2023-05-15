S="abcdefa"

S2 = ""

for i in S:
    if i in S2:
        print(i)
        break
    S2 += i


