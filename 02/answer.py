def safety_check(line):
    last=int(line[0])
    curr=int(line[1])
    if abs(curr-last)>3:
        return False
    if curr>last:
        increase = True
    elif curr<last:
        increase = False
    else:
        return False
    last = curr
    for i in range(len(line)-2):
        curr = int(line[i+2])
        if increase and curr<=last:
            # print(f"Last: {last}, Curr: {curr}, increasing = {increase}")
            return False 
        elif not increase and curr>=last:
            print(f"Last: {last}, Curr: {curr}, increasing = {increase}")
            return False
        if abs(curr-last)>3:
            # print(f"Last: {last}, Curr: {curr}, increasing = {increase}")
            return False
        last = curr
    return True
with open("input","r") as f:
    file = f.readlines()

safety_list = []
for line in file:
    line = line.strip('\n')
    line_arry = line.split(' ')
    # print(line_arry)
    safety = safety_check(line_arry)
    # print(safety)
    safety_list.append(safety)

print(sum(safety_list))
