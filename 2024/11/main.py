from functools import cache

@cache
def process_one_stone(blinks,stone):
    if blinks == 0:
        return 1
    if stone == 0:
        return process_one_stone(blinks-1,1)
    if len(str(stone))%2 == 0:
        cur_str = str(stone)
        return process_one_stone(blinks-1,int(cur_str[0:len(cur_str)//2])) + process_one_stone(blinks-1,int(cur_str[len(cur_str)//2:]))
    else:
        return process_one_stone(blinks-1,stone*2024)

def run(blinks):
    stones = [int(d) for d in open("input.txt").read().split()]
    return sum([process_one_stone(blinks,stone) for stone in stones])

if __name__ == "__main__":
    print("Part 1:",run(25))
    print("Part 1:",run(75))