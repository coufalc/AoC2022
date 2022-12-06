def is_subset(pair):
    p1_low = int(pair[0].split('-')[0])
    p1_high = int(pair[0].split('-')[1])
    p2_low = int(pair[1].split('-')[0])
    p2_high = int(pair[1].split('-')[1])

    if p1_low <= p2_low and p1_high>=p2_high:
        return True
    elif p2_low <= p1_low and p2_high >= p1_high:
        return True
    return False


def overlaps(pair):
    p1_low = int(pair[0].split('-')[0])
    p1_high = int(pair[0].split('-')[1])
    p2_low = int(pair[1].split('-')[0])
    p2_high = int(pair[1].split('-')[1])

    if p1_low in range(p2_low,p2_high+1):
        return True
    if p1_high in range(p2_low,p2_high+1):
        return True
    if p2_low in range(p1_low,p1_high+1):
        return True
    if p2_high in range(p1_low,p1_high+1):
        return True
    return False


def day_4() :
    with open('day4') as infile:
        pairs = [x.split(',') for x in infile.read().split()]

    subset_counts = 0
    for pair in pairs:
        if is_subset(pair):
            subset_counts += 1
    print(f'part 1 answer: {subset_counts}')

    subset_counts = 0
    for pair in pairs:
        if overlaps(pair):
            subset_counts += 1
    print(f'part 2 answer: {subset_counts}')