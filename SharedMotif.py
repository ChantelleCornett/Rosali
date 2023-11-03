# Return largest commmon substring of the collection

f = open("/Users/m13477cc/Documents/demofile.txt", "r")

input = f.readlines()

dna_strs = []

for i in range(1,len(input),2):
    if '\n' in input[i]:
        input[i]=input[i].replace('\n', '') 
    dna_strs.append(input[i])

match_list = []
for i in range(0,len(dna_strs)):
    for j in range(1,len(dna_strs[i])):
        for k in range(0, len(dna_strs[i])):
        
# start from biggest