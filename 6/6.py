# num_map = []
# ops = []
# for line in open('input2.txt', 'r').readlines():
#     line = line.strip()
#     if line[0] in ['+', '*']:
#         ops = line.split()
#     else:
#         nums = [int(x) for x in line.split()]
#         num_map.append(nums)

# # print(num_map)
# grand_total = 0
# totals = []
# for j in range(0, len(num_map[0])):
#     op_str = ''
#     for i in range(0, len(num_map)):
#         if i == 0:
#             total = num_map[i][j]
#             op_str = str(num_map[i][j])
#             continue
#         if ops[j] == '+':
#             total += num_map[i][j]
#         else:
#             assert ops[j] == '*'
#             total *= num_map[i][j]
#         op_str += ops[j] + str(num_map[i][j])
#     totals.append(total)
#     grand_total += total
#     print(f'{op_str}={total}')


# # print(num_map)
# print(f'Grand Total: {grand_total}')

num_map = []
ops = []
for line in open('input.txt', 'r').readlines():
    line = line.strip()
    if line[0] in ['+', '*']:
        ops = line.split()
    else:
        nums = [int(x) for x in line.split()]

        num_map.append(nums)


# print(num_map)
grand_total = 0
totals = []
for j in range(0, len(num_map[0])):
    op_str = ''
    hit_zero = False
    new_nums = []
    for i in range(0, len(num_map)):
        new_nums.append(num_map[i][j])
        # print(new_nums)
    new_nums.sort()
    new_nums.reverse()
    first_op = True
    total = 0
    final_nums = [0] * len(new_nums)
    while new_nums[0] > 0:
        print(new_nums)
        newer_nums = []
        for i, num in enumerate(new_nums):
            # largest number has no digits left
            # bail
            if i == 0 and num == 0:
                break
            newer_num = num // 10
            newer_nums.append(newer_num)
            num = num % 10
            if first_op:
                first_op = False
                total = num
                op_str += str(num)    
            if ops[j] == '+':
                total += num
            else:
                assert ops[j] == '*'
                total *= num
            op_str += ops[j] + str(num)
        new_nums = newer_nums
    grand_total += total
    print(f'{op_str}={total}')


# print(num_map)
print(f'Grand Total: {grand_total}')

