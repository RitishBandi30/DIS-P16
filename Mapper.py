f = open("dataset.txt","r")  # open file, read-only raw data
o = open("mapper_output.txt", "w") # open file, write - just our key, value pairs
for line in f:  
    data = line.strip().split("		") 
  
    if len(data) == 3:
        country, gold, silver = data
        o.write("{0}\t{1}\n".format(country, gold))
f.close()
o.close()
n = open("mapper_output.txt","r");
s = open("mapper_output_sorted.txt","w")
line = n.readlines()
line.sort()
for l in line:
 s.write(l)
n.close()
s.close()

