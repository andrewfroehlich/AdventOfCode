class Field():
    def __init__(self, raw_str):
        raw_spl = raw_str.split(": ")
        self.name = raw_spl[0]
        raw_ranges = raw_spl[1].split(" or ")
        self.r1a = int(raw_ranges[0].split("-")[0])
        self.r1b = int(raw_ranges[0].split("-")[1])
        self.r2a = int(raw_ranges[1].split("-")[0])
        self.r2b = int(raw_ranges[1].split("-")[1])
        self.index = -1
    def isValid(self, value):
        return (self.r1a <= value and value <= self.r1b) or (self.r2a <= value and value <= self.r2b)

with open("../Resources/problem16.txt") as f:
    lines = f.read().splitlines()
line_number = 0
fields = []
while lines[line_number].strip():
    fields.append(Field(lines[line_number].strip()))
    line_number += 1
myTicketIndex = line_number + 2
validTicketsIndices = [myTicketIndex]
part1 = 0
for index in range(line_number+5,len(lines)):
    nums = [int(c) for c in lines[index].split(",")]
    ticketIsValid = True
    for n in nums:
        isValid = False
        for f in fields:
            if f.isValid(n):
                isValid = True
                break
        if not isValid:
            ticketIsValid = False
            part1 += n
    if ticketIsValid:
        validTicketsIndices.append(index)
print("Part 1:",part1)

# Start with all fields valid for all indices, and iterate to find where invalid on any ticket
fieldsPerIndex = [set([i for i in range(len(fields))]) for _ in range(len(fields))]
for ticket_index in validTicketsIndices:
    nums = [int(c) for c in lines[ticket_index].split(",")]
    for num_index in range(len(nums)):
        for field_index in range(len(fields)):
            if field_index in fieldsPerIndex[num_index] and not fields[field_index].isValid(nums[num_index]):
                fieldsPerIndex[num_index].remove(field_index)

# Field indices that can only be 1 field to set the index
indexFound = 0
while indexFound > -1:
    indexFound = -1
    for num_index in range(len(fields)):
        if len(fieldsPerIndex[num_index]) == 1:
            indexFound = num_index
            break
    if indexFound > -1:
        fieldId = tuple(fieldsPerIndex[indexFound])[0]
        fields[fieldId].index = indexFound
        for s in fieldsPerIndex:
            s.discard(fieldId)

# Get Part 2 return value using the appropriate fields
my_ticket = [int(c) for c in lines[myTicketIndex].split(",")]
part2 = 1
for f in fields:
    if f.name.startswith("departure"):
        part2 = part2 * my_ticket[f.index]
print("Part 2:",part2)