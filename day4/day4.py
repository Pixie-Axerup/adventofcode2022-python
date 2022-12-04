
answer_part1 = 0
answer_part2 = 0
with open("input.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        first_elf, second_elf = line.split(',')
        start1, end1 = first_elf.split('-')
        start2, end2 = second_elf.split('-')
        start1, end1, start2, end2 = [int(x) for x in [start1, end1, start2, end2]]

        if (start1 <= start2 and end2 <= end1) or (start2 <= start1 and end1 <= end2):
            answer_part1 = answer_part1 + 1

        if not (end1 < start2 or start1 > end2):
            answer_part2 = answer_part2 + 1

    print(answer_part1)
    print(answer_part2)
