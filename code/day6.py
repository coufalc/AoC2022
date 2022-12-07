def find_marker(seq,length):
    for idx in range(len(seq)-length):
        in_range = False
        for idx2 in range(length):
            if seq[idx+idx2] in seq[idx+idx2+1:idx+length]:
                in_range = True
                break
        if in_range:
            continue
        return idx+length


def day_6():
    with open('day6') as infile:
        sequence = infile.read()

    print(f'part 1 answer: {find_marker(sequence, 4)}')
    print(f'part 2 answer: {find_marker(sequence, 14)}')