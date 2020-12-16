from pprint import pprint

import re

with open('input.txt') as file:
    lines = [l.strip() for l in file.readlines()]
    parsed = []
    temp = []
    for item in lines:
        if item:
            temp.append(item)
        else:
            parsed.append(" ".join(temp))
            temp.clear()

    passports = []

    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for item in parsed:
        items = item.split()
        dic = {}
        for attribut in items:
            splitted = attribut.split(":")
            dic[splitted[0]] = splitted[1]
        passports.append(dic)

    compte = 0

    valid_eye_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    for item in passports:
        if all(map(lambda attr: attr in item, required)):
            if 1920 <= int(item['byr']) <= 2002:
                if 2010 <= int(item['iyr']) <= 2020:
                    if 2020 <= int(item['eyr']) <= 2030:
                        unit = item['hgt'][-2:]
                        if unit == 'cm' or unit == 'in':
                            value = int(item['hgt'][:-2])
                            if (unit == 'cm' and 150 <= value <= 193) or (
                                    unit == 'in' and 59 <= value <= 76):
                                x = re.search("^#([0-9]|[a-f]){6}$", item['hcl'])
                                if x:
                                    if item['ecl'] in valid_eye_color:
                                        y = re.search("^[0-9]{9}$", item["pid"])
                                        if y:
                                            print(item)
                                            print("Valid")
                                            compte = compte + 1

    print("Valid passwords : {}".format(compte))
