from pprint import pprint


def count_occupied_seats(p_seats):
    count = 0
    for m_row in p_seats:
        for item in m_row:
            if item == '#':
                count = count + 1
    return count


def close_iteration(p_seats, p_superior):
    result = []
    for ro in range(len(p_seats)):
        row_temp = []
        for co in range(len(p_seats[ro])):
            if p_seats[ro][co] == 'L' and check_number_of_neighbors(p_seats, ro, co) == 0:
                row_temp.append('#')
            elif p_seats[ro][co] == '#' and check_number_of_neighbors(p_seats, ro, co) >= p_superior:
                row_temp.append('L')
            else:
                row_temp.append(p_seats[ro][co])
        result.append(row_temp)
    return result


def diagonal_iteration(p_seats, p_superior):
    result = []
    for ro in range(len(p_seats)):
        row_temp = []
        for co in range(len(p_seats[ro])):
            if p_seats[ro][co] == 'L' and check_neighbors_diagonals(p_seats, ro, co) == 0:
                row_temp.append('#')
            elif p_seats[ro][co] == '#' and check_neighbors_diagonals(p_seats, ro, co) >= p_superior:
                row_temp.append('L')
            else:
                row_temp.append(p_seats[ro][co])
        result.append(row_temp)
    return result


def check_neighbors_diagonals(p_seats, row, column):
    count = 0
    max_row_length = len(p_seats)
    max_col_length = len(p_seats[0])
    tokens = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for token in tokens:
        temp_row = row
        temp_col = column
        while 0 <= temp_row < max_row_length and 0 <= temp_col < max_col_length:
            temp_row = temp_row + token[0]
            temp_col = temp_col + token[1]
            if 0 <= temp_row < max_row_length and 0 <= temp_col < max_col_length:
                if p_seats[temp_row][temp_col] == '.':
                    continue
                if p_seats[temp_row][temp_col] == '#':
                    count = count + 1
                    break
                else:
                    break
            else:
                break
    return count


def check_number_of_neighbors(p_seats, row, column):
    count = 0
    max_row_length = len(p_seats)
    max_col_length = len(p_seats[0])
    tokens = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for token in tokens:
        if 0 <= row + token[0] < max_row_length and 0 <= column + token[1] < max_col_length and p_seats[row + token[0]] \
                [column + token[1]] == '#':
            count = count + 1
    return count


def part1(p_seats):
    osef = p_seats
    temp_count = count_occupied_seats(osef)
    while True:
        pprint(osef)
        print()
        osef = close_iteration(osef, 4)
        if count_occupied_seats(osef) != temp_count:
            temp_count = count_occupied_seats(osef)
        else:
            break
    return osef


def part2(p_seats):
    osef = p_seats
    temp_count = count_occupied_seats(osef)
    while True:
        osef = diagonal_iteration(osef, 5)
        if count_occupied_seats(osef) != temp_count:
            temp_count = count_occupied_seats(osef)
        else:
            break
    return osef


with open('input.txt') as file:
    seats = []
    for line in file.readlines():
        row = line.rstrip()
        seats.append(list(row))
    final_seats = part2(seats)
    print("Final value of occupied seats : {}".format(count_occupied_seats(final_seats)))
    with open('output.txt', 'w') as output:
        for line in final_seats:
            output.write(''.join(line))
            output.write('\n')
