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
