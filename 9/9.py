class coordinate(object):
    def __init__(self, coord_str):
        self.x, self.y = [int(x) for x in coord_str.split(',')]
        self.largest_area = 0
        self.other_coord = None
    def __repr__(self):
        return f'({self.x},{self.y})'
    def calc_max_area(self, other):
        width = abs(self.x - other.x) + 1
        height = abs(self.y - other.y) + 1
        area = width * height
        if area > self.largest_area:
            self.largest_area = area
            self.other_coord = other
    def __hash__(self):
        return hash((self.x, self.y))
    

coords = []
for line in open('input2.txt', 'r').readlines():
    line = line.strip()
    coords.append(coordinate(line))

for i, _ in enumerate(coords):
    for coord2 in coords[i+1:]:
        coords[i].calc_max_area(coord2)

coords.sort(key=lambda x: x.largest_area, reverse=True)

for coord in coords:
    print((coord, coord.other_coord))
    print(f'largest area {coord.largest_area}')
    break
