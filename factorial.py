def fact(num):
    s = 1
    for i in range(1, num + 1):
        s = s * i
    return s


x = fact(5)
print(x)


