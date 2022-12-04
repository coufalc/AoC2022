def get_match(c1, c2):
    for c in c1:
        if c in c2:
            return c


def get_match2(group):
    for c in group[0]:
        if c in group[1] and c in group[2]:
            return c
    print(group)


def get_priority(c):
    if ord(c) < ord('a'):
        return ord(c)-ord('A')+27
    else:
        return ord(c)-ord('a')+1


def day_3():
    with open('day3') as infile:
        lines = infile.read().split()

    repeat_priority = 0
    for line in lines:
        if not line:
            continue
        match = get_match(line[:len(line)//2], line[len(line)//2:])
        repeat_priority += get_priority(match)

    print(f'part 1 answer: {repeat_priority}')

    groups = []
    for idx in range(0, len(lines), 3):
        if not lines[idx]:
            continue
        groups += [(lines[idx], lines[idx+1], lines[idx+2])]

    priority = 0
    for group in groups:
        match = get_match2(group)
        priority += get_priority(match)

    print(f'part 2 answer: {priority}')
