import copy
from math import fabs


def print_grid(grid, rope):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] = '.'
    for g in rope[::-1]:
        grid[g[0]][g[1]] = g[2]
    for row in grid[::-1]:
        print(''.join(row))
    print()


def do_move(grid, rope, part, dist):
    rope[0][part] += dist

    # move rest of rope
    for i in range(1, len(rope)):
        #print(i, rope)
        #print_grid(grid, rope)

        # same column
        if rope[i][0] == rope[i-1][0]:
            if rope[i][1] == rope[i-1][1]+2:
                rope[i][1] -= 1
            elif rope[i][1] == rope[i-1][1]-2:
                rope[i][1] += 1
        # same row
        elif rope[i][1] == rope[i-1][1]:
            if rope[i][0] == rope[i-1][0]+2:
                rope[i][0] -= 1
            elif rope[i][0] == rope[i-1][0]-2:
                rope[i][0] += 1
        elif rope[i][0] == rope[i-1][0]-2:
            if rope[i][1] <= rope[i-1][1] - 1:
                rope[i][0] += 1
                rope[i][1] += 1
            elif rope[i][1] >= rope[i-1][1] + 1:
                rope[i][0] += 1
                rope[i][1] -= 1
        elif rope[i][0] == rope[i-1][0]+2:
            if rope[i][1] <= rope[i-1][1] - 1:
                rope[i][0] -= 1
                rope[i][1] += 1
            elif rope[i][1] >= rope[i-1][1] + 1:
                rope[i][0] -= 1
                rope[i][1] -= 1
        elif rope[i][0] == rope[i-1][0] - 2:
            if rope[i][1] <= rope[i-1][1] - 1:
                rope[i][0] += 1
                rope[i][1] += 1
            elif rope[i][1] >= rope[i-1][1] + 1:
                rope[i][0] += 1
                rope[i][1] -= 1
        elif rope[i][1] == rope[i-1][1] + 2:
            if rope[i][0] >= rope[i-1][0] + 1:
                rope[i][1] -= 1
                rope[i][0] -= 1
            elif rope[i][0] <= rope[i-1][0] - 1:
                rope[i][1] -= 1
                rope[i][0] += 1
        elif rope[i][1] == rope[i-1][1] - 2:
            if rope[i][0] >= rope[i-1][0] + 1:
                rope[i][1] += 1
                rope[i][0] -= 1
            elif rope[i][0] <= rope[i-1][0] - 1:
                rope[i][1] += 1
                rope[i][0] += 1
    #print_grid(grid, rope)
    return rope


def part1(moves, rope_len):
    moves = moves
    min_lr = 0
    max_lr = 0
    min_ud = 0
    max_ud = 0
    pos = [0, 0]
    for move in moves:
        if move[0] == 'L':
            pos[1] -= move[1]
        elif move[0] == 'R':
            pos[1] += move[1]
        elif move[0] == 'U':
            pos[0] += move[1]
        else:
            pos[0] -= move[1]
        if pos[1] > max_lr:
            max_lr = pos[1]
        if pos[0] > max_ud:
            max_ud = pos[0]
        if pos[1] < min_lr:
            min_lr = pos[1]
        if pos[0] < min_ud:
            min_ud = pos[0]

    max_ud += 1
    max_lr += 1
    #min_ud -= 1
    #min_lr -= 1
    visited = []
    grid = []
    for i in range((max_ud-min_ud)):
        grid += [['.']*(max_lr-min_lr)]
    #print_grid(grid)
    rope = [[-min_ud, -min_lr, str(x) if x > 0 else 'H'] for x in range(rope_len)]
    #print(rope)
    visited += []
    # print(visited)
    # grid[0][0] = 'H'

    #print_grid(grid)
    # for row in grid[::-1]:
        # print(' '.join(row))
    for move in moves:
        #print(move)
        #print(rope)
        if move[0] == 'U':
            for m in range(move[1]):
                rope = do_move(grid, rope, 0, 1)
                # print_grid(grid,rope)
                if (rope[-1][0], rope[-1][1]) not in visited:
                    visited += [(rope[-1][0], rope[-1][1])]
        elif move[0] == 'D':
            for m in range(move[1]):
                rope = do_move(grid, rope, 0, -1)
                if (rope[-1][0], rope[-1][1]) not in visited:
                    visited += [(rope[-1][0], rope[-1][1])]
               # print_grid(grid)
        elif move[0] == 'R':
            for m in range(move[1]):
                rope = do_move(grid, rope, 1, 1)
                if (rope[-1][0], rope[-1][1]) not in visited:
                    visited += [(rope[-1][0],rope[-1][1])]
               # print_grid(grid)
                # print('visited:', visited)
        else:
            for m in range(move[1]):
                rope = do_move(grid, rope, 1, -1)
                if (rope[-1][0], rope[-1][1]) not in visited:
                    visited += [(rope[-1][0], rope[-1][1])]
                #print_grid(grid)
        # print(rope)
        #print(visited)
    #print_grid(grid)
    # print(head)

    return len(visited)


def day_9():
    with open('day9') as infile:
        lines = infile.read().split('\n')
    moves = []
    for line in lines:
        if not line:
            continue
        moves += [(line.split()[0], int(line.split()[1]))]
    print(f'part 1 answer: {part1(moves,2)}')
    print(f'part 1 answer: {part1(moves, 10)}')
