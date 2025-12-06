ranges = open('input2.txt', 'r').read().strip().split(',')

id_sum = 0
for thing in ranges:
    temp = thing.split('-')
    bottom = int(temp[0])
    top = int(temp[1])
    for i in range(bottom, top + 1):
        text  = str(i)
        # print(text)
        length = len(text)
        if (length % 2 ) != 0:
            continue
        left = text[:length//2]
        right = text[length//2:]
        # print(f'left {left}')
        # print(f'right {right}')
        if left == right:
            print(f'{text} is invalid')
            id_sum += i
    # break
print(f'id sum {id_sum}')