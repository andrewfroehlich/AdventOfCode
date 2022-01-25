steps = 301
buffer = [0]
index = 0
for current in range(1,2018):
    insert_index = (index + steps)%len(buffer) + 1
    buffer.insert(insert_index, current)
    index = insert_index
print("Part 1:",buffer[(insert_index+1)%len(buffer)])

#don't need to build a buffer, 0 never moves, just remember what's at index 1
buffer_len = 1
index = 0
val_after_0 = -1
for current in range(1,50000001):
    insert_index = (index + steps)%buffer_len + 1
    buffer_len += 1 
    if insert_index == 1:
        val_after_0 = current
    index = insert_index
print("Part 2:",val_after_0)