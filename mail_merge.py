import os

print(os.listdir("/Users/shamilkc/PycharmProjects/pythonTests/files"))
print(os.getcwd())

with open("/Users/shamilkc/PycharmProjects/pythonTests/files/names.txt", "r") as names_file:
    with open("/Users/shamilkc/PycharmProjects/pythonTests/files/bd.txt", "r", ) as body_file:
        bd = body_file.read()

        for name in names_file:
            mail = "Hi " + name.strip() + "\n" + bd


            with open("/Users/shamilkc/PycharmProjects/pythonTests/files/" + name.strip() + ".txt", "w") as mail_file:
                mail_file.write(mail)
