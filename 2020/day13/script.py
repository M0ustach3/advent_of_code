def part1(p_early_timestamp, p_buses):
    p_buses = [int(a) for a in p_buses if a != 'x']
    bus_schedules = []
    for bus in p_buses:
        bus_schedules.append(p_early_timestamp - (p_early_timestamp % bus) + bus)
    minimum_bus = bus_schedules.index(min(bus_schedules))
    print("Solution is {}".format((bus_schedules[minimum_bus] - p_early_timestamp) * p_buses[minimum_bus]))


def part2(p_buses):
    print(p_buses)
    finished = False
    first_index = 0
    timestamp = 0
    while not finished:
        timestamp = 1068781
        valid = 0
        for i in range(1, len(p_buses)):
            if p_buses[i] == 'x':
                continue
            next_passage = timestamp - (timestamp % int(p_buses[i])) + int(p_buses[i])
            print("Next passage {} and timestamp {}".format(next_passage, timestamp))
            if next_passage - timestamp != i:
                break
            else:
                print("VALID")
                valid = valid + 1
                timestamp = next_passage
        print("Valid number : {}".format(valid))
        if valid == len(p_buses):
            finished = True
            break
        first_index = first_index + 1


with open('example.txt') as file:
    lines = [li.rstrip() for li in file.readlines()]
    early_timestamp = int(lines[0])
    buses = lines[1].split(",")
    # part1(early_timestamp, buses)
    part2(buses)
