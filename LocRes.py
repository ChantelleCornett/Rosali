# Rev palindrome if its equal to reverse compliment
import pandas as pd
import re

f = open("/Users/m13477cc/Documents/demofile.txt", "r")
input = (f.readlines())[1:]
no_nl = [i.replace('\n','') for i in input]
stripped = [i.replace(',','') for i in no_nl]
dna = ''.join(stripped)

mapping_table = str.maketrans({'A':'T', 'T':'A', 'G':'C', 'C':'G'})

comp_dna = dna.translate(mapping_table)

found = {}
for i in range(4,13,1):
    count = 0
    for j in range(0,len(dna)-i+1):
        if dna[j:j+i] == (comp_dna[j:j+i])[::-1]:
            found[j+1] = i

sorted_dic = dict(sorted(found.items())) 

for i in sorted_dic:
    print(i, "", sorted_dic[i])
