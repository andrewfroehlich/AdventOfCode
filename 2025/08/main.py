from itertools import combinations
import heapq
import math

def distance(p1,p2):
    return ((p2[2]-p1[2])**2 + (p2[1]-p1[1])**2 + (p2[0]-p1[0])**2)**0.5

def solve(part2=False):
    points = [tuple(map(int, line.strip().split(','))) for line in open("input.txt")]
    distances = []
    for i, j in combinations(range(len(points)), 2):
        dist = distance(points[i], points[j])
        distances.append((dist, i, j))
    
    shortest = heapq.nsmallest(1000, distances) if not part2 else sorted(distances)
    point_to_circuit,circuit_sizes = {},[]
    for dist,i,j in shortest:
        if i not in point_to_circuit and j not in point_to_circuit:
            circuit_id = len(circuit_sizes)+1
            point_to_circuit[i] = circuit_id
            point_to_circuit[j] = circuit_id
            circuit_sizes.append(2)
        elif i in point_to_circuit and j in point_to_circuit:
            if point_to_circuit[i] != point_to_circuit[j]:
                cid_from = point_to_circuit[j]
                cid_to = point_to_circuit[i]
                for p in point_to_circuit:
                    if point_to_circuit[p] == cid_from:
                        point_to_circuit[p] = cid_to
                circuit_sizes[cid_to-1] += circuit_sizes[cid_from-1]
                circuit_sizes[cid_from-1] = 0
                if circuit_sizes[cid_to-1] == len(points) and part2:
                    return points[i][0]*points[j][0]
        else:
            circuit_id = point_to_circuit.get(i) or point_to_circuit[j]
            point_to_circuit[i] = circuit_id
            point_to_circuit[j] = circuit_id
            circuit_sizes[circuit_id-1] += 1
            if circuit_sizes[circuit_id-1] == len(points) and part2:
                return points[i][0]*points[j][0]

    if not part2:
        largest_circuits = heapq.nlargest(3, circuit_sizes)
        return math.prod(largest_circuits)

if __name__ == "__main__":
    print("Part 1:", solve())
    print("Part 2:", solve(True))