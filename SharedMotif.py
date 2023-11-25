# Return largest commmon substring of the collection

f = open("/Users/m13477cc/Documents/demofile.txt", "r")

input = f.readlines()
with_s = len([x for x in input if x.startswith('>')])
print(with_s)
dna_strs = []

for i in range(1,len(input),2):
    if '\n' in input[i]:
        input[i]=input[i].replace('\n', '') 
    dna_strs.append(input[i])

min_len_str = min(dna_strs, key = len)

count = 0

for j in range (len(min_len_str),1,-1):
    for k in range(0,len(min_len_str) - j, 1):
        count = 0
        for i in dna_strs:
            if i.find(min_len_str[k:k+j]) > -1: 
                count += 1
            next
            if count == with_s:
                print('max string: ', min_len_str[k:k+j])
                if 1:
                    break
            
            

