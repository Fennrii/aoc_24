import re

# The idea is the treat the string as an array of Chars and test each char until
# it gets to either the closing paranthesis or 12 chars long

def get_mul_results(file,_mul_starts) -> list[int]:
    res_list = []
    for i in _mul_starts:
        nums = file[i[0]:i[1]].strip('mul()').split(',')
        fi = int(nums[0])
        se = int(nums[1])
        if ((fi < 0 or fi >= 1000) or (se < 0 or se >= 1000)):
            continue
        else:
            res_list.append(fi*se)
    return res_list



regex = r"mul\(\d{1,3},\d{1,3}\)"
with open("input","r") as f:
    file = f.read()
mul_starts = [m.span() for m in re.finditer(regex ,file)]
res_list = get_mul_results(file, mul_starts)
print(sum(res_list))

# To filter the do's and don'ts I will use another regex and only get the starts,
# Then loop through the list comparing do's and don'ts 

def get_mul_results(file,_mul_starts) -> int:
    nums = file[_mul_starts[0]:_mul_starts[1]].strip('mul()').split(',')
    fi = int(nums[0])
    se = int(nums[1])
    if ((fi < 0 or fi >= 1000) or (se < 0 or se >= 1000)):
        return 0
    return fi*se

def get_do_zones(do_starts, dont_starts, mul_starts):
    _res_list = []
    do = True
    curr_do_index = 0
    max_do_index = len(do_starts)-1
    curr_dont_index = 0
    max_dont_index = len(dont_starts)-1
    print("do = True")
    print(f"Start do = {do_starts[curr_do_index]}, Start dont = {dont_starts[curr_dont_index]}")
    for i in mul_starts:
        if do:
            if dont_starts[curr_dont_index]<=i[0]:
                do = False
                print(f"{dont_starts[curr_dont_index]} < {i[0]}: do = False")
                if curr_dont_index < max_dont_index:
                    curr_dont_index+=1
                while do_starts[curr_do_index]<=i[0] and curr_do_index != max_do_index:
                    curr_do_index+=1
                    print(f"New do = {do_starts[curr_do_index]}")
                print(f"New do = {do_starts[curr_do_index]}")
            else:
                _res_list.append(get_mul_results(file,i))
        else:
            if do_starts[curr_do_index]<=i[0]:
                do = True
                print(f"{do_starts[curr_do_index]} < {i[0]}: do = True")
                if curr_do_index < max_do_index:
                    curr_do_index+=1
                while dont_starts[curr_dont_index]<=i[0] and curr_dont_index != max_dont_index:
                    curr_dont_index+=1
                    print(f"New dont = {dont_starts[curr_dont_index]}")
                print(f"New dont = {dont_starts[curr_dont_index]}")
            else:
                _res_list.append(0)
    return _res_list


def bruit_force(file, do_starts, dont_starts, mul_starts):
    _res_list = []
    do = True
    starts = [m[0] for m in mul_starts]
    for i in range(len(file)):
        if i in do_starts:
            do = True
        if i in dont_starts:
            do = False
        if i in starts and do:
            _res_list.append(get_mul_results(file,mul_starts[starts.index(i)]))
    return _res_list
    

do_starts = [m.start() for m in re.finditer(r'do\(\)', file)]
dont_starts = [m.start() for m in re.finditer(r"don't\(\)", file)]
res_list = bruit_force(file,do_starts,dont_starts,mul_starts)
print(sum(res_list))
