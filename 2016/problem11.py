from collections import deque
import itertools

def run(state):
    moves = deque()
    moves.append( (0,1,state) )
    visited = set()
    while moves:
        steps, elevator, state = moves.popleft()
        
        #Sort the state, as it does not matter which Gen and Chip is which
        l = list(state)
        l.sort()
        state = tuple(l)
        if ((elevator, state) in visited):
            continue
        visited.add((elevator, state))
        
        #check if complete, where all items are on floor 4
        done = True
        for g,m in state:
            if g!=4 or m!=4:
                done = False
                break
        if done:
            return steps
            
        #check if the configuration is valid
        valid = True
        for i in range(len(state)):
            if state[i][0] != state[i][1]:
                for j in range(len(state)):
                    if i != j and state[i][1] == state[j][0]:
                        valid = False
                        break
        if not valid:
            continue
        
        #find move-eligible items (on elevator's floor), and combinations of 2 items
        on_floor_indices = []
        for i in range(len(state)):
            if state[i][0] == elevator:
                on_floor_indices.append( (i,0) )
            if state[i][1] == elevator:
                on_floor_indices.append( (i,1) )
        two_item_combos = list(itertools.combinations(on_floor_indices, 2))
        
        #add 1 or 2 items up or down to the stack
        if elevator < 4:
            for item_i,item_j in two_item_combos:
                moves.append( (steps+1, elevator+1, updateState(state,1,item_i,item_j)) )
            for item_i in on_floor_indices:
                moves.append( (steps+1, elevator+1, updateState(state,1,item_i,None)) )
        if elevator > 1:
            for item_i in on_floor_indices:
                moves.append( (steps+1, elevator-1, updateState(state,-1,item_i,None)) )
            for item_i,item_j in two_item_combos:
                moves.append( (steps+1, elevator-1, updateState(state,-1,item_i,item_j)) )

# increment coord 1 and 2 by the multiple supplied, returning a new state object (tuple of tuples)
def updateState(state, multiple, coord_1, coord_2):
    new_state = []
    for i in range(len(state)):
        new_g = state[i][0] + (multiple if (i,0) in (coord_1,coord_2) else 0)
        new_m = state[i][1] + (multiple if (i,1) in (coord_1,coord_2) else 0)
        new_state.append( (new_g,new_m) )
    return tuple(new_state)

print("Part 1:",run( ((1,1),(2,3),(2,3),(2,3),(2,3)) ))
print("Part 2:",run( ((1,1),(2,3),(2,3),(2,3),(2,3),(1,1),(1,1)) ))