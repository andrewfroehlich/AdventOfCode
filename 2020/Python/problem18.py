from collections import deque

values = deque()
operations = deque()

def runOperations():
    global values,operations
    while len(operations) > 0 and operations[0] != "(":
        operation = operations.popleft()
        if operation == "+":
            values.appendleft(values.popleft() + values.popleft())
        else: #operation == "*"
            values.appendleft(values.popleft() * values.popleft())

def runPlus():
    global values,operations
    while len(operations) > 0 and operations[0] == "+":
        operations.popleft()
        values.appendleft(values.popleft() + values.popleft())
    
def run(part2):
    global values,operations
    values = deque()
    operations = deque()
    val = 0
    for line in open("../Resources/problem18.txt"):
        for c in line.strip():
            if c == " ": 
                continue
            if c.isnumeric():
                values.appendleft(int(c))
                if part2:
                    runPlus()
                else:
                    runOperations()
            elif c in ("+","*","("):
                operations.appendleft(c)
            else: #c == ")"
                runOperations()
                operations.popleft() #pop the (
                if part2:
                    runPlus()
                else:
                    runOperations()
        runOperations()
        val += values.popleft()
    return val

print("Part 1:",run(False))
print("Part 2:",run(True))