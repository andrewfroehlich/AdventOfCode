from itertools import permutations
from sys import maxsize

weights = dict()
cities = set()
for line in open("Resources/input9.txt"):
    a,_,b,_,value = line.split()
    cities.add(a)
    cities.add(b)
    weights[(a,b)] = int(value)
    weights[(b,a)] = int(value)

min_path = maxsize
max_path = 0
for permutation in permutations(cities):
    path_weight = 0
    prev = None
    for current in permutation:
        path_weight += weights[(prev,current)] if prev else 0
        prev = current
    min_path = min(min_path, path_weight)
    max_path = max(max_path, path_weight)
print("Part 1:",min_path,"\nPart 2:",max_path)