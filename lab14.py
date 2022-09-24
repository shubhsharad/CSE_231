# Simple bar graph
import csv
import pylab
fp = open("STC_2014_STC005.csv","r")
#values = percent_list
#indices = [i for i in range(len(values))]
csvreader = csv.reader(fp)
next(csvreader,None)
next(csvreader,None)
next(csvreader,None)
empty_list = []
percent_list = []
for line in csvreader:
    state_name = line[2]
    empty_list.append(state_name)
    total_taxes = int(line[3])
    sgrt = int(line[5])
    percent = (sgrt/total_taxes) *100 
    percent_list.append(percent)
# figsize adjusts the entire figure dimensions -- place before other pylab instructions
pylab.figure(figsize=(10,5))
values = percent_list
indices = [i for i in range(len(values))]
pylab.title("Ratio of Sales Tax to All state taxes by state")
pylab.xlabel('State')
pylab.ylabel('Ratio')
print(empty_list)

# 1. These next two lines put labels on the x axis, one at each of the indices
names = empty_list
pylab.xticks(indices,names,rotation=90)

# 2. What does ylim do?
pylab.ylim([0,100])


# simple plot
#pylab.bar(indices,values)

# 3. more complex plot especially when combined with xticks line above
mybarwidth = 0.5    # default is 0.8; you might want it smaller
pylab.bar(indices,values,mybarwidth,align='center')
