def part1():
    degrees = 0 # increasing clockwise (right), 0=E, 90=S, 180=W, 270=N
    coord_x = coord_y = 0
    for line in open("../Resources/problem12.txt"):
        direction = line[0:1]
        value = int(line[1:])
        if direction == "N" or (direction == "F" and degrees == 270):
            coord_y += value
        elif direction == "W" or (direction == "F" and degrees == 180):
            coord_x -= value
        elif direction == "S" or (direction == "F" and degrees == 90):
            coord_y -= value
        elif direction == "E" or (direction == "F" and degrees == 0):
            coord_x += value
        elif direction == "R":
            degrees += value
            while degrees >= 360:
                degrees -= 360
        else: #direction == "L"
            degrees -= value
            while degrees < 0:
                degrees += 360
    return abs(coord_x)+abs(coord_y)

def part2():
    my_x = my_y = 0
    wp_x = 10
    wp_y = 1
    for line in open("../Resources/problem12.txt"):
        direction = line[0:1]
        value = int(line[1:])
        if direction == "F":
            my_x += wp_x * value
            my_y += wp_y * value
        elif direction == "N":
            wp_y += value
        elif direction == "W":
            wp_x -= value
        elif direction == "S":
            wp_y -= value
        elif direction == "E":
            wp_x += value
        else:
            degrees = (360 + (value if direction == "R" else value*-1)) % 360
            if degrees == 90:
                temp_y = -1 * wp_x
                wp_x = wp_y
                wp_y = temp_y
            elif degrees == 180:
                wp_x = wp_x * -1
                wp_y = wp_y * -1
            elif degrees == 270:
                temp_x = -1 * wp_y
                wp_y = wp_x
                wp_x = temp_x
    return abs(my_x)+abs(my_y)

print("Part 1:",part1())
print("Part 2:",part2())