from itertools import combinations

# create Moon class 
class Moon:
    def __init__(self, x, y, z):
        self.v_x, self.v_y, self.v_z = 0,0,0
        self.x = x
        self.y = y
        self.z = z
    def energy(self):
        return (abs(self.x)+abs(self.y)+abs(self.z)) * (abs(self.v_x)+abs(self.v_y)+abs(self.v_z))
        
# helper functions for debugging
def print_moon(m):
    print("<x={}, y={}, z={} | v_x={}, v_y={}, v_z={}>".format(m.x,m.y,m.z,m.v_x,m.v_y,m.v_z))
def print_moons(moons):
    for m in moons:
        print_moon(m)
    
def run_steps(moons, steps):
    pair_indices = list(combinations(range(len(moons)),2))
    # for each time step
    for time_step in range(1, steps+1):
        # update the velocity by applying gravity on each axis for each pair of moons
        for indices in pair_indices:
            m1,m2 = moons[indices[0]],moons[indices[1]]
            m1.v_x = m1.v_x + 1 if m2.x > m1.x else m1.v_x - 1 if m2.x < m1.x else m1.v_x
            m2.v_x = m2.v_x + 1 if m1.x > m2.x else m2.v_x - 1 if m1.x < m2.x else m2.v_x
            m1.v_y = m1.v_y + 1 if m2.y > m1.y else m1.v_y - 1 if m2.y < m1.y else m1.v_y
            m2.v_y = m2.v_y + 1 if m1.y > m2.y else m2.v_y - 1 if m1.y < m2.y else m2.v_y
            m1.v_z = m1.v_z + 1 if m2.z > m1.z else m1.v_z - 1 if m2.z < m1.z else m1.v_z
            m2.v_z = m2.v_z + 1 if m1.z > m2.z else m2.v_z - 1 if m1.z < m2.z else m2.v_z
        
        # update the position of every moon by applying velocity
        for m in moons:
            m.x = m.x + m.v_x
            m.y = m.y + m.v_y
            m.z = m.z + m.v_z
        
        # debug info
        #print("End of time_step",str(time_step))
        #print_moons(moons)

    # calculate the total energy: each moon is potential energy (sum abs val of coords) times kinetic energy (sum abs val of velocity)
    return sum([moon.energy() for moon in moons])


# parse file, example: <x=15, y=10, z=0>
moons_raw = open("Resources/input12.txt").readlines()
moons = []
for raw_line in moons_raw:
    raw_line = raw_line[1:-1] if raw_line[-1] == ">" else raw_line[1:-2] # chop off < and >\n
    coords_raw = raw_line.split(", ")
    coords = [int(z.split("=")[1]) for z in coords_raw]
    moons.append(Moon(coords[0],coords[1],coords[2]))

print("Part 1:", run_steps(moons,1000))