from pprint import pprint

trees = []

with open('input.txt') as file:
    lines = [lin.strip() for lin in file.readlines()]
    for line in lines:
        temp_line = []
        for i in range(100):
            for char in line:
                temp_line.append(char)

        trees.append(temp_line)

found = False
i = 0
j = 0

compte_2 = 0

while not found:
    try:
        if trees[i][j] == '#':
            compte_2 = compte_2 + 1
    except IndexError:
        found = True
    i = i + 1
    j = j + 3

found = False
i = 0
j = 0

compte_1 = 0

while not found:
    try:
        if trees[i][j] == '#':
            compte_1 = compte_1 + 1
    except IndexError:
        found = True
    i = i + 1
    j = j + 1

found = False
i = 0
j = 0

compte_3 = 0

while not found:
    try:
        if trees[i][j] == '#':
            compte_3 = compte_3 + 1
    except IndexError:
        found = True
    i = i + 1
    j = j + 5

found = False
i = 0
j = 0

compte_4 = 0

while not found:
    try:
        if trees[i][j] == '#':
            compte_4 = compte_4 + 1
    except IndexError:
        found = True
    i = i + 1
    j = j + 7

found = False
i = 0
j = 0

compte_5 = 0

while not found:
    try:
        if trees[i][j] == '#':
            compte_5 = compte_5 + 1
    except IndexError:
        found = True
    i = i + 2
    j = j + 1

print("{} {} {} {} {}".format(compte_1, compte_2, compte_3, compte_4, compte_5))
print("Multiplication : {}".format(compte_1 * compte_2 * compte_3 * compte_4 * compte_5))
