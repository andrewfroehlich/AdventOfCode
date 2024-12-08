def process_input():
    grid = open("input.txt").read().splitlines()
    obstacles = set()
    dir_indices= {"^":0, ">":1, "v":2, "<":3}
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] == "#":
                obstacles.add( (i,j) )
            elif grid[j][i] != ".":
                guard = ( (i,j) , dir_indices[grid[j][i]] )
    return obstacles,len(grid[0])-1,len(grid)-1,guard

def part1(obstacles,max_x,max_y,guard):
    visited = set()
    x,y = guard[0]
    dir_index = guard[1]
    directions = [ (0,-1), (1,0), (0,1), (-1,0) ]
    while 0<=x<=max_x and 0<=y<=max_y:
        visited.add( (x,y) )
        dir_x,dir_y = directions[dir_index]
        next_x,next_y = x+dir_x,y+dir_y
        if (next_x,next_y) in obstacles:
            dir_index = (dir_index+1) % 4 #turn right
        else:
            x,y = next_x,next_y
    return len(visited)

def part2_brute(obstacles,max_x,max_y,guard):
    part2 = 0
    directions = [ (0,-1), (1,0), (0,1), (-1,0) ]
    # iterate through possible obstruction spots
    for i in range(max_x+1):
        for j in range(max_y+1):
            if (i,j) in obstacles or (i,j) == guard[0]:
                continue # skip existing obstacles and guard start location
            visited = set()
            x,y = guard[0]
            dir_index = guard[1]
            while 0<=x<=max_x and 0<=y<=max_y:
                if (x,y,dir_index) in visited:
                    part2 += 1
                    break
                visited.add( (x,y,dir_index) )
                dir_x,dir_y = directions[dir_index]
                next_x,next_y = x+dir_x,y+dir_y
                if (next_x,next_y) in obstacles or (next_x,next_y) == (i,j):
                    dir_index = (dir_index+1) % 4 #turn right
                else:
                    x,y = next_x,next_y
    return part2

if __name__ == "__main__":
    obstacles,max_x,max_y,guard = process_input()
    print("Part 1:",part1(obstacles,max_x,max_y,guard))
    print("Part 2:",part2_brute(obstacles,max_x,max_y,guard))