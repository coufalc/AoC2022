def part1(forest):
    visible = 0
    for idx in range(len(forest)):
        tallest = -1
        for idx2 in range(len(forest[idx])):
            if forest[idx][idx2][0] > tallest:
                tallest = forest[idx][idx2][0]
                if not forest[idx][idx2][1]:
                    forest[idx][idx2][1] = True
                    visible += 1
    for idx2 in range(len(forest[0])):
        tallest = -1
        for idx in range(len(forest)):
            if forest[idx][idx2][0] > tallest:
                tallest = forest[idx][idx2][0]
                if not forest[idx][idx2][1]:
                    visible += 1
                    forest[idx][idx2][1] = True
    for idx in range(len(forest), 0, -1):
        tallest = -1
        for idx2 in range(len(forest[0]),0,-1):
            if forest[idx-1][idx2-1][0] > tallest:
                tallest = forest[idx-1][idx2-1][0]
                if not forest[idx-1][idx2-1][1]:
                    forest[idx-1][idx2-1][1] = True
                    visible += 1
    for idx2 in range(len(forest[0]),0,-1):
        tallest = -1
        for idx in range(len(forest),0,-1):
            if forest[idx-1][idx2-1][0] > tallest:
                tallest = forest[idx-1][idx2-1][0]
                if not forest[idx-1][idx2-1][1]:
                    visible += 1
                    forest[idx-1][idx2-1][1] = True

    return visible


def calc_score(forest,row,col):
    down = 0
    up = 0
    right = 0
    left = 0
    for r in range(row+1, len(forest)):
        down += 1
        if forest[row][col][0] <= forest[r][col][0]:
            break
    for r in range(row-1, -1, -1):
        up += 1
        if forest[row][col][0] <= forest[r][col][0]:
            break
    for c in range(col+1, len(forest[0])):
        right += 1
        if forest[row][col][0] <= forest[row][c][0]:
            break
    for c in range(col-1, -1, -1):
        left += 1
        if forest[row][col][0] <= forest[row][c][0]:
            break
    return up*down*left*right


def part2(forest):
    highest_score = 0

    for row in range(len(forest)):
        for col in range(len(forest[0])):
            score = calc_score(forest, row, col)
            if score > highest_score:
                highest_score = score
    return highest_score


def day_8():
    with open('day8') as infile:
        lines = infile.read().split('\n')

    forest = []
    for line in lines:
        if not line:
            continue
        forest += [[[int(x), False] for x in line]]
    print(f'part 1 answer: {part1(forest)}')
    print(f'part 2 answer: {part2(forest)}')
