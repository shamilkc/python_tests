# sorting words in alphabet order

source_string = 'hello how are you doing my boy!'
source_string = source_string.lower()  # source_string to lower case
# lower cased string source_sorted after using split function
for words in sorted(source_string.split()):
    print(words)
