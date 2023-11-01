# This is my solution to Complementing a Strand of DNA

f = open("/Users/m13477cc/Documents/demofile.txt", "r")
input = f.readline()
rev = input[::-1]
mapping_table = str.maketrans({'A':'T', 'T':'A', 'G':'C', 'C':'G'})
output = rev.translate(mapping_table)
print(output)