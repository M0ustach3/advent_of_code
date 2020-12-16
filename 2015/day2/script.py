with open('input.txt') as file:
    lines = [[int(j) for j in l.rstrip().split('x')] for l in file.readlines()]
    total = 0
    ribbon = 0
    for gift in lines:
        l = gift[0]
        w = gift[1]
        h = gift[2]
        ribbon = ribbon + (min([2 * l + 2 * w, 2 * w + 2 * h, 2 * h + 2 * l]) + l * w * h)
        total = total + (2 * l * w + 2 * w * h + 2 * h * l + min([l * w, w * h, h * l]))
    print("Total papier {} et total ruban {}".format(total, ribbon))
