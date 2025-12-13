import pprint
class coordinate(object):
    def __init__(self, coord_str):
        self.x, self.y, self.z = [int(x) for x in coord_str.split(',')]
    def __repr__(self):
        return f'({self.x},{self.y},{self.z})'
    def __sub__(self, other):
        a = (self.x - other.x)**2
        b = (self.y - other.y)**2
        c = (self.z - other.z)**2
        return (a + b + c)**1/2
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    def __hash__(self):
        return hash((self.x, self.y, self.z))
coords = []
for line in open('input1.txt', 'r').readlines():
    line = line.strip()
    coords.append(coordinate(line))

total_coords = len(coords)

# for coord in coords:
#     print(coord)


distances_map = {}
distances = []
#going to assume each distance is unique

for i, coord1 in enumerate(coords[:-1]):
    # if i == len(coords)-1:
    #     break
    for j, coord2 in enumerate(coords[i+1:]):
        key = coord1 - coord2
        assert key not in distances_map
        distances_map[key] = (coord1, coord2)
        distances.append(key)

distances.sort()

circuits = []

# pprint.pprint(distances_map)

# circuits = [set([coord]) for coord in coords]
# for circuit in circuits:
#     print(circuit)
print(f'circuit len {len(circuits)}')

i = 0
while len(circuits) == 0 or len(circuits[0]) != total_coords:

    print(f'iteration {i}')
    i +=1
    shortest_distance = distances.pop(0)
    value = distances_map[shortest_distance]
    coord1, coord2 = value

    # print(f'iteration {i} Next Shortest Distance is {coord1} to {coord2} at distance {shortest_distance}')
    found_circuit = False
    for j, circuit in enumerate(circuits):
        if coord1 in circuit:
            found_circuit = True
            circuits[j].add(coord2)
            # break
        if coord2 in circuit:
            found_circuit = True
            circuits[j].add(coord1)
            # break
        # for coord in circuit:
        #     if coord == coord1:
        #         found_circuit = True
        #         circuits[j].add(coord2)
        #         break
        #     if coord == coord2:
        #         found_circuit = True
        #         circuits[j].add(coord1)
        #         break
    if found_circuit == False:
        new_set = set()
        new_set.add(coord1)
        new_set.add(coord2)
        circuits.append(new_set)
    print((coord1, coord2))

    # print('---------')
    # for circuit in circuits:
    #     print(circuit)
    # print('---------')
    changed = True
    while changed:
        changed = False
        new_circuits = []
        for j, circuit in enumerate(circuits):
            for k, circuit2 in enumerate(circuits[j+1:]):
                # if changed:
                #     new_circuits.append(circuit2)
                #     continue
                if len(circuit.intersection(circuit2)) != 0:
                    circuits[j] = circuits[j].union(circuit2)
                    circuits.remove(circuit2)
                    # # if (j + k + 1) < len(circuits) - 1:
                    # #     new_circuits.extend(circuits[j + k + 1:])
                    changed = True
                    # break
                    # break
            if changed:
                break

for j, circuit in enumerate(circuits):
    for k, circuit2 in enumerate(circuits[j+1:]):
        if len(circuit.intersection(circuit2)) != 0:
            assert False

size_of_one = 0
for coord in coords:
    found = False
    for circuit in circuits:
        if coord in circuit:
            found = True
            break
    if not found:
        size_of_one += 1

# for j, circuit in enumerate(circuits):
#     print(f'{j}: {circuit}')

print(f'{str(coord1.x)} * {str(coord2.x)} = {coord1.x* coord2.x}')

all_points = set()

for circuit in circuits:
    for point in circuit:
        if point in all_points:
            assert False
        all_points.add(point)

circuits.sort(key=lambda x: len(x), reverse=True)
total = 0
# for i in range(0,3):
#     size = len(circuits[i])
#     print(f'Circuit {i} size {size}')
#     print(circuit)
#     if total == 0:
#         total = size
#     else:
#         total *= size

# print(f'total {total}')
# print(f'{len(circuits)} total circuits')
# print(f'{size_of_one} size_of_one')
# # print(len(distances))