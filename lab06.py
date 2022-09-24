fn = open("scores.txt","r")
st_list = []
e1_score = 0
e2_score = 0
e3_score = 0
e4_score = 0

for line in fn:
    data = line.split()
    #print(data)
    name = data[0]+data[1]
    #print(name)
    s1 = int(data[2])
    s2 = int(data[3])
    s3 = int(data[4])
    s4 = int(data[5])
    #print(s1,s2,s3,s4)    
    average = (s1+s2+s3+s4)/4
    st_list.append((name,s1,s2,s3,s4,average))
#print(st_list)
s_st_list = sorted(st_list)

print(s_st_list)
print("{:<20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}".format("Name","Exam1","Exam2","Exam3","Exam4","Mean"))
for s in s_st_list:
    print("{:20s}{:>6d}{:>6d}{:>6d}{:>6d}{:>10.2f}".format(s[0],s[1],s[2],s[3],s[4],s[5]))
    e1_score = e1_score+s[1]
    e2_score = e2_score+s[2]
    e3_score = e3_score+s[3]
    e4_score = e4_score+s[4]
    e1_mean = e1_score/5
    e2_mean = e2_score/5
    e3_mean = e3_score/5
    e4_mean = e4_score/5
print("{:20s}{:>6.1f}{:>6.1f}{:>6.1f}{:>6.1f}".format("Exam Mean",e1_mean,e2_mean,e3_mean,e4_mean,))
    
    
    


