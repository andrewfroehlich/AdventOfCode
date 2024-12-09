from collections import deque

def part1(input):
    memory,space_ids = [],deque()
    id,files = 0,True
    for value in input:
        if files:
            for _ in range(int(value)):
                memory.append(id)
            id += 1
        else:
            for _ in range(int(value)):
                memory.append(".")
                space_ids.append(len(memory)-1)
        files = not files

    # fill in memory
    while space_ids:
        space_id = space_ids.popleft()
        if space_id >= len(memory):
            break
        fill_in = memory.pop()
        while fill_in == ".": # keep popping until a value is found to fill in
            fill_in = memory.pop()
        if space_id >= len(memory): # check to make sure the space hasn't been popped off
            memory.append(fill_in)
            break
        memory[space_id] = fill_in

    # get checksum
    return sum(i * memory[i] for i in range(len(memory)) if memory[i] != ".")

def part2(input):
    memory = deque()
    files = True
    id = 0
    for value in input:
        value = int(value)
        if files:
            memory.append( (id,value) )
            id += 1
        elif value > 0:
            memory.append( (".",value) )
        files = not files

    # fill in memory
    i = len(memory)-1
    while i >= 0:
        if memory[i][0] == ".": # spaces don't have to move
            i -= 1
        else:
            id,value = memory[i]
            j = 0
            while j < i and (memory[j][0] != "." or memory[j][1] < value):
                j += 1
            if j < i: #need to check again in case the while ended on this case

                # mark what is to be moved
                to_be_moved = memory[i]

                # pop the moving item, replacing with a wider space
                to_be_popped = (i,1) # (index of pops, num of pops)
                if i-1 >= 0 and memory[i-1][0] == ".": # check for space before
                    to_be_popped = (i-1,2)
                if i+1 < len(memory) and memory[i+1][0] == ".": # check for space after
                    to_be_popped = (to_be_popped[0],to_be_popped[1]+1)
                new_space_value = 0
                memory.rotate(-to_be_popped[0]) # use rotations on the deque to pop at index
                for _ in range(to_be_popped[1]):
                    new_space_value += memory.popleft()[1]
                memory.rotate(to_be_popped[0])
                memory.insert(to_be_popped[0], (".",new_space_value) )
                i = to_be_popped[0] # move i to the index where we ultimately popped

                # move the value to the new location
                space_replaced_value = memory[j][1]
                memory[j] = to_be_moved
                if space_replaced_value > to_be_moved[1]:
                    memory.insert(j+1, (".",space_replaced_value-to_be_moved[1]))
                    i += 1 # popping an extra moves everything up one, so move i so we don't miss anything
            i -= 1 # iterate on i regardless

    # get checksum
    checksum,i = 0,0
    for id, value in memory:
        checksum += id * sum(range(i, i + value)) if id != '.' else 0
        i += value
    return checksum

if __name__ == "__main__":
    input = open("input.txt").read().strip()
    print("Part 1:",part1(input))
    print("Part 2:",part2(input))