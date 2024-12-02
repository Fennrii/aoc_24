def safety_check(line):
    safe = True
    last=int(line[0])
    curr=int(line[1])
    if curr>last and abs(curr-last)<4:
        increase = True
    elif curr<last and abs(curr-last)<4:
        increase = False
    else:
        return False
    last = curr
    for i in range(len(line)-2):
        curr = int(line[i+2])
        if increase and curr<=last:
            safe = False 
        elif curr>=last:
            safe = False
        if abs(curr-last)>3:
            safe = False
        last = curr
    return safe
with open("input","r") as f:
    file = f.readlines()

safety_list = []
for line in file:
    line_arry = line.split(' ')
    safety_list.append(safety_check(line_arry))
print(sum(safety_list))
