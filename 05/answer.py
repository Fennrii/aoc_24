from collections import defaultdict

def check_rule(X,Y,rules):
    return X in rules[Y]

def check_order(order,rules):
    orlen = len(order)
    print(f"\n{order}")
    restring = "Numbers Checked: "
    for i in range(orlen): # Check each item in order
        restring+=f"{order[i]}: ("
        for j in range(i): # Check only next items
            restring+=f"{order[j]},"
            if check_rule(order[j], order[i], rules):
                print(restring)
                print(f"FAILED\n{order[j]} is in {order[i]}'s list: {rules[order[i]]}")
                return False
        restring+=f") "
    print(restring)
    print("PASSED")
    return True

rules = []
prints = []
with open('input','r') as f:
    lines = list(map(lambda n: n.strip('\n'),f.readlines()))
indx = 0
tmp = [rules,prints]
for line in lines:
    if line != '':
        tmp[indx].append(line)
    else:
        indx += 1

req_dict = defaultdict(list)
# The order is for X|Y Y cannot follow X
# Creates a dict of X's that contain a list of Y's
for i in rules:
    tmp = i.split('|')
    req_dict[tmp[0]].append(tmp[1])

for i in range(len(prints)):
    prints[i] = prints[i].split(',')
result_list = []
for i in prints:
    result_list.append(check_order(i,req_dict))

result = 0
incorrect_prints = []
for i in range(len(result_list)):
    if result_list[i]:
        result += int(prints[i][int(len(prints[i])/2)])
    else:
        incorrect_prints.append(prints[i])
print(result)


def order_prints(order,rules):
    sorted = False
    orlen = len(order)
    print(f"\n{order}")
    while not sorted:
        sort_made = False
        for i in range(orlen): # Check each item in order
            for j in range(i): # Check only next items
                if check_rule(order[j], order[i], rules):
                    print(f"FAILED\n{order[j]} is in {order[i]}'s list: {rules[order[i]]}")
                    print(f"Swapping {order[j]} and {order[i]}")
                    sorted =  False
                    sort_made = True
                    tmp = order[j]
                    order[j] = order[i]
                    order[i]=tmp
                    break
            if sort_made:
                break
        if not sort_made:
            sorted = True
    print(f"PASSED: Sorted list: {order}")
    return order
result = 0
for i in range(len(incorrect_prints)):
    incorrect_prints[i] = order_prints(incorrect_prints[i],req_dict)
    result += int(incorrect_prints[i][int(len(incorrect_prints[i])/2)])
print(result)
