dance_moves = open("Resources/input16.txt").readline().strip().split(",")

def dance(string):
    programs = list(string)
    for move in dance_moves:
        if move[0:1] == "s":
            shift = int(move[1:])
            programs = programs[-shift:]+programs[:-shift]
        elif move[0:1] == "x":
            i1,i2 = move[1:].split("/")
            temp = programs[int(i1)]
            programs[int(i1)] = programs[int(i2)]
            programs[int(i2)] = temp
        else: #"p"
            c1,c2 = move[1:].split("/")
            i1 = programs.index(c1)
            i2 = programs.index(c2)
            programs[i1] = c2
            programs[i2] = c1
    return "".join(programs)

input_str = "abcdefghijklmnop"
print("Part 1:",dance(input_str))

#find a loop back to the original string
string = input_str
dance_loop = 0
while True:
    string = dance(string)
    dance_loop += 1
    if string == input_str:
        break
#mod 1,000,000,000 by the loop size to see how many times to run
for _ in range(1000000000%dance_loop):
    string = dance(string)
print("Part 2:", string)