open_file = open('C:/Users/shubh/Desktop/data.txt')

count=0
min_height=10000
max_height=0
sum_height=0
min_weight=10000
max_weight=0
sum_weight=0
min_bmi=10000
max_bmi=0
sum_bmi=0
bmi = 0

for line in open_file:
    line = line.strip()
    e_strip = line.split()
    name = e_strip[0]
    #print(name)
    
    if count>0:
        height = float(e_strip[1])
        weight = float(e_strip[2])
        bmi = weight/height**2
        if bmi<min_bmi:
            min_bmi = bmi
        if bmi> max_bmi:
            max_bmi = bmi
        sum_bmi = sum_bmi + bmi
        avg_bmi = sum_bmi/8
        
        if height<min_height:
            min_height = height
        if height>max_height:
            max_height = height
        sum_height = sum_height+height
        avg_height = sum_height/8
        if weight<min_weight:
            min_weight = weight
        if weight>max_weight:
            max_weight = weight
        sum_weight = sum_weight+weight
        avg_weight = sum_weight/8
        print(line,"{:10.2f}".format(bmi))
    else:
        count = count+1
        print(line,"BMI")

print()
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format('Average',avg_height,avg_weight,avg_bmi))
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format('Max',max_height,max_weight,max_bmi))
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format('Min',min_height,min_weight,min_bmi))




        
            
    
        