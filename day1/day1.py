cal_list = []

with open("input.txt", "r") as file:
    cal = 0
    for line in file.readlines():
        line = line.strip()
        if line != '':
            cal = cal + int(line)
        else:
            cal_list.append(cal)
            cal = 0


print(cal_list)
print(max(cal_list))

cal_list = sorted(cal_list)
print(cal_list)
print(cal_list[-1] + cal_list[-2] + cal_list[-3])

