#          rock              paper           scissors
vals = [(('A', 'X'), 1), (('B', 'Y'), 2), (('C', 'Z'), 3)]


def points(play) -> int:
    op_idx: int = -1
    my_idx: int = -1
    scored: int = 0
    for idx in range(len(vals)):
        if play[1] in vals[idx][0]:
            scored += vals[idx][1]
            my_idx = idx
        if play[0] in vals[idx][0]:
            op_idx = idx

    if (op_idx+1) % 3 == my_idx:
        scored += 6
    elif op_idx == my_idx:
        scored += 3

    return scored


def get_move(play):
    op_idx = -1
    my_idx = -1
    for idx in range(len(vals)):
        if play[0] in vals[idx][0]:
            op_idx = idx
    if play[1] == 'X':
        my_idx = op_idx+2
    elif play[1] == 'Y':
        my_idx = op_idx
    else:
        my_idx = op_idx+1
    my_idx %= 3
    return vals[my_idx][0][1]


def day_2():
    with open('day2') as infile:
        lines = infile.read().split('\n')

    score: int = 0
    for line in lines:
        if not line:
            continue
        play = line.split()
        score += points(play)

    print(f'part 1 answer: {score}')

    score = 0
    for line in lines:
        if not line:
            continue
        play = line.split()
        score += points((play[0], get_move(play)))
    print(f'part 2 answer: {score}')