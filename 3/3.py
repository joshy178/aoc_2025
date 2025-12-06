total = 0



def find_largest(num_str):
    largest = 0
    largest_index = -1
    for index, num in enumerate(num_str):
        num = int(num)
        if num > largest:
            largest = num
            largest_index = index
    return largest_index, largest

for line in open('input2.txt', 'r').readlines():
    line = line.strip()
    # print(line)
    org_line = line
    line_len = len(line)
    int_list =[]
    for i in reversed(range(1, 13)):
        largest_index, largest = find_largest(line[:len(line)-i+1])
        int_list.append(str(largest))
        line = line[largest_index+1:]
        # print((largest_index, largest))
        # print(line)

    large_num = int(''.join(int_list))
    print(f'{org_line} ---- {large_num}')
    total += large_num
print(f'total output {total}')


''''
 2 9 3 4 2





'''