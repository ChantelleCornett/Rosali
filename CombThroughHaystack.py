import re
f = open("/Users/m13477cc/Documents/demofile.txt", "r")
input = f.readlines()
str1, str2 = input[0][:-2].strip(), input[1].strip()

l = [(i.start() + 1 ) for i in re.finditer((r"(?=(" + str2 + "))"), str1)]

print(' '.join(map(str, l)))