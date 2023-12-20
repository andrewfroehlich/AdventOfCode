from collections import deque

def parse_input():
    instr = { }
    for line in open("input.txt").read().splitlines():
        spl = line.split(" -> ")
        mod_type = spl[0][0] if spl[0][0] in "%&" else "."
        if mod_type == "%":
            instr[spl[0][1:]] = [mod_type, spl[1].split(", "), False] # type, output_list, is_on
        elif mod_type == "&":
            instr[spl[0][1:]] = [mod_type, spl[1].split(", "), [set(),set()]] # type, output_list, [input_off,input_on]
        else:
            instr[spl[0]] = [mod_type, spl[1].split(", "), None] # type, output_list, n/a
    # set input lists for &s (can't do inline with parse as we can't guarantee good order)
    for k,v in instr.items():
        mod_type,output_list,input_sets = v
        if mod_type != "&":
            continue
        for i_k,i_v in instr.items():
            _,output_list,_ = i_v
            if k in output_list:
                input_sets[0].add(i_k)
    return instr

def press_button(instr, presses, registers_to_track=None):
    totals = [0,0] # low, high
    pulses = deque()
    for _ in range(presses):
        pulses.append( (0, "broadcaster", "button") ) # 0/1 low/high, to whom, from whom
        while pulses:
            is_high,module_name,from_whom = pulses.popleft()
            if registers_to_track and is_high and from_whom in registers_to_track:
                return from_whom
            totals[is_high] += 1
            if module_name not in instr:
                continue # just process the pulse and stop, like an output condition
            mod_type,output_list,bonus = instr[module_name]
            if mod_type == ".":
                for out in output_list:
                    pulses.append( (is_high, out, module_name) )
            elif mod_type == "%" and is_high == 0: # % ignores high pulses
                is_on = instr[module_name][2]
                for out in output_list:
                    pulses.append( (0 if is_on else 1, out, module_name) )
                instr[module_name][2] = not is_on
            elif mod_type == "&":
                bonus[1 - is_high].discard(from_whom)
                bonus[is_high].add(from_whom)
                send_pulse = 0 if not bonus[0] else 1 # only send low if there are no input lows remembered (all high)
                for out in output_list:
                    pulses.append( (send_pulse, out, module_name) )
    return totals[0]*totals[1]

def part1():
    instr = parse_input()
    return press_button(instr, 1000)
    
def part2():
    instr = parse_input()
    
    # The final output is fed by nested &s. The second layer of those & need to return a High in order to flip rx to low
    input_modules_to_rx = []
    for k,v in instr.items():
        if "rx" in v[1]: # if "rx" is in the output_list
            input_modules_to_rx.append(k)
    modules_to_track = []
    for mod in input_modules_to_rx:
        modules_to_track.extend(list(instr[mod][2][0]))
    
    # Find the first spot each of the second input layer pushes a high pulse, which is where it cycles, and do the LCM
    presses,lcm = 1,1
    while modules_to_track:
        result = press_button(instr,1,modules_to_track)
        if not isinstance(result,int):
            lcm = lcm*presses
            modules_to_track.remove(result)
        presses += 1
    return lcm

if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())