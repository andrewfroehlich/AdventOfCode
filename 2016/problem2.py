
keypad = [[1,2,3],[4,5,6],[7,8,9]]
r = c = 1
code = []
for line in open("Resources/input2.txt"):
    for d in line.strip():
        if d == "U":
            r = r-1 if r > 0 else 0
        elif d == "D":
            r = r+1 if r < 2 else 2
        elif d == "L":
            c = c-1 if c > 0 else 0
        else: #"R"
            c = c+1 if c < 2 else 2
    code.append(str(keypad[r][c]))
print("Part 1:","".join(code))

keypad2 = [["X","X","X","X","X","X","X"],
    ["X","X","X","1","X","X","X"],
    ["X","X","2","3","4","X","X"],
    ["X","5","6","7","8","9","X"],
    ["X","X","A","B","C","X","X"],
    ["X","X","X","D","X","X","X"],
    ["X","X","X","X","X","X","X"]]
r = 3
c = 1
code = []
for line in open("Resources/input2.txt"):
    for d in line.strip():
        prev_r,prev_c = r,c
        if d == "U":
            r = r-1
        elif d == "D":
            r = r+1
        elif d == "L":
            c = c-1
        else: #"R"
            c = c+1
        if keypad2[r][c] == "X":
            r,c = prev_r,prev_c
    code.append(keypad2[r][c])
print("Part 2:","".join(code))