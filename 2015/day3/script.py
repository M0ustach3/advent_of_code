import os
from pprint import pprint

with open('input.txt') as file:
    line = file.readline().rstrip()
    houses = [[0 for j in range(8000)] for i in range(8000)]
    pos = [2000, 2000]
    houses[pos[0]][pos[1]] = houses[pos[0]][pos[1]] + 1
    for char in line:
        if char == '<':
            pos[0] = pos[0] - 1
        elif char == '>':
            pos[0] = pos[0] + 1
        elif char == 'V':
            pos[1] = pos[1] + 1
        else:
            pos[1] = pos[1] - 1
        houses[pos[0]][pos[1]] = houses[pos[0]][pos[1]] + 1
    total = 0
    for i in range(8000):
        for j in range(8000):
            if houses[i][j] > 0:
                total = total + 1
    print("Total covered houses is {}".format(total))
