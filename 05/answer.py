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
# The order is for X|Y X cannot follow Y
# Creates a dict of Y's that contain a list of X's
for i in rules:
    tmp = i.split('|')
    req_dict[tmp[0]].append(tmp[1])

for i in range(len(prints)):
    prints[i] = prints[i].split(',')
result_list = []
for i in prints:
    result_list.append(check_order(i,req_dict))

result = 0
for i in range(len(result_list)):
    if result_list[i]:
        result += int(prints[i][int(len(prints[i])/2)])
print(result)
