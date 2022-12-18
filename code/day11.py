import math

def part1(monkeys):
    for i in range(10000):
        modular = 1
        for idx in range(len(monkeys)):
            modular *= monkeys[idx][3]
        for idx in range(len(monkeys)):
            for item in monkeys[idx][0]:
                worry = item[1]
                mod = monkeys[idx][2]
                if monkeys[idx][2] == 'old':
                    mod = worry
                if monkeys[idx][1] == '+':
                    worry += mod
                elif monkeys[idx][1] == '*':
                    worry *= mod
                worry = worry % modular
                #worry //= 5-2*part
                #worry //= 1.5
                if worry % monkeys[idx][3] == 0:
                    monkeys[monkeys[idx][4]][0] += [(item[0], worry)]
                else:
                    monkeys[monkeys[idx][5]][0] += [(item[0], worry)]
            monkeys[idx][6] += len(monkeys[idx][0])
            monkeys[idx][0] = []
    item1 = 0
    item2 = 0
    for m in monkeys:
        if m[6] > item1:
            item2 = item1
            item1 = m[6]
        elif m[6] > item2:
            item2 = m[6]
    return item1*item2


def day_11():
    with open('day11') as infile:
        monkey_input = infile.read().split('\n\n')

    monkeys = []
    item = 0

    for i in monkey_input:
        raw = i.split('\n')
        items = []
        for x in raw[1].split(': ')[1].split(', '):
            items += [(item,int(x))]
            item += 1
        op = raw[2].split()[4]
        raw_amt = raw[2].split()[5]
        if raw_amt != 'old':
            amt = int(raw_amt)
        else:
            amt = raw_amt
        mod = int(raw[3].split()[3])
        true = int(raw[4].split()[5])
        false = int(raw[5].split()[5])
        monkeys += [[items,op,amt,mod,true,false,0]]
    print(monkeys)
    print(part1(monkeys))