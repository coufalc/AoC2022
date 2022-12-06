def parse_raw_stacks(raw_stacks):
    raw_stack_count = len(raw_stacks.split('\n')[-1].replace(' ', ''))
    stacks = [[] for x in range(raw_stack_count)]
    for idx in range(len(raw_stacks.split('\n'))-2,-1,-1):
        row = raw_stacks.split('\n')[idx]
        for c in range(0,len(row),4):
            if row[c+1] not in '[] ':

                if not stacks[c//4]:
                    stacks[c//4] = []
                stacks[c//4] += row[c+1]

    return stacks


def parse_raw_moves(raw_moves):
    moves = []
    for line in raw_moves.split('\n'):
        if not line:
            continue
        line_split = line.split()
        moves += [(int(line_split[1]), int(line_split[3]), int(line_split[5]))]

    return moves


def part1(stacks, moves):
    for move in moves:
        count = move[0]
        from_stack = move[1] - 1
        to_stack = move[2] - 1
        stacks[to_stack] += stacks[from_stack][-1*count::][::-1]
        stacks[from_stack] = stacks[from_stack][:-1*count]

    print('part 1 answer: ', end='')
    for stack in stacks:
        if stack:
            print(stack[-1], end='')
        else:
            print(' ')
    print()


def part2(stacks, moves):
    for move in moves:
        count = move[0]
        from_stack = move[1] - 1
        to_stack = move[2] - 1
        stacks[to_stack] += stacks[from_stack][-1*count:]
        stacks[from_stack] = stacks[from_stack][:-1*count]

    print('part 2 answer: ', end='')
    for stack in stacks:
        if stack:
            print(stack[-1], end='')
        else:
            print(' ', end='')
    print()


def day_5():
    with open('day5') as infile:
        raw_stacks, raw_moves = infile.read().split('\n\n')

    stacks = parse_raw_stacks(raw_stacks)
    moves = parse_raw_moves(raw_moves)

    part1(stacks, moves)
    stacks = parse_raw_stacks(raw_stacks)
    part2(stacks, moves)
