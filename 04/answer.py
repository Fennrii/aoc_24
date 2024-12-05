

xmas = ['X','M','A','S']
# print(word[0][1]='M')
# print(word[1][0]='Z')

def find_word(array,word,wordindx,row,col,direction):
    if wordindx >= len(word):
        print("\nTrue")
        return 1
    if row < 0 or col < 0:
        print("\nFalse - out of bounds")
        return 0
    if row >= len(array) or col >= len(array[0]):
        print("\nFalse - out of bounds")
        return 0
    row_offset = 0
    col_offset = 0
    match direction:
        case 1:
            row_offset = -1
            col_offset = -1
        case 2:
            row_offset = -1
        case 3:
            row_offset = -1
            col_offset = 1
        case 4:
            col_offset = -1
        case 5:
            col_offset = 1
        case 6:
            row_offset = 1
            col_offset = -1
        case 7:
            row_offset = 1
        case 8:
            row_offset = 1
            col_offset = 1
        case _:
            print(f"Direction {direction} not accepted")
            exit()
    if array[row][col] == word[wordindx]:
        print(array[row][col],end='')
        return find_word(array,word,wordindx+1,row+row_offset,col_offset+col_offset,direction)
    print(f"\nFalse - {array[row][col]} != {word[wordindx]}")
    return 0

def search_all_dirs(array,word,row,col):
    result = 0
    for _i in range(1,9):
        result += find_word(array,word,0,row,col,_i)
    return result

with open('input','r') as f:
    lines = f.readlines()


for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')

found_words = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == xmas[0]:
            found_words += search_all_dirs(lines,xmas,i,j)
            # print(lines[i][j])
            

print(found_words)
