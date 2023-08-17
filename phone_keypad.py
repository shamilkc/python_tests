keypad = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: " "
}
num = []
def check_char(s):
    for i in s:
        for x,y in keypad.items():
            for j in y:
                if j == i:
                    t = y.index(j)
                    for z in range(t+1):
                        num.append(x)
    return [print(n, end="") for n in num]




check_char("sddff")
