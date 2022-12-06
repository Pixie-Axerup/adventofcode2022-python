
#part1
with open("input.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        for i in range(0, len(line)):
            if ((line[i] != line[i+1] and line[i] != line[i+2] and line[i] != line[i+3]) and
                (line[i+1] != line[i+2] and line[i+1] != line[i+3]) and
                (line[i+2] != line[i+3])):
                print(line[i]+line[i+1]+line[i+2]+line[i+3])
                break

            else:
                continue

        print(i+4)
        file.close()


#part2
from collections import Counter
somm = ''
with open("input.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        for i in range(0, len(line)):
            somm = line[i:i+14]
            freq = Counter(somm)
            if len(freq) == len(somm):
                print(True)
                break
            else:
                continue

        print(i+14)
        file.close()