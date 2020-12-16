def set_bit(p_value, p_bit):
    return p_value | (1 << p_bit)


def clear_bit(p_value, p_bit):
    return p_value & ~(1 << p_bit)


def part1(p_mask, p_input):
    memory = {}

    for mask_length in range(len(p_mask)):
        current_mask = p_mask[mask_length]
        current_instructions = p_input[mask_length]

        for instruction in current_instructions:
            for loop in range(len(current_mask)):
                if current_mask[loop] == 'X':
                    continue
                elif current_mask[loop] == '1':
                    instruction[1] = set_bit(instruction[1], len(current_mask) - loop - 1)
                elif current_mask[loop] == '0':
                    instruction[1] = clear_bit(instruction[1], len(current_mask) - loop - 1)
        for item in current_instructions:
            memory[item[0]] = item[1]
    return memory


with open('input.txt') as file:
    lines = [li.rstrip() for li in file.readlines()]
    masks = []
    instructions = []
    current_instruction_set = -1
    for line in lines:
        if line.find("mask") != -1:
            masks.append(line.split(" = ")[1])
            instructions.append([])
            current_instruction_set = current_instruction_set + 1
        elif line.find("me") != -1:
            splitted = line.split(" = ")
            value = int(splitted[1])
            address = int(splitted[0].split("mem[")[1][:-1])
            instructions[current_instruction_set].append([address, value])

    mem = part1(masks, instructions)
    print(sum(mem.values()))
