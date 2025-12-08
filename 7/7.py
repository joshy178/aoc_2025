map = []
timelines_map = []
for line in open('input2.txt', 'r').readlines():
    line = line.strip()
    row = []
    timelines_row =[]
    for char in line:
        row.append(char)
        timelines_row.append(0)
    map.append(row)
    timelines_map.append(timelines_row)
for row in map:
    print(''.join(row))
print('-----------------')
num_splits = 0
for i, row in enumerate(map[:-1]):
    # prev_num_timelines = 0
    for j, _ in enumerate(row):
        if map[i][j] == 'S':
            map[i+1][j] = '|'
            timelines_map[i+1][j] = 1
        if map[i][j] == '|':
            if map[i+1][j] == '^':
                num_splits += 1
                if j < len(row)-1:
                    map[i+1][j+1] = '|'
                    timelines_map[i+1][j+1] += timelines_map[i][j]
                if j > 0:
                    map[i+1][j-1] = '|'
                    timelines_map[i+1][j-1] += timelines_map[i][j]
            else:
                map[i+1][j] = '|'
                print(f'timelines_map[i+1][j] {timelines_map[i+1][j]}')
                print(f'timelines_map[i][j] {timelines_map[i][j]}')
                timelines_map[i+1][j] += timelines_map[i][j]
    # num_timelines +=prev_num_timelines
for row in map:
    print(''.join(row))
for row in timelines_map:
    print(''.join([str(x) for x in row]))
print(f'Total splits {num_splits}')
num_timelines = 0
for timeline in timelines_map[-2]:
    num_timelines += timeline

print(f'Total timelines {num_timelines}')
