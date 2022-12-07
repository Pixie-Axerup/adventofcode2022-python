from collections import defaultdict

sizes_dict = defaultdict(int)
path = []

#part1
with open("input.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        part = line.split(' ')
        if part[1] == 'cd':
            if part[2] == '..':
                path.pop()
            else:
                path.append(part[2])
        elif part[1] == 'ls':
            continue
        elif part[0] == 'dir':
            continue
        else:
            size = int(part[0])
            for i in range(1, len(path)+1):
                sizes_dict['/'.join(path[:i])] += size

total = sizes_dict['/']

part1 = 0
for k,v in sizes_dict.items():
    if v <= 100000:
        part1 = part1 + v

print(part1)

#part2

max_used = 70000000 - 30000000
to_free_up = total - max_used
part2 = 1000000000

for k,v in sizes_dict.items():
    if v > to_free_up:
        part2 = min(part2, v)

print(part2)