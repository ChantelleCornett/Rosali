# This is my solution to Counting DNA Nucleotides

f = open("/Users/m13477cc/Documents/demofile.txt", "r")
f = f.readline()
Ac,Cc,Gc,Tc = f.count("A"),f.count("C"),f.count("G"),f.count("T")
print(str(Ac) + " " + str(Cc) + " " + str(Gc) + " " + str(Tc))
