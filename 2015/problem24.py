import itertools
import math

def run(weights,piles):
    target_weight = sum(weights)//piles
    lowest_product = -1
    for k in range(1, len(weights)//piles + 1):
        for subset in itertools.combinations(weights, k):
            if sum(subset) == target_weight:
                new_prod = math.prod(subset)
                lowest_product = new_prod if lowest_product == -1 else min(new_prod,lowest_product)
        if lowest_product != -1:
            return lowest_product

weights = [int(c) for c in open("Resources/input24.txt").readlines()]
print("Part 1:",run(weights,3))
print("Part 2:",run(weights,4))