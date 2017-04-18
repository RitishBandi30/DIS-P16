sorted = open("mapper_output_sorted.txt","r")   
results = open("reducer_output.txt", "w")   

totalGold = 0       
oldCountry = None    


lines = sorted.readlines()
for line in lines:
    datalist = line.strip().split("\t")
    if len(datalist) != 2:  # if bad input line
       continue             # ignore it

    thisCountry, thisGold = datalist  # read into variables

   

    if oldCountry and oldCountry != thisCountry:        
        results.write("{0}\t{1}\n".format(oldCountry, totalGold))
        oldCountry = thisCountry;
        totalGold = 0

    oldCountry = thisCountry            
    totalGold += int(thisGold)




if oldCountry != None: 
    results.write("{0}\t{1}\n".format(oldCountry, totalGold))

sorted.close() 
results.close()

result = open("reducer_output.txt", "r") 

max = 0
r = result.readlines()
for l in r:
    data = l.strip().split("\t");
    if float(data[1]) > float(max):
        max = float(data[1])
            
print("The maximum number of gold medals is {0}".format(max))
result.close()
