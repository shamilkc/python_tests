list1= []

with open("files/names.txt", "r", encoding='utf-8') as name_file:
    lines = name_file.readlines()
    print(lines)
