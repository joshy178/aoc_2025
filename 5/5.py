ranges = []

check = False
total_fresh = 0
for line in open('input2.txt', 'r').readlines():
    line = line.strip()
    if line == '':
        check = True
        continue
    if not check:
        id_range = line.split('-')
        lower = int(id_range[0])
        higher = int(id_range[1])
        ranges.append((lower, higher))
        continue
    else:
        num = int(line)
        fresh_str = 'spoiled'
        for id_range in ranges:
            lower = id_range[0]
            higher = id_range[1]
            if num >= lower and num <= higher:
                fresh_str = 'fresh'
                total_fresh += 1
                break
        print(f'ID {num} {fresh_str}')

print(f'total fresh {total_fresh}')

