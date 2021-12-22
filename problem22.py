class Step:
    def __init__(self, input_str):
        self.on = (input_str[0:2] == "on")
        raw_coords = input_str.split(',')
        raw_x_range = raw_coords[0].split("=")[1].split("..")
        self.x_range = (int(raw_x_range[0]),int(raw_x_range[1]))
        raw_y_range = raw_coords[1].split("=")[1].split("..")
        self.y_range = (int(raw_y_range[0]),int(raw_y_range[1]))
        raw_z_range = raw_coords[2].split("=")[1].split("..")
        self.z_range = (int(raw_z_range[0]),int(raw_z_range[1]))  

steps = [Step(c) for c in open("input22.txt").read().strip().split('\n')]
on_cubes = set()
for s in steps:
    for x in range(max(-50,s.x_range[0]), min(50, s.x_range[1])+1):
        for y in range(max(-50,s.y_range[0]), min(50, s.y_range[1])+1):
            for z in range(max(-50,s.z_range[0]), min(50, s.z_range[1])+1):
                if s.on:
                    on_cubes.add( (x,y,z) )
                else:
                    on_cubes.remove( (x,y,z) )
print("Part 1:", len(on_cubes))