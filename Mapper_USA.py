import re
f = open("dataset_USA.txt","r")  # open file, read-only raw data
o = open("mapper_output_USA.txt", "w") # open file, write - just our key, value pairs
for line in f:  
    data = line.strip().split("\t")

    print data
  
    if len(data) == 5:
        country, sport, gold, silver, bronze = data
        o.write("{0}\t{1}\n".format(sport, gold))
f.close()
o.close()
n = open("mapper_output_USA.txt","r");
s = open("mapper_output_sorted_USA.txt","w")
line = n.readlines()
line.sort()
for l in line:
 s.write(l)
n.close()
s.close()

