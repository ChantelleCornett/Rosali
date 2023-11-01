import pandas as pd

df = pd.read_csv("/Users/m13477cc/Documents/RNA_codon.txt", sep=" ", header=None,  
                 names=["RNA Codon", "Protein"]) 

dic = df.set_index("RNA Codon").T.to_dict("records")[0]

input = open("/Users/m13477cc/Documents/demofile.txt", "r").readline()

str_list = [input[i:i+3] for i in range(0, len(input), 3)]

# define function to replace string
def replace_string(s):
    return dic[s] if s in dic else s
 
# using map() function to solve problem
protein = list(map(replace_string, str_list))

pro_out = ''.join(protein)

if pro_out[-4:] == 'Stop':
    pro_out = pro_out[:-4]

print(pro_out)
 
