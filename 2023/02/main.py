def part1(red_max=12,green_max=13,blue_max=14):
    sum1 = 0
    game_num = 1
    cube_max = {"red":red_max,"green":green_max,"blue":blue_max}
    for line in open("input.txt"):
        possible = True
        reveals = line.strip().split(": ")[1].split("; ")
        for reveal in reveals:
            cube_defs = reveal.split(", ")
            for cube_def in cube_defs:
                num,color = cube_def.split()
                if cube_max[color] < int(num):
                    possible = False
                    break
            if not possible:
                break
        if possible:
            sum1 += game_num
        game_num += 1
    return sum1

def part2():
    sum2 = 0
    for line in open("input.txt"):
        cube_max = {"red":0,"green":0,"blue":0}
        reveals = line.strip().split(": ")[1].split("; ")
        for reveal in reveals:
            cube_defs = reveal.split(", ")
            for cube_def in cube_defs:
                num,color = cube_def.split()
                cube_max[color] = max(cube_max[color],int(num))
        sum2 += cube_max["red"]*cube_max["green"]*cube_max["blue"]
    return sum2

if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())