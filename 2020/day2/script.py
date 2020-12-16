with open('input.txt') as file:
    lines = [l.strip().split(": ") for l in file.readlines()]
    valid_passwords = 0
    for item in lines:
        number_letter = item[0].split(" ")
        range_array = number_letter[0].split("-")
        min = int(range_array[0])
        max = int(range_array[1])
        letter = number_letter[1]
        password = item[1]

        count = 0

        if password[min -1] == letter and password[max -1] != letter:
            valid_passwords = valid_passwords + 1
        elif password[min -1] != letter and password[max -1] == letter:
            valid_passwords = valid_passwords + 1
        else:
            pass
            

    pass
    print(valid_passwords)