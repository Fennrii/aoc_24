def to_ints(line) -> list[int]:
    for i in range(len(line)):
        line[i] = int(line[i])
    return line

def safety_check(line):
    line = to_ints(line)
    increase = 2
    # initial keys
    last=line[0]
    for i in range(len(line)-1):
        curr = line[i+1]
        diff = last-curr
        if abs(diff)>3:
            return False
        if increase == 2:
            if diff == 0:
                return False
            elif diff < 0:
                increase = True
            else:
                increase = False
        else:
            if increase and diff > 0:
                return False
            elif not increase and diff < 0:
                return False
            elif diff == 0:
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

def to_ints(line) -> list[int]:
    for i in range(len(line)):
        line[i] = int(line[i])
    return line

def buffer_check(line, buffered):
    if buffered:
        return 0
    result_list = []
    for i in range(len(line)):
        tmpline = line.copy()
        tmpline.pop(i)
        result_list.append(safety_check(tmpline,True))
    if sum(result_list)>0:
        return 1
    else:
        return 0

def safety_check(line, buffered = False):
    line = to_ints(line)
    increase = 2
    # initial keys
    last=line[0]
    for i in range(len(line)-1):
        curr = line[i+1]
        diff = last-curr
        if abs(diff)>3:
            # print("diff > 3")
            return buffer_check(line,buffered)
        if increase == 2:
            if diff == 0:
                # print("diff = 0")
                return buffer_check(line,buffered)
            elif diff < 0:
                increase = True
            else:
                increase = False
        else:
            if increase and diff > 0:
                # print("Wrong Dir")
                return buffer_check(line,buffered)
            elif not increase and diff < 0:
                # print("Wrong Dir")
                return buffer_check(line,buffered)
            elif diff == 0:
                # print("diff = 0")
                return buffer_check(line,buffered)
        last = curr
    return 1

safety_list = []
for line in file:
    line = line.strip('\n')
    line_arry = line.split(' ')
    safety = safety_check(line_arry)
    safety_list.append(safety)

print(sum(safety_list))
# print(len(file))
