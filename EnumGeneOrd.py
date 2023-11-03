# calculate number of permutations, given an integer
import itertools

num = input("What is the integer?")
f= open("Enum.txt","w+")
num_list = list(range(1,int(num) +1))
f.write(str(len(list(itertools.permutations(num_list))))+'\n')
for i in (list((itertools.permutations(num_list)))):
    f.write(((str(i)[:-1])[1:]).replace(',','')+'\n')
f.close()