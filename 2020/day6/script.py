from pprint import pprint

with open('input.txt') as file:
    lines = [l.rstrip() for l in file.readlines()]
    groups = []
    temp = []
    for line in lines:
        if line:
            temp.append(line)
        else:
            groups.append(temp.copy())
            temp.clear()
    groups.append([
        "hlqbanmtjy",
        "tdrvxcajgnfpoke",
        "jtiunkpsroa"
    ])

    total_yes_answers = []

    for group in groups:
        count = {}
        for answer in group:
            for char in answer:
                if char not in count.keys():
                    count[char] = 1
                else:
                    count[char] = count[char] + 1
        for key, cnt in count.items():
            if cnt != len(group):
                count[key] = False
            else:
                count[key] = True
        count = [key for key in count.values() if key]
        total_yes_answers.append(len(count))
    total_yes_answers = sum(total_yes_answers)
    print(total_yes_answers)
