# Return largest commmon substring of the collection
from difflib import SequenceMatcher

f = open("/Users/m13477cc/Documents/demofile.txt", "r")

input = f.readlines()
with_s = len([x for x in input if x.startswith('>')])

dna_strs = []

for i in range(1,len(input),2):
    if '\n' in input[i]:
        input[i]=input[i].replace('\n', '') 
    dna_strs.append(input[i])

min_len_str = min(dna_strs, key = len)

result = ""
 # Iterate through each position in the strings up to the length of the shortest string
for k in range(len(min_len_str)):

    # Consider substrings of decreasing length at position i
    for j in range(len(min_len_str) + 1, k-2, -1):

        # Extract the substring from the first string
        substring = dna_strs[0][k:j+1]
        print(substring)
        # Check if the substring is present in all other strings
        if all(substring in s for s in dna_strs[1:]):

            # Update the result if the current substring is longer
            if len(substring) > len(result):
                result = substring




