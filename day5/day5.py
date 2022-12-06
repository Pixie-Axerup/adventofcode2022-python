part1 = ''
part2 = ''

stacks_example = [["Z", "N"],
                ["M", "C", "D"],
                ["P"]]

stacks_real = [["Z", "P", "M", "H", "R"],
                ["P", "C", "J", "B"],
                ["S", "N", "H", "G", "L", "C", "D"],
                ["F", "T", "M", "D", "Q", "S", "R", "L"],
                ["F", "S", "P", "Q", "B", "T", "Z", "M"],
                ["T", "F", "S", "Z", "B", "G"],
                ["N", "R", "V"],
                ["P", "G", "L", "T", "D", "V", "C", "M"],
                ["W", "Q", "N", "J", "F", "M", "L"]]

stacks1 = stacks_real

#part1
with open("input.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        words = line.split(' ')
        quantity = int(words[1])
        from_stack = int(words[3])
        to_stack = int(words[5])

        for i in range(quantity):
            crate = stacks1[from_stack-1].pop()
            stacks1[to_stack-1].append(crate)

    for stack in stacks1:
        part1 = part1 + stack[-1]

    print(part1)
    file.close()

#part2

stacks_real2 = [["Z", "P", "M", "H", "R"],
               ["P", "C", "J", "B"],
               ["S", "N", "H", "G", "L", "C", "D"],
               ["F", "T", "M", "D", "Q", "S", "R", "L"],
               ["F", "S", "P", "Q", "B", "T", "Z", "M"],
               ["T", "F", "S", "Z", "B", "G"],
               ["N", "R", "V"],
               ["P", "G", "L", "T", "D", "V", "C", "M"],
               ["W", "Q", "N", "J", "F", "M", "L"]]

stacks2 = stacks_real2
with open("input.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        words = line.split(' ')
        quantity = int(words[1])
        from_stack = int(words[3])
        to_stack = int(words[5])

        for i in range(quantity):
            index = len(stacks2[from_stack-1])-(quantity-i)
            crate = stacks2[from_stack-1][index]
            stacks2[from_stack-1].pop(index)
            stacks2[to_stack-1].append(crate)


    for stack in stacks2:
        part2 = part2 + stack[-1]

    print(part2)
    file.close()







