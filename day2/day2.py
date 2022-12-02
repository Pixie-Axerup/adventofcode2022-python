score1 = 0
score2 = 0

#part1
with open("input.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        opponent = line[0]
        me = line[2]
        if opponent == 'A': #Rock
            if me == 'X':   #Rock
                score1 = score1 + 1 + 3
            elif me == 'Y': #Paper
                score1 = score1 + 2 + 6
            elif me == 'Z':  #Scissors
                score1 = score1 + 3 + 0
        if opponent == 'B': #Paper
            if me == 'X':   #Rock
                score1 = score1 + 1 + 0
            elif me == 'Y': #Paper
                score1 = score1 + 2 + 3
            elif me == 'Z': #Scissors
                score1 = score1 + 3 + 6
        if opponent == 'C': #Scissors
            if me == 'X':   #Rock
                score1 = score1 + 1 + 6
            elif me == 'Y': #Paper
                score1 = score1 + 2 + 0
            elif me == 'Z': #Scissors
                score1 = score1 + 3 + 3
file.close()

print(score1)

#part2
with open("input.txt", "r") as file2:
    for line in file2.readlines():
        line = line.strip()
        opponent = line[0]
        me = line[2]
        if opponent == 'A': #Rock
            if me == 'X':   #Loose => Scissors
                score2 = score2 + 3 + 0
            elif me == 'Y': #Draw => Rock
                score2 = score2 + 1 + 3
            elif me == 'Z':  #Win => Paper
                score2 = score2 + 2 + 6
        if opponent == 'B': #Paper
            if me == 'X':   #Loose => Rock
                score2 = score2 + 1 + 0
            elif me == 'Y': #Draw => Paper
                score2 = score2 + 2 + 3
            elif me == 'Z': #Win => Scissors
                score2 = score2 + 3 + 6
        if opponent == 'C': #Scissors
            if me == 'X':   #Loose => Paper
                score2 = score2 + 2 + 0
            elif me == 'Y': #Draw => Scissors
                score2 = score2 + 3 + 3
            elif me == 'Z': #Win => Rock
                score2 = score2 + 1 + 6

file2.close()
print(score2)



