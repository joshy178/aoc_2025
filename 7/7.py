map = []

for line in open('input2.txt', 'r').readlines():
    line = line.strip()
    row = []
    for char in line:
        row.append(char)
    map.append(row)
for row in map:
    print(''.join(row))
print('-----------------')
num_splits = 0
for i, row in enumerate(map[:-1]):
    for j, _ in enumerate(row):
        if map[i][j] == 'S':
            map[i+1][j] = '|'
        if map[i][j] == '|':
            if map[i+1][j] == '^':
                num_splits += 1
                if j < len(row)-1:
                    map[i+1][j+1] = '|'
                if j > 0:
                    map[i+1][j-1] = '|'
            else:
                map[i+1][j] = '|'
for row in map:
    print(''.join(row))
print(f'Total splits {num_splits}')
