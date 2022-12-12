from collections import deque

class Monkey:
    def __init__(self, items, op_sign, op_num, div, true_target, false_target):
        self.items = items
        self.op_sign = op_sign
        self.op_num = op_num
        self.div = div
        self.true_target = true_target
        self.false_target = false_target
        self.inspects = 0
    def operation(self, part1, mega_div):
        if len(self.items) > 0:
            self.inspects += 1
            item = self.items.popleft()
            num = (item if self.op_num == "old" else int(self.op_num))
            item = (item * num) if self.op_sign == "*" else (item + num)
            if part1:
                item = item//3
            return (self.true_target, item % mega_div) if (item % self.div == 0) else (self.false_target, item % mega_div)
        return -1,-1

def run(part1, rounds):
    monkeys = []
    mega_div = 1
    lines = open("input11.txt").readlines()
    for i in range(0, len(lines), 7):
        items = deque( [int(d) for d in lines[i+1].split(": ")[1].split(", ")] )
        op_split = lines[i+2].split()
        monkey = Monkey(items, op_split[-2], op_split[-1], int(lines[i+3].split()[-1]), int(lines[i+4].split()[-1]), int(lines[i+5].split()[-1]))
        mega_div = mega_div * monkey.div
        monkeys.append(monkey)
    
    for r in range(rounds):
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            while len(monkey.items) > 0:
                target, item = monkey.operation(part1, mega_div)
                monkeys[target].items.append(item)
    inspects = [monkey.inspects for monkey in monkeys]
    inspects.sort()
    return inspects[-1]*inspects[-2]

print("Part 1:",run(True,20))
print("Part 2:",run(False,10000))