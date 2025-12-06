total = 0
for line in open('input2.txt', 'r').readlines():
    line = line.strip()
    largest = 0
    next_largest = 0
    line_len = len(line)
    for index, num in enumerate(line):
        # print(num)
        num = int(num)
        if num > largest and index != ( line_len - 1 ):
            largest = num
            next_largest = 0
        else:
            if num > next_largest:
                next_largest = num
    large_num = int(f'{largest}{next_largest}')
    print(f'{line} ---- {large_num}')
    total += large_num
print(f'total output {total}')