
xmas = "XMAS"

def find_word(array,word,wordindx,row,col,direction):
    rows = len(array)
    cols = len(array[0])
    if wordindx >= len(word):
        # print("\nTrue")
        return 1

    if (0 > row or row >= rows) or (0 > col or col >= cols):
        # print(f"\nFalse - [{row}][{col}] out of bounds [{len(array)-1}][{len(array[0])-1}]")
        return 0
    # print(array[row][col],end='')
    if array[row][col] == word[wordindx]:
        return find_word(array,word,wordindx+1,row+direction[0],col+direction[1],direction)
    # print(f"\nFalse - {array[row][col]} != {word[wordindx]}")
    return 0

def search_all_dirs(array,word,row,col):
    result = 0
    directions = [
            (1,0),(0,1),(-1,0),(0,-1),
            (1,1),(1,-1),(-1,1),(-1,-1)
            ]
    for direction in directions:
        result += find_word(array,word,0,row,col,direction)
    return result

with open('input','r') as f:
    lines = list(map(lambda n: n.strip('\n'),f.readlines()))


found_words = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == xmas[0]:
            # print(f"[{i}][{j}]")
            found_words += search_all_dirs(lines,xmas,i,j)


print(found_words)
mas = "MAS"
def find_x_mas(array, word, row, col):
    result = 0
    directions = [
            (1,1),(1,-1),(-1,-1),(-1,1)
            ]
    rev_directions = [
            (-1,-1),(-1,1),(1,1),(1,-1)
            ]
    count = 0
    for dirindx in range(len(directions)):
        regdir = directions[dirindx]
        invdir = rev_directions[dirindx]
        count+= find_word(array,word,0,row+regdir[0],col+regdir[1],invdir)
    if count == 2:
        return 1
    return 0
found_words = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        found_words += find_x_mas(lines,mas,i,j)
print(found_words)
