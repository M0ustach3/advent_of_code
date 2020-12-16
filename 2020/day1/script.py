with open('input.txt') as file:
    lines = [int(l.strip()) for l in file.readlines()]
    for i in range(len(lines)):
        for j in range(len(lines)):
            for k in range(len(lines)):
                if lines[i] + lines[j] + lines[k] == 2020:
                    print("solution {}".format(lines[i] * lines[j] * lines[k]))