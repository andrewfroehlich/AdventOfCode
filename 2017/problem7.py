from functools import lru_cache

class Tree():
    def __init__(self,lines):
        self.nodes = dict()
        # create nodes
        for line in lines:
            n = TreeNode(line.strip())
            self.nodes[n.name] = n
        # link nodes
        self.root_names = set()
        for name,n in self.nodes.items():
            if not n.parent:
                self.root_names.add(n.name)
            for child_name in n.children_names:
                self.nodes[child_name].parent = n
                n.children.append(self.nodes[child_name])
                self.root_names.discard(child_name)
        self.root = self.nodes[list(self.root_names)[0]]

class TreeNode():
    def __init__(self,line):
        raw_line = line.split(" -> ")
        self.name,raw_val = raw_line[0].split()
        self.value = int(raw_val[1:-1])
        self.children_names = []
        if len(raw_line) > 1:
            raw_children = raw_line[1].split(", ")
            for c in raw_children:
                self.children_names.append(c)
        self.parent = None
        self.children = []

@lru_cache
def total_weight(node):
    total = node.value
    for c in node.children:
        total += total_weight(c)
    return total

part2 = -1
def check_balance(node):
    global part2
    if part2 > -1:
        return
    for c in node.children:
        check_balance(c)
    if len(node.children) > 1:
        children_weights = [(total_weight(c),c.value) for c in node.children]
        children_weights.sort()
        if children_weights[0][0] != children_weights[1][0] and part2 == -1:
            part2 = (children_weights[1][0]-children_weights[0][0])+children_weights[0][1]
        elif children_weights[-1][0] != children_weights[-2][0] and part2 == -1:
            part2 = children_weights[-1][1]-(children_weights[-1][0]-children_weights[-2][0])

tree = Tree(open("Resources/input7.txt").readlines())
print("Part 1:",tree.root.name)

check_balance(tree.root)
print("Part 2:",part2)