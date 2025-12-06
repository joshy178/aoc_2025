ranges = []


class id_range:
    def __init__(self, lower, higher):
        self.lower = lower
        self.higher = higher
    def __hash__(self):
        return hash([self.lower, self.higher])
    def __repr__(self):
        return f'({self.lower},{self.higher})'
def merge_ranges(r1, r2):
    #r1
    #                       |---------|
    # r2
    #                   |----|
    #print(f'attempt to merge {r1} and {r2}')
    if r2.lower > r1.higher:
        return None
    if r1.lower > r2.higher:
        return None
    return id_range(min(r1.lower, r2.lower), max(r1.higher, r2.higher))

check = False

for line in open('input2.txt', 'r').readlines():
    line = line.strip()
    if line == '':
        check = True
        break
    id_r = line.split('-')
    lower = int(id_r[0])
    higher = int(id_r[1])
    new_range = id_range(lower, higher)
    ranges.append(new_range)

changed = True

iterations = 1
while changed:
    print(f'iteration {iterations}')
    changed = False
    for i, range1 in enumerate(ranges):
        new_range = None
        if i == len(ranges)-1:
            continue
        for range2 in ranges[i+1:]:
            new_range = merge_ranges(range1, range2)
            if new_range != None:
                #print('created new range')
                break
        if new_range != None:
            break
    if new_range != None:
        changed = True
        ranges.remove(range1)
        ranges.remove(range2)
        ranges.append(new_range)
    iterations +=1
    #print(f'List length {len(ranges)}')
    #print(ranges)

total = 0
for range1 in ranges:
    total += range1.higher - range1.lower + 1
print(f'{total} total ids')

    

