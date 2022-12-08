class Node(object):
    def __init__(self, name):
        self.name = name
        self.files = []
        self.dirs = []
        self.is_root = (name == '/')

    def add_file(self, name, size):
        self.files += [(name, size)]

    def add_dir(self, name):
        self.dirs += [Node(name)]

    def my_print(self, level):
        print(' ' * (level * 2) + '/' + self.name)
        for i in self.files:
            print(' '*((level+1)*2)+i[0]+ ' '+str(i[1]))
        for i in self.dirs:
            i.my_print(level+1)


def get_dir_size(tree):
    size = 0
    for f in tree.files:
        size += f[1]
    for d in tree.dirs:
        size += get_dir_size(d)

    return size


def populate(node, input_data, idx):
    while idx < len(input_data):
        line = input_data[idx]
        if not line:
            idx += 1
            continue
        info = line.split()
        if info[0] == '$':
            if info[1] == 'ls':
                idx += 1
                continue
            elif info[1] == 'cd':
                if info[2] == '..':
                    return idx
                else:
                    for fdir in node.dirs:
                        if fdir.name == info[2]:
                            idx = populate(fdir, input_data, idx+1)
                            break
        elif info[0] == 'dir':
            node.add_dir(info[1])
        else:
            node.add_file(info[1], int(info[0]))
        idx += 1
    return idx


def part1(node, total):
    dir_size = get_dir_size(node)
    if dir_size < 100000:
        total += dir_size
    for d in node.dirs:
        total = part1(d, total)
    return total


def part2(node, total_size, closest):
    need_size = 40000000
    my_size = get_dir_size(node)
    del_size = total_size - my_size
    if closest[1] < del_size <= need_size:
        closest = (node, del_size)
    for d in node.dirs:
        closest = part2(d, total_size, closest)
    return closest


def day_7():
    with open('day7') as infile:
        input_data = infile.read().split('\n')

    file_tree = Node('/')
    populate(file_tree, input_data, 1)
    tree_size = get_dir_size(file_tree)
    print(f'part 1 answer: {part1(file_tree, 0)}')
    print(f'part 2 answer: {get_dir_size(part2(file_tree,tree_size, (file_tree, 0))[0])}')


