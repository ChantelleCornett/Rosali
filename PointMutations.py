f = open("/Users/m13477cc/Documents/demofile.txt", "r")
input = f.readlines()
str1, str2 = input[0], input[1]

diffs = []
count = 0
for i in range(0,len(str1)-1):
    if str1[i] != str2[i]:
        count += 1

print(count)