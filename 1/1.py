
num_times_zero = 0

def left_move( position, amt_to_move ):
    rollover = amt_to_move // 100
    amt_to_move = amt_to_move % 100
    val = position - amt_to_move

    if val < 0:
        # plus one to account for rollover
        # example -2 means at pos 98
        # 99 + -2 + 1 == 98
        new_position = 99 + 1 + val
        if new_position != 0 and position != 0:
            rollover += 1
        return new_position, rollover
    return val, rollover

def right_move( position, amt_to_move ):
    rollover = amt_to_move // 100
    amt_to_move = amt_to_move % 100
    val = position + amt_to_move

    if val > 99:
        # minus one to account for rollover
        # 100 means at pos 0
        # 0 == 100 - 99 - 1
        diff = val - 99
        new_position = diff - 1
        if new_position != 0 and position != 0:
            rollover += 1
        return new_position, rollover
    return val, rollover
    

position = 50
print(f'The dial starts by pointing at {position}.')
for line in open('input2.txt', 'r').readlines():
    line = line.strip()
    direction = line[0]
    amt_to_move = int(line[1:])
    rollover = 0
    if direction == 'L':
        position, rollover = left_move(position=position, amt_to_move=amt_to_move)
    else:
        assert direction == 'R'
        position, rollover = right_move(position=position, amt_to_move=amt_to_move)
    extra_str = ''
    if position == 0:
        extra_str = '------------'
        num_times_zero += 1
    print(f'The dial is rotated {line} to point at {position}.{extra_str}')
    print(f'it points at zero {rollover} time(s)')
    num_times_zero += rollover

    if position < 0:
        break

print(f'the password is {num_times_zero}')