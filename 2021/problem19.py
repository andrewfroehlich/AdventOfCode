scanners_raw = open("input19.txt").read().strip().split('\n\n')
scanners = []
for scanner_raw in scanners_raw:
    scanners.append([[int(c) for c in s.split(',')] for s in scanner_raw.split("\n")[1:]])
#48 possible rotations with the product of the below; some might not be truly valid
coord_swaps = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
negations = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]
def rotations(swap, negate, scan):
    result = []
    for i in scan:
        result.append([negate[0]*i[swap[0]], negate[1]*i[swap[1]], negate[2]*i[swap[2]]])
    return result
    
distance_from_0 = [(0,0,0)]
def alignScanner(scanner_a, scanner_b):
    a_beacons = set()
    for b in scanner_a:
        a_beacons.add(tuple(b))
    
    for swap in coord_swaps:
        for negate in negations:
            a = scanner_a
            b = rotations(swap, negate, scanner_b)
            for a_beacon in a:
                for b_beacon in b:
                    offset = [b_beacon[0]-a_beacon[0], b_beacon[1]-a_beacon[1], b_beacon[2]-a_beacon[2]]
                    match = 0
                    all_b_with_offset = []
                    for remaining_b_beacon in b:
                        b_remapped_by_offset = (remaining_b_beacon[0]-offset[0], remaining_b_beacon[1]-offset[1], remaining_b_beacon[2]-offset[2])
                        if b_remapped_by_offset in a_beacons:
                            match += 1
                        all_b_with_offset.append(b_remapped_by_offset)
                    if match >= 12:
                        distance_from_0.append(tuple(offset))
                        return (True, all_b_with_offset)
    return (False, None)

completed_indices = set()
completed_indices.add(0)
aligned_scanners = {}
aligned_scanners[0] = scanners[0]
aligned_beacons = set()
for c in scanners[0]:
    aligned_beacons.add(tuple(c))
no_overlap = set()
while len(completed_indices) < len(scanners):
    for i in range(len(scanners)):
        if i in completed_indices:
            continue
        for j in completed_indices:
            if (i,j) in no_overlap:
                continue
            found, remapped_beacons = alignScanner(aligned_scanners[j], scanners[i])
            if found:
                completed_indices.add(i)
                aligned_scanners[i] = remapped_beacons
                for c in remapped_beacons:
                    aligned_beacons.add(tuple(c))
                break
            else:
                no_overlap.add((i,j))
print("Part 1:",len(aligned_beacons))

max_manhattan_distance = 0
for x in distance_from_0:
    for y in distance_from_0:
        max_manhattan_distance = max(max_manhattan_distance, (abs(x[0]-y[0]) + abs(x[1]-y[1]) + abs(x[2]-y[2])))
print("Part 2:",max_manhattan_distance)