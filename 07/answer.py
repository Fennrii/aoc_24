def concat(val1,val2):
    return int(f"{val1}{val2}")
def check_solution(answer, val):
    return answer == val

class Solution:
    ans = []
    ds = []
    

    def recurPermute(self, nums):
        if len(self.ds) == nums:
            self.ans.append(self.ds.copy())
            return
        for char in ["m","a","c"]:
            self.ds.append(char)
            self.recurPermute(nums)
            self.ds.pop()

    def permute(self,array):
        self.ans = []
        self.ds = []
        self.recurPermute(len(array)-1)
        return self.ans


NUM_OPS = 2
with open('input','r') as f:
    lines = list(map(lambda n: n.strip('\n'),f.readlines()))

answers = []
inputs = []
for line in lines:
    tmp = line.split(' ')
    answers.append(int(tmp.pop(0).strip(':')))
    inputs.append(list(map(lambda n: int(n),tmp)))


# The amount of different signs would be number of inputs - 1 * number of operations
# One way I can change the operations is by using modulus on the index
resultlist = []
obj = Solution()
for k in range(len(inputs)):
    testa = answers[k]
    ina = inputs[k]

    sums = obj.permute(ina)

    for i in range(len(sums)):
        result = ina[0]
        for j in range(len(sums[i])):
            if sums[i][j] == "m":
                result*=ina[j+1]
            elif sums[i][j] == "a":
                result+=ina[j+1]
            elif sums[i][j] == "c":
                result = concat(result,ina[j+1])
    
        if check_solution(testa,result):
            print(f"{testa} == {result}")
            resultlist.append(result)
            break
result = 0
for i in set(resultlist):
    result+= i
print(result)
