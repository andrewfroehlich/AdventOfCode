east_cuc = set()
south_cuc = set()
raw_input = open("input25.txt").readlines()
max_lines = len(raw_input)
max_chars = len(raw_input[0].strip())
for line in range(max_lines):
    for char in range(max_chars):
        if raw_input[line][char] == ">":
            east_cuc.add( (line,char) )
        elif raw_input[line][char] == "v":
            south_cuc.add( (line,char) )

steps_completed = 0
while True:
    moves = 0
    moved_set = set()
    for c in east_cuc:
        moved_coord = (c[0], (c[1]+1)%max_chars)
        if moved_coord not in east_cuc and moved_coord not in south_cuc:
            moved_set.add(moved_coord)
            moves += 1
        else:
            moved_set.add(c)
    east_cuc = moved_set.copy()
    moved_set.clear()
    for c in south_cuc:
        moved_coord = ((c[0]+1)%max_lines, c[1])
        if moved_coord not in east_cuc and moved_coord not in south_cuc:
            moved_set.add(moved_coord)
            moves += 1
        else:
            moved_set.add(c)
    south_cuc = moved_set.copy()
    moved_set.clear()
    steps_completed += 1
    if moves == 0:
        print("Part 1: Step",steps_completed)
        break
    