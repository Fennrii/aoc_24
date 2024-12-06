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
def guard_move(array,loc,directions,direction):
    cols = len(array)
    rows = len(array[0])
    x,y = loc
    dx,dy = directions[direction]
    array[y][x] = "^"
    show_locale(array,loc, rows, cols)
    array[y][x] = 'X'
    if 0<x+dx>=rows or 0<y+dy>=cols:
        return array
    if array[y+dy][x+dx] == '#':
        if direction == NORTH:
            direction = WEST
        else:
            direction -= 1
        dx,dy = directions[direction]
    return guard_move(array,(x+dx,y+dy),directions,direction)

def find_start(array):
    cols = len(array)
    rows = len(array[0])
    for i in range(cols):
        for j in range(rows):
            if array[i][j] == '^':
                return (j,i)


newlines = []
with open('input','r') as f:
    lines = list(map(lambda n: n.strip('\n'),f.readlines()))
for line in lines:
    tmp = []
    for char in line:
        tmp.append(char)
    newlines.append(tmp)
start_pos = find_start(newlines)
map = guard_move(newlines,start_pos,directions,NORTH)
result = 0
for i in map:
    for j in i:
        if j == "X":
            result+=1
print(result)

