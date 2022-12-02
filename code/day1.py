def day_1():
    with open('day1') as infile:
        groups = infile.read().split('\n\n')
    max = [(0,0),(-1,-1),(-2,-2)]
    group = 0
    for g in groups:
        group += 1
        sum = 0
        for l in g.split('\n'):
            v=0
            if l:
                v = int(l)
            sum += v
        #print(group,sum,max)
        for m in range(len(max)):
            if sum > max[m][1]:
                max.insert(m,(group,sum))
                max = max[:3]
                break
        #if group > 5:
        #    break

    print(f'part 1 answer: {max[0][1]}')
    total = 0
    for m in max:
        total += m[1]
    print(f'part 2 answer: {total}')