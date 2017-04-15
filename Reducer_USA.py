sorted = open("mapper_output_sorted_USA.txt","r")   
results = open("reducer_output_USA.txt", "w")   

totalGold = 0       
oldSport = None    


lines = sorted.readlines()
for line in lines:
    datalist = line.strip().split("\t")
    if len(datalist) != 2:  # if bad input line
       continue             # ignore it

    thisSport, thisGold = datalist  # read into variables

   

    if oldSport and oldSport != thisSport:        
        results.write("{0}\t{1}\n".format(oldSport, totalGold))
        oldSport = thisSport;
        totalGold = 0

    oldSport = thisSport            
    totalGold += int(thisGold)




if oldSport != None: 
    results.write("{0}\t{1}\n".format(oldSport, totalGold))

sorted.close() 
results.close()