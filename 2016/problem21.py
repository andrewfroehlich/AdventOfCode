def run(p, reverse):
    password = list(p)
    lines = open("Resources/input21.txt").readlines()
    if reverse:
        lines.reverse()
    for line in lines:
        if line[0:4] == "swap":
            _,swaptype,x,_,_,y = line.split()
            if swaptype == "position":
                temp = password[int(x)]
                password[int(x)] = password[int(y)]
                password[int(y)] = temp
            else: #"letter"
                x_pos = password.index(x)
                y_pos = password.index(y)
                password[x_pos] = y
                password[y_pos] = x
        elif line[0:4] == "move":
            _,_,x,_,_,y = line.split()
            if reverse:
                temp = x
                x = y
                y = temp
            letter_x = password.pop(int(x))
            password.insert(int(y), letter_x)
        elif line[0:7] == "reverse":
            _,_,x,_,y = line.split()
            x_pos = int(x)
            y_pos = int(y)
            while x_pos < y_pos:
                temp = password[x_pos]
                password[x_pos] = password[y_pos]
                password[y_pos] = temp
                x_pos += 1
                y_pos -= 1
        elif line[0:12] == "rotate based":
            x = line.strip().split()[-1]
            if not reverse:
                shift = (password.index(x) + 1 + (1 if password.index(x) >= 4 else 0)) % len(password)
                password = password[-shift:] + password[:-shift]
            else:
                password = password[1:] + password[:1]
                shifts = 1
                while not (password.index(x) >= 4 and ((password.index(x) + 2) % len(password)) == shifts % len(password)) and not (password.index(x) < 4 and (password.index(x) + 1) % len(password) == shifts % len(password)):
                    shifts += 1
                    password = password[1:] + password[:1]
        else: #rotate left/right
            _,direction,x,_ = line.split()
            shift = int(x) if direction=="left" else -int(x)
            if reverse:
                shift = -shift
            password = password[shift:] + password[:shift]
    return "".join(password)

print("Part 1:",run("abcdefgh",False))
print("Part 2:",run("fbgdceah",True))