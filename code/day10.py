def part1(ops):
    pos = 0
    cycles = 1
    x = 1
    idx = 0
    state = 0
    update = 0
    sum = 0
    part2 = '\n'
    while True:
        if x-1 <= (pos%40) <= x+1:
            part2 += 'O'
        else:
            part2 += '.'
        if pos in [39, 79, 119, 159, 199, 239]:
            #pos = 1
            part2 += '\n'
        #print(cycles, X, state)
        #print(X)
        if cycles in [20, 60, 100, 140, 180, 220]:
            sum += cycles*x
            #print(cycles, cycles * X)

        if state == 0:
            if idx == len(ops):
                break
            op = ops[idx].split()
            idx += 1
            if op[0] == 'addx':
                update = int(op[1])
                state = 1
        else:
            x += update
            state = 0

        pos += 1
        cycles += 1

    return sum,part2

def day_10():
    with open('day10') as infile:
        lines = infile.read().split('\n')

    ans = part1(lines)
    p1 = ans[0]
    p2 = ans[1]
    print(f'part 1 answer: {p1}')
    print(p2)