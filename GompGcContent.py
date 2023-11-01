from Bio import SeqIO
import pandas as pd
import re

f = open("/Users/m13477cc/Documents/demofile.txt", "r")
input = f.readlines()

n_input = ','.join(input)
s_input = n_input.split('>')
s_in = s_input[1:]
new = [i.replace('\n','') for i in s_in]
new2 = [i.replace(',','') for i in new]
new3 = [re.split('(Rosalind_+[0-9]+[0-9]+[0-9]+[0-9])', i) for i in new2]
new4 = [i[1:] for i in new3]

percList=[]
for i in range (0, len(new4)):
    perc = (new4[i][1].count('G') + new4[i][1].count('C'))/ len(new4[i][1])
    percList.append(perc*100)

print(new4[pd.Series(percList).idxmax()][0])
print(max(percList))




