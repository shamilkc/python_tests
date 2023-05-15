import re

pat = "^[a-zA-Z0-9\\.]+@{1}[a-zA-Z0-9]+\\.{1}[a-zA-Z]{2,4}$"

# mail_list = ['hillard.robel@hotmail.com',
#              'jacynthe.schultz@yahoo.com',
#              'jermain80@hotmail.com',
#              'osborne.abernathy@hotmail.com',
#              'eriberto.kohler@hotmail.com',
#              'wkoss@hotmail.com',
#              'kyleigh64@yahoo.com',
#              'nicola.gottlieb@jacobi.net',
#              'jakob56@yahoo.com',
#              'ardith37@johnston.info']
#
# for i in mail_list:
#     if re.search(pat, i):
#         print(i)

u = input("Enter a email you need to validate: ")

x = re.search(pat,u)
if x:
    print("Your  email is valid")
else:
    print("Your Email is not valid!!!!!")

