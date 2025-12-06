

def left_move( position, amt_to_move ):
    amt_to_move = amt_to_move % 100
    val = position - amt_to_move

    if val < 0:
        # plus one to account for rollover
        # example -2 means at pos 98
        # 99 + -2 + 1 == 98
        return 99 + 1 + val 
    return val

def right_move( position, amt_to_move ):
    amt_to_move = amt_to_move % 100
    val = position + amt_to_move

    if val > 99:
        # minus one to account for rollover
        # 100 means at pos 0
        # 0 == 100 - 99 - 1
        diff = val - 99
        return diff - 1
    return val
    

position = 50
print(f'The dial starts by pointing at {position}.')
num_times_zero = 0
for line in open('input.txt', 'r').readlines():
    line = line.strip()
    direction = line[0]
    amt_to_move = int(line[1:])
    if direction == 'L':
        position = left_move(position=position, amt_to_move=amt_to_move)
    else:
        assert direction == 'R'
        position = right_move(position=position, amt_to_move=amt_to_move)
    extra_str = ''
    if position == 0:
        extra_str = '------------'
        num_times_zero += 1
    print(f'The dial is rotated {line} to point at {position}.{extra_str}')
    if position < 0:
        break

print(f'the password is {num_times_zero}')