from collections import deque

def parse_rules():
    rule_map = {}
    sections = open("input.txt").read().split("\n\n")
    for line in sections[0].splitlines():
        name,rawrules = line[:-1].split("{")
        rule_map[name] = [d.split(":") for d in rawrules.split(",")]
    return rule_map,sections[1].splitlines()

def part1():
    rule_map,lines = parse_rules()
    sum1 = 0
    for line in lines:
        for expression in line[1:-1].split(","):
            exec("global x,m,a,s;"+expression)
        current = rule_map["in"]
        rule_i = 0 
        while rule_i < len(current):
            rule = current[rule_i]
            if len(rule) == 1 or eval(rule[0]):
                sum1 += (x+m+a+s) if rule[-1] == 'A' else 0
                if rule[-1] in ('A','R'):
                    break
                current = rule_map[rule[-1]]
                rule_i = 0
            else:
                rule_i += 1
    return sum1

def part2():
    rule_map,_ = parse_rules()
    rule_map['A'] = [['A']] # add 'A' and 'R' cases so they can be processed like any other rule
    rule_map['R'] = [['R']]
    bfs = deque()
    bfs.append( ("in",0,1,4000,1,4000,1,4000,1,4000) ) # ruleId, ruleIndex, x-range, m-range, a-range, s-range (ranges inclusive)
    sum2 = 0
    while bfs:
        ruleId,rule_i,x1,x2,m1,m2,a1,a2,s1,s2 = bfs.popleft()
        if rule_i >= len(rule_map[ruleId]) or x1>x2 or m1>m2 or a1>a2 or s1>s2 or any(i<1 for i in (x1,m1,a1,s1)) or any(i>4000 for i in (x2,m2,a2,s2)):
            continue # stop processing for invalid cases
        rule = rule_map[ruleId][rule_i]
        if len(rule) == 1: # no condition to check, process result or move to next ruleId
            if rule[-1] == 'A':
                sum2 += (1+x2-x1)*(1+m2-m1)*(1+a2-a1)*(1+s2-s1)
            elif rule[-1] != 'R':
                bfs.append( (rule[-1],0,x1,x2,m1,m2,a1,a2,s1,s2) )
        else:
            v,s,n = rule[0][0],rule[0][1],int(rule[0][2:])
            # append to bfs with the new ranges for the success case, moving to the new ruleId
            bfs.append( (rule[-1], 0,
                (n+1) if v=='x' and s=='>' else x1, (n-1) if v=='x' and s=='<' else x2,
                (n+1) if v=='m' and s=='>' else m1, (n-1) if v=='m' and s=='<' else m2,
                (n+1) if v=='a' and s=='>' else a1, (n-1) if v=='a' and s=='<' else a2,
                (n+1) if v=='s' and s=='>' else s1, (n-1) if v=='s' and s=='<' else s2) )
            # append to bfs with the new ranges for the failure case, incrementing the index on current ruleId
            bfs.append( (ruleId, rule_i+1,
                n if v=='x' and s=='<' else x1, n if v=='x' and s=='>' else x2,
                n if v=='m' and s=='<' else m1, n if v=='m' and s=='>' else m2,
                n if v=='a' and s=='<' else a1, n if v=='a' and s=='>' else a2,
                n if v=='s' and s=='<' else s1, n if v=='s' and s=='>' else s2) )
    return sum2
        
if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())