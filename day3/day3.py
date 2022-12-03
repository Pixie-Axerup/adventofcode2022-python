

#part1
print("part1")
shared_items = ''
output = 0

with open("input.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        lenght = int(len(line))
        length_comp1 = int(len(line) / 2)
        comp1 = line[0:length_comp1]
        comp2 = line[length_comp1:lenght]

        for char in comp1:
            if char in comp2:
                shared_items = shared_items + char
                break

    for char in shared_items:
        if char.islower():
            number = ord(char) - 96
            output = output + number
        else:
            number = ord(char) - 64 + 26
            output = output + number

    print(output)
file.close()

#part2
print("part2")
result = 0

from string import ascii_lowercase, ascii_uppercase
key = ascii_lowercase + ascii_uppercase
with open("input.txt", "r") as file:
     all_rucksacks = file.read().strip()

lines = all_rucksacks.split("\n")
for i in range(0,len(lines), 3):
        elf_group = lines[i:(i + 3)]

        for i, c in enumerate(key):
            if all([c in li for li in elf_group]):
                result += key.index(c) + 1

print(result)