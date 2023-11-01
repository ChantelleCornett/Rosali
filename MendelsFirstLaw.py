# This is my solution to Medel's First Law
import numpy as np

f = open("/Users/m13477cc/Documents/demofile.txt", "r")
input = f.readline()

input_list = input.split()
int_list = []

for num in input_list:
    int_list.append(int(num))

# first num is indivs homozygous for a factor
# second num is for heterozygous
# 3rd is for homozygous recessive

# prob 2 randomly selected organisms will produce individual
# with dominant allele

# will produce someone with dominant if 
pop_num = int_list[0] + int_list[1] + int_list[2]
Dho_p, Dhe_p, R_p = int_list[0]/pop_num, int_list[1]/pop_num, int_list[2]/pop_num

sample = np.random.choice([1,2,3], 2, replace = False, p=[Dho_p, Dhe_p, R_p])

print(sample[1])
print(sample)