import re
from builtins import print


def password_check(s):
    white_space = re.findall("\s", s)

    valid = re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%&*!])", s)

    if white_space:
        return "White spaces are not allowed in passowrd"
    else:
        if valid:
            return "It is a Strong Password"
        else:
            return "Not a Strong Password"



print(password_check("Shamil123@"))

