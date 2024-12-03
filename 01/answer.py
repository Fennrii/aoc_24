## Part 1
import os

arr1 = []
arr2 = []
diff_arr = []

with open("input","r") as f:
    lines = f.readlines()
for line in lines:
    tmp = line.split("   ")
    arr1.append(int(tmp[0]))
    arr2.append(int(tmp[1]))

arr1.sort()
arr2.sort()
for i in range(len(arr1)):
    diff_arr.append(abs(arr1[i]-arr2[i]))
# print(sum(diff_arr))
## Part 2


def calc_simularity_score(llnum, num_apps):
    return llnum * num_apps
    

myset = set(arr1)
mydict = dict.fromkeys(myset, 0)

for i in arr2:
    if i in myset:
        mydict[i]+=1
    # mydict[24396]=mydict[24396]+1

fullscore = 0
for i in myset:
    fullscore += calc_simularity_score(i,mydict[i])
print(fullscore)

