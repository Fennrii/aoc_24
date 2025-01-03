import sys
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
sys.setrecursionlimit(20000)
directions = [
        (0,-1),(-1,0),(0,1),(1,0)
        ]
def show_locale(array,loc, arrows, arcols):
    tmparray = [['█','█','█','█','█'],
                ['█','█','█','█','█'],
                ['█','█','█','█','█'],
                ['█','█','█','█','█'],
                ['█','█','█','█','█']]
    tmploc = (2,2)
    
    x,y = loc
    tx,ty = tmploc
    for i in directions:
        iy,ix=i
        if 0<=y+iy<arcols and 0<=x+ix<arrows:
            tmparray[ty+iy][tx+ix] = array[y+iy][x+ix]
        for j in directions:
            jy,jx=j
            if 0<=y+iy+jy<arcols and 0<=x+ix+jx<arrows:
                tmparray[ty+jy+iy][tx+jx+ix] = array[y+jy+iy][x+jx+ix]
    for i in tmparray:
        tmpstr = "".join(i)
        print(tmpstr)

def is_subset(big,sub):
    size = len(big)
    if len(sub)>2:
        return False
    if len(sub)<2:
        return False
    for _i in range(size-1):
        if big[_i]==sub[0] and big[_i+1]==sub[1]:
            return True
    return False

def guard_move(array,loc,_directions,_direction,obj_list,last_two):
    cols = len(array)
    rows = len(array[0])
    x,y = loc
    dx,dy = _directions[_direction]

    # array[y][x] = "^"
    # show_locale(array,loc, rows, cols)
    array[y][x] = 'X'
    if (x+dx < 0 or x+dx >= rows) or (y+dy < 0 or y+dy >= cols):
        return array,'','','','',True,False
    if array[y+dy][x+dx] == '#':
        next_loc = (x+dx,y+dy)
        newtwo = []
        if len(last_two) > 0:
            newtwo.append(last_two[-1])
        newtwo.append(next_loc)
        if is_subset(obj_list,newtwo):
            print(f"FOUND: \n{obj_list}\n{newtwo}")
            return array,'','',obj_list,'',True,True
        obj_list.append(next_loc)
        if _direction == NORTH:
            _direction = WEST
        else:
            _direction -= 1
        dx,dy = _directions[_direction]
    else:
        newtwo = last_two
    if not 'newtwo' in locals():
        newtwo = last_two
    next_loc = (x+dx,y+dy)
    return array,next_loc,_direction,obj_list,newtwo,False,False

def find_start(array):
    cols = len(array)
    rows = len(array[0])
    for i in range(cols):
        for j in range(rows):
            if array[i][j] == '^':
                return (j,i)

def same_list(list1, list2):
    col1 = len(list1)
    col2 = len(list2)
    if col1 != col2:
        return True
    for col in range(col1):
            if list1[col] != list2[col]:
                return True
    print(f"These are the same\n{list1}\n{list2}")
    return False

newlines = []
with open('input','r') as f:
    lines = list(map(lambda n: n.strip('\n'),f.readlines()))
for line in lines:
    tmp = []
    for char in line:
        tmp.append(char)
    newlines.append(tmp)
start_pos = find_start(newlines)
direction = NORTH
done = False
next_pos = start_pos
hit_list = []
lasttwo = []
maps = newlines.copy()
while not done:
    maps, next_pos, direction,hit_list,lasttwo, done, found = guard_move(maps,next_pos,directions,direction,hit_list,lasttwo)
result = 0
if found:
    print("FOUND")
for i in maps:
    for j in i:
        if j == "X":
            result+=1
print(result)




result = 0
prev_hit_list = []
count = 0
for row in range(len(maps)):
    for col in range(len(maps[0])):
        
        if maps[row][col] == "X":
            direction = NORTH
            done = False
            found = False
            next_pos = start_pos
            hit_list = []
            lasttwo = []
            tmparr = []
            tmparr = newlines.copy()
            tmparr[col][row]="#"
            print(f"placed [{col}][{row}]")
            while not done:
                tmparr, next_pos, direction,hit_list,lasttwo, done, found= guard_move(tmparr,next_pos,directions,direction,hit_list,lasttwo)
            if found and same_list(hit_list, prev_hit_list):
                result += 1
                print(result)
            else:
                # pass
                print(f"Fail : {count}")
            prev_hit_list = hit_list
            count += 1
print(result)
