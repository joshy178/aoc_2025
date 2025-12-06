ranges = open('input2.txt', 'r').read().strip().split(',')

id_sum = 0
for thing in ranges:
    temp = thing.split('-')
    bottom = int(temp[0])
    top = int(temp[1])
    patterns = {}
    for num in range(bottom, top + 1):
        # print('------------------------------')
        # print(num)
        text  = str(num)
        # print(text)
        length = len(text)
        patterns = {}
        is_invalid = False
        for i in range(1, (length//2) + 1):
            sub_text = text[0:i]
            sub_text_len = len(sub_text)
            if length % sub_text_len != 0:
                continue
            if ( sub_text * (length // sub_text_len) ) == text:
                is_invalid = True
                break

        if is_invalid:
            print(f'id {num} is invalid')
            id_sum += num
        # print('------------------------------')

    # break
print(f'id sum {id_sum}')