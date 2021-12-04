def checkForBingo(board, i, j):
    bingo = True
    for x in range(len(board)):
        if board[x][j] != -1:
            bingo = False
            break
    if not bingo:
        for y in range(len(board[i])):
            if board[i][y] != -1:
                return False
    return True

def getScore(board, lastNum):
    s = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            s += 0 if board[i][j] == -1 else int(board[i][j])
    return s * int(lastNum)

def part1():
    with open("input4.txt") as f:
        lines = f.read().splitlines()
    lineIndex = 0
    #Set up input structures
    numbers = lines[lineIndex].split(",")
    boards = []
    lineIndex += 2
    while len(lines) > lineIndex:
        board = []
        for i in range(5):
            board.append(lines[lineIndex+i].split())
        boards.append(board)
        lineIndex += 6
    #Play Bingo
    for num in numbers:
        for board in boards:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == num:
                        board[i][j] = -1 #mark
                        if checkForBingo(board, i, j):
                            return getScore(board, num)
    return -1

def part2():
    with open("input4.txt") as f:
        lines = f.read().splitlines()
    lineIndex = 0
    #Set up input structures
    numbers = lines[lineIndex].split(",")
    boards = []
    lineIndex += 2
    while len(lines) > lineIndex:
        board = []
        for i in range(5):
            board.append(lines[lineIndex+i].split())
        boards.append(board)
        lineIndex += 6
    #Play Bingo
    for num in numbers:
        noBingoBoards = []
        for board in boards:
            bingo = False
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == num:
                        board[i][j] = -1 #mark
                        if checkForBingo(board, i, j):
                            if len(boards) == 1:
                                return getScore(board, num)
                            bingo = True
            if not bingo:
                noBingoBoards.append(board)
        boards = noBingoBoards
    return -1

print("Part 1:", part1())
print("Part 2:", part2())