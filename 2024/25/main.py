def process_input():
    locks,keys = list(),list()
    for item in open("input.txt").read().split("\n\n"):
        item_lines = item.split("\n")
        current = [-1]*5
        is_lock = (item_lines[0] == "#####")
        for row in (range(1,7) if is_lock else range(6,-1,-1)):
            for col in range(5):
                if item_lines[row][col] == "." and current[col] == -1:
                    current[col] = (row-1) if is_lock else (5-row)
        (locks if is_lock else keys).append( tuple(current) )
    return locks,keys

def fit(lock, key):
    return all(l + k <= 5 for l, k in zip(lock, key))

def part1():
    locks,keys = process_input()
    return sum(fit(lock, key) for lock in locks for key in keys)

if __name__ == "__main__":
    print("Part 1:",part1())