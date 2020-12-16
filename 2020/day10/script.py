def find_next_list_of_indexes(p_current_voltage, p_adapters):
    lst = []
    if p_current_voltage + 1 in p_adapters:
        lst.append(p_adapters.index(p_current_voltage + 1))
    if p_current_voltage + 2 in p_adapters:
        lst.append(p_adapters.index(p_current_voltage + 2))
    if p_current_voltage + 3 in p_adapters:
        lst.append(p_adapters.index(p_current_voltage + 3))
    return lst


def find_next_adapter_index(p_current_voltage, p_adapters):
    if p_current_voltage + 1 in p_adapters:
        return 1, p_adapters.index(p_current_voltage + 1)
    elif p_current_voltage + 2 in p_adapters:
        return 2, p_adapters.index(p_current_voltage + 2)
    elif p_current_voltage + 3 in p_adapters:
        return 3, p_adapters.index(p_current_voltage + 3)
    else:
        return -1, None


def part1(p_adapters):
    current_voltage = 0
    compte_1 = 0
    compte_3 = 0
    finished = False
    while not finished:
        next_index = find_next_adapter_index(current_voltage, p_adapters)
        if next_index[0] == 1:
            compte_1 = compte_1 + 1
        elif next_index[0] == 3:
            compte_3 = compte_3 + 1
        if next_index[1] is None:
            compte_3 = compte_3 + 1  # For the final adapter
            current_voltage = current_voltage + 3  # Same
            finished = True
            break
        current_voltage = p_adapters[next_index[1]]
    print("Total count of one volt {} and of three volts {}".format(compte_1, compte_3))
    print("The answer is {}".format(compte_1 * compte_3))


def get_arrangements(p_voltage, p_adapters):
    available_voltages = [p_adapters[vo] for vo in find_next_list_of_indexes(p_voltage, p_adapters)]
    if len(available_voltages) == 0:
        return 1
    else:
        compte = 1
        for vo in available_voltages:
            compte = compte + get_arrangements(vo, p_adapters)
        return compte


def part2(p_adapters):
    possibilities = [[0]]
    test = 4
    temp = []
    while test > 0:
        for i in range(len(possibilities)):
            next_poss = find_next_list_of_indexes(max(possibilities[i]), p_adapters)
            print("Next possibilities for {} : {}".format(max(possibilities[i]), [p_adapters[v] for v in next_poss]))
            if len(next_poss) == 1:
                possibilities[i].append(p_adapters[next_poss[0]])
            else:
                print("oof")
                for item in next_poss:
                    temp = possibilities[i]
                    temp.append(p_adapters[item])
                    possibilities.append(temp)
                    temp.clear()
        test = test - 1

    print(possibilities)


with open('example.txt') as file:
    adapters = [int(l.rstrip()) for l in file.readlines()]
    part2(adapters)
