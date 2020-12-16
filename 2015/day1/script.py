with open('input.txt') as file:
    line = file.readline()
    floor = 0
    pos = 1
    ended = False
    for char in line:
        if char == '(':
            floor = floor + 1
        else:
            floor = floor - 1
        if floor < 0 and not ended:
            print("Position entering the basement {}".format(pos))
            ended = True
        else:
            pos = pos + 1

    print("Final floor {}".format(floor))
