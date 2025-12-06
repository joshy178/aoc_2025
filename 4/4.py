map = []
for line in open('input2.txt', 'r').readlines():
    line = line.strip()
    row = []
    for char in line:
        row.append(char == '@')
    map.append(row)


OFFSETS_TO_CHECK = [-1, 0, 1]


count_str = ''
total_can_access = 0
for row in range(0, len(map)):
    #print(f'row {row}')
    row_str = ''
    for column in range(0, len(map[row])):
        #print(f'column {column}')
        def is_valid(r, c):
            if r < 0:
                return False
            if c < 0:
                return False
            if r >= len(map):
                return False
            if c >= len(map[r]):
                return False
            return True
        def is_empty(r, c):
            if not is_valid(r, c):
                # #print('not valid')
                return True
            return map[r][c] == False
        if is_empty(row, column):
            row_str += '.'
            count_str += '0'
            #print('skipped')
            continue
        total_full = 0
        for row_offset in OFFSETS_TO_CHECK:
            for column_offset in OFFSETS_TO_CHECK:
                if row_offset == 0 and column_offset == 0:
                    continue
                #print(f'row {row} column {column} row_offset {row_offset}, column_offset {column_offset}')
                if not is_empty(row + row_offset, column + column_offset):
                    total_full +=1
        if total_full < 4:
            row_str = row_str + 'X'
            total_can_access += 1
        else:
            row_str += '@'
        count_str += str(total_full)
    print(row_str)
    count_str += '\n'

#print(count_str)
print(f'can access {total_can_access} rolls')
