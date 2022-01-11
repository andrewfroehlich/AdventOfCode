
class DAG:
    def __init__(self):
        self.refs = dict()
    
    def addNode(self, value):
        if value not in self.refs:
            self.refs[value] = Node(value)
        return self.refs[value]
    
    def get(self, value):
        return self.refs[value]
    
    def addEdge(self, big, small, count):
        e = Edge(big,small,count)
        big.containsEdges.append(e)
        small.containedEdges.append(e)
    
class Node:
    def __init__(self, value):
        self.value = value
        self.containsEdges = []
        self.containedEdges = []

class Edge:
    def __init__(self, big, small, count):
        self.big = big
        self.small = small
        self.contains = count

def buildDAG():
    f = open("../Resources/problem7.txt")
    d = DAG()
    for line in f:
        spl1 = line.strip().split(" bags contain ")
        containingNode = d.addNode(spl1[0])
        
        spl2 = spl1[1].split(", ")
        for s in spl2:
            countString = s.split(" ")[0]
            #"no" means no other bags, so containing will be empty
            if countString != "no":
                containsColor = s[s.index(' ')+1:s.rindex(' ')]
                containsNode = d.addNode(containsColor)
                d.addEdge(containingNode, containsNode, int(countString))
    return d

def part1(dag):
    shinyGold = dag.get("shiny gold")
    possibleColors = set()
    toTraverse = shinyGold.containedEdges
    currentEdge = None
    while len(toTraverse)>0:
        currentEdge = toTraverse.pop(0)
        containingNode = currentEdge.big
        if containingNode.value not in possibleColors:
            possibleColors.add(containingNode.value)
            toTraverse.extend(containingNode.containedEdges)
    return len(possibleColors)
    
def part2(dag):
    shinyGold = dag.get("shiny gold")
    return addCount(shinyGold.containsEdges)-1

def addCount(edges):
    returnVal = 1
    for e in edges:
        returnVal += e.contains * addCount(e.small.containsEdges)
    return returnVal

dag = buildDAG()
print("Part 1:",part1(dag))
print("Part 2:",part2(dag))