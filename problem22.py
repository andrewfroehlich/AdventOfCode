class Cube:
    def __init__(self, *args): #either string to parse, or all 6 coords passed in
        if len(args) > 1:
            self.on = True
            self.x_range = (int(args[0]),int(args[1]))
            self.y_range = (int(args[2]),int(args[3]))
            self.z_range = (int(args[4]),int(args[5]))
        else:
            input_str = args[0]
            self.on = (input_str[0:2] == "on")
            raw_coords = input_str.split(',')
            raw_x_range = raw_coords[0].split("=")[1].split("..")
            self.x_range = (int(raw_x_range[0]),int(raw_x_range[1]))
            raw_y_range = raw_coords[1].split("=")[1].split("..")
            self.y_range = (int(raw_y_range[0]),int(raw_y_range[1]))
            raw_z_range = raw_coords[2].split("=")[1].split("..")
            self.z_range = (int(raw_z_range[0]),int(raw_z_range[1]))  

def part1(cubes):
    on_cubes = set()
    for c in cubes:
        for x in range(max(-50,c.x_range[0]), min(50, c.x_range[1])+1):
            for y in range(max(-50,c.y_range[0]), min(50, c.y_range[1])+1):
                for z in range(max(-50,c.z_range[0]), min(50, c.z_range[1])+1):
                    if c.on:
                        on_cubes.add( (x,y,z) )
                    else:
                        on_cubes.remove( (x,y,z) )
    return len(on_cubes)

def part2(input_cubes):
    output_cubes = []
    for c in input_cubes:
        for cube_i in range(len(output_cubes)):
            cur = output_cubes[cube_i]
            if c.x_range[0] > cur.x_range[1] or c.x_range[1] < cur.x_range[0] or c.y_range[0] > cur.y_range[1] or c.y_range[1] < cur.y_range[0] or c.z_range[0] > cur.z_range[1] or c.z_range[1] < cur.z_range[0]: #no overlap, no need to split
                continue
            output_cubes[cube_i] = None
            if c.x_range[0] > cur.x_range[0]:
                output_cubes.append(Cube(cur.x_range[0], c.x_range[0] - 1, cur.y_range[0], cur.y_range[1], cur.z_range[0], cur.z_range[1]))
            if c.x_range[1] < cur.x_range[1]:
                output_cubes.append(Cube(c.x_range[1] + 1, cur.x_range[1], cur.y_range[0], cur.y_range[1], cur.z_range[0], cur.z_range[1]))
            if c.y_range[0] > cur.y_range[0]:
                output_cubes.append(Cube(max(cur.x_range[0], c.x_range[0]), min(cur.x_range[1], c.x_range[1]), cur.y_range[0], c.y_range[0] - 1, cur.z_range[0], cur.z_range[1]))
            if c.y_range[1] < cur.y_range[1]:
                output_cubes.append(Cube(max(cur.x_range[0], c.x_range[0]), min(cur.x_range[1], c.x_range[1]), c.y_range[1] + 1, cur.y_range[1], cur.z_range[0], cur.z_range[1]))
            if c.z_range[0] > cur.z_range[0]:
                output_cubes.append(Cube(max(cur.x_range[0], c.x_range[0]), min(cur.x_range[1], c.x_range[1]), max(cur.y_range[0], c.y_range[0]), min(cur.y_range[1], c.y_range[1]), cur.z_range[0], c.z_range[0] - 1))
            if c.z_range[1] < cur.z_range[1]:
                output_cubes.append(Cube(max(cur.x_range[0], c.x_range[0]), min(cur.x_range[1], c.x_range[1]), max(cur.y_range[0], c.y_range[0]), min(cur.y_range[1], c.y_range[1]), c.z_range[1] + 1, cur.z_range[1]))
        if c.on: #only if "on", add the actual cube "overlap"
            output_cubes.append(Cube(min(c.x_range[0], c.x_range[1]), max(c.x_range[0], c.x_range[1]), min(c.y_range[0], c.y_range[1]), max(c.y_range[0], c.y_range[1]), min(c.z_range[0], c.z_range[1]), max(c.z_range[0], c.z_range[1])))
        output_cubes = [cube for cube in output_cubes if cube is not None]
    # calculate the total volume of all the cubes left
    part2 = 0
    for c in output_cubes:
        part2 += (c.x_range[1] - c.x_range[0] + 1) * (c.y_range[1] - c.y_range[0] + 1) * (c.z_range[1] - c.z_range[0] + 1)
    return part2

cubes = [Cube(c) for c in open("input22.txt").read().strip().split('\n')]
print("Part 1:", part1(cubes))
print("Part 2:", part2(cubes))
