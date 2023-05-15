
def punctuat(s):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in s:
        if i not in punctuations:
            print(i,end=" ")



punctuat("whar?")