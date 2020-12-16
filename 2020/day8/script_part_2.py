def run(instructions):
    treated_instructions = []
    accumulator = 0
    instruction_pointer = 0
    while True:
        if instruction_pointer in treated_instructions:
            return False, None
        treated_instructions.append(instruction_pointer)
        try:
            instr = instructions[instruction_pointer]
        except:
            return True, accumulator
        instr = instr.split()
        if instr[0] == 'acc':
            accumulator = accumulator + int(instr[1])
            instruction_pointer = instruction_pointer + 1
            pass
        elif instr[0] == 'nop':
            instruction_pointer = instruction_pointer + 1
            continue
        elif instr[0] == 'jmp':
            instruction_pointer = instruction_pointer + int(instr[1])
            pass


with open('input.txt') as file:
    lines = [li.rstrip() for li in file.readlines()]
    print(lines)
    accumul = 0

    for index, instruction in enumerate(lines):
        if instruction[0] == 'n':
            # NOP to JMP, then run and see
            temp_instructions = lines.copy()
            temp_ins = list(temp_instructions[index])
            temp_ins[0] = 'j'
            temp_ins[1] = 'm'
            temp_instructions[index] = ''.join(temp_ins)
            value, acc = run(temp_instructions)
            if value:
                accumul = acc

        elif instruction[0] == 'j':
            # JMP to NOP, then run and see
            temp_instructions = lines.copy()
            temp_ins = list(temp_instructions[index])
            temp_ins[0] = 'n'
            temp_ins[1] = 'o'
            temp_instructions[index] = ''.join(temp_ins)
            value, acc = run(temp_instructions)
            if value:
                accumul = acc
    print("Final value of accumulator = {}".format(accumul))
