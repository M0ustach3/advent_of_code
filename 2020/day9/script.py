def part1(preamble):
    with open('input.txt') as file:
        numbers = [int(l.rstrip()) for l in file.readlines()]
        start = 0
        end = preamble
        valid = True
        while valid:
            valid_numbers = numbers[start:end]
            current_number = numbers[end]
            compte = 0
            for i in range(len(valid_numbers)):
                for j in range(len(valid_numbers)):
                    if valid_numbers[i] + valid_numbers[j] == current_number:
                        compte = compte + 1
            if compte <= 0:
                valid = False
                break
            start = start + 1
            end = end + 1
        return current_number


def part2(preamble):
    with open('input.txt') as file:
        numbers = [int(l.rstrip()) for l in file.readlines()]
        target = part1(preamble)
        start = 0
        end = 0
        found = False
        while not found:
            check_numbers = numbers[start:end]
            somme = sum(check_numbers)
            if somme == target:
                found = True
                print('Minimum {} and Maximum {}'.format(min(check_numbers), max(check_numbers)))
                print('The solution is {}'.format(min(check_numbers) + max(check_numbers)))
                break
            elif somme < target:
                # Expand with one more
                end = end + 1
            else:
                start = start + 1
                end = 0


part2(25)
