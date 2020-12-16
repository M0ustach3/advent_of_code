import math
from pprint import pprint

rows, columns = 128, 8
plane = [[0 for x in range(columns)] for y in range(rows)]

best_score = 0

with open('input.txt') as file:
    lines = [f.strip() for f in file.readlines()]
    for line in lines:
        row_start = 0
        row_end = 127
        column_start = 0
        column_end = 7

        for i in range(7):
            if line[i] == 'F':
                # Keep upper half
                row_end = math.floor(row_end - ((row_end - row_start) / 2))
            else:
                # Keep lower half
                row_start = math.ceil(row_start + ((row_end - row_start) / 2))

        for i in range(7, 10):
            if line[i] == 'L':
                # Keep lower half
                column_end = math.floor(column_end - ((column_end - column_start) / 2))
            else:
                # Keep upper half
                column_start = math.ceil(column_start + ((column_end - column_start) / 2))

        score = row_start * 8 + column_end
        plane[row_start][column_end] = score
        if score > best_score:
            best_score = score

pprint(plane)
print("Best score is : {}".format(best_score))
