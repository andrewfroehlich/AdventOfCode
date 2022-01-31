from collections import deque

inp = [int(d) for d in open("Resources/input8.txt").readline().split()]
part1 = index = 0
stack = deque()
while index < len(inp):
    children,metadata = inp[index],inp[index+1]
    index += 2
    if children == 0:
        node_value = 0
        for i in range(index,index+metadata):
            node_value += inp[i]
        part1 += node_value
        index += metadata
        while stack:
            stack_ch,stack_me,child_list = stack.pop()
            stack_ch -= 1
            child_list.append(node_value)
            if stack_ch > 0:
                stack.append( (stack_ch,stack_me,child_list) )
                break
            else:
                node_value = 0
                for i in range(index,index+stack_me):
                    part1 += inp[i]
                    if inp[i]-1 < len(child_list):
                        node_value += child_list[inp[i]-1]
                index += stack_me
    else:
        stack.append( (children,metadata,[]) )
print("Part 1:", part1,"\nPart 2:", node_value)