with open('input.txt') as file:
    lines = [li.rstrip() for li in file.readlines()]
    treated_instructions = []
    print(lines)
    accumulator = 0
    instruction_pointer = 0

    ended = False

    while not ended:
        if instruction_pointer in treated_instructions:
            print('Fin')
            ended = True
            break
        treated_instructions.append(instruction_pointer)
        instr = lines[instruction_pointer]
        instr = instr.split()
        print("Instruction courante : {} (pointer at {}) and acc : {}".format(instr, instruction_pointer, accumulator))
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
    print("Valeur finale de l'accumulateur : {}".format(accumulator))
