
with open('input','r') as f:
    lines = list(map(lambda n: n.strip('\n'),f.readlines()))
antenna_set = set()
for line in lines:
    for char in line:
        if char != ".":
            antenna_set.add(char)

for i in antenna_set:
    print(i,end=" ")
print()
antinodes = [[[]*len(antenna_set)]*len(lines)]*len(lines[0])
print(antinodes)
for i in antenna_set:
    # Search through the lines array for instances of i
    # Then make a list of all the hits
    # Then calculate the line between hits if there are more than 1 hit
    # Then calculate the location of the antinodes and if they are within the array, append it to the antinodes list
    # TODO: make the antinodes list into a set since it is asking for uniqie antinodes
   pass
