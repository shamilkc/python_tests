
def sum_of_n(num):
    if num <= 1:
        return num
    else:
        return num + sum_of_n(num-1)


print(sum_of_n(7))
