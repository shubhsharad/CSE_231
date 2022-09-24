d = {}
def readfile(d):
    with open("data1.txt") as file_pointer:
        for each_line in file_pointer:
            name,score = each_line.split()
            if name == "Name" and score == "Score":
                continue
            if name in d:
                d[name] = d[name]+int(score)
            else:
                d[name] = int(score)
    with open("data2.txt") as file_pointer:
        for each_line in file_pointer:
            name,score = each_line.split()
            if name == "Name" and score == "Score":
                continue
            if name in d:
                d[name] = d[name]+int(score)
            else:
                d[name] = int(score) 
                

def print_results(d):
    print("{:10s} {:10s}".format("Name","Total"))
    for key,value in sorted(d.items()):
        
        print("{:10s} {:<10d}".format(key,value))

readfile(d)

print_results(d)