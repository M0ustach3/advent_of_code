from pprint import pprint


class Bag:
    def __init__(self, p_color):
        self.color = p_color
        self.can_contain = {}

    def __repr__(self):
        return repr("Bag of color {}, who can contain {}".format(self.color, self.can_contain))


def find_bag_with_name(p_name, p_list):
    for bg in p_list:
        if bg.color == p_name:
            return bg
    return None


def who_can_contain(p_color, p_list):
    container = []
    for p in p_list:
        if p_color in p.can_contain.keys():
            container.append(p)
    return container


def compute(p_bag, p_list):
    m_bag = find_bag_with_name(p_bag, p_list)
    total = 1
    for key, value in m_bag.can_contain.items():
        total = total + value * compute(key, p_list)
    return total


with open('input.txt') as file:
    lines = [li.rstrip() for li in file.readlines()]
    bags = []
    for line in lines:
        li = line.split(' bags ')
        color = li[0]
        li[1] = li[1][8:]
        containing_bags = li[1][:-1]
        containing_bags = containing_bags.split(', ')
        bag = Bag(color)
        for con_bag in containing_bags:
            splitted = con_bag.split()
            try:
                quantity = int(splitted[0])
                bag_name = " ".join(splitted[1:3])
                bag.can_contain[bag_name] = quantity
            except:
                quantity = 0
        bags.append(bag)

    compte = compute('shiny gold', bags) - 1
    print(compte)

# for bag in bags:
#     if bg.color in bag.can_contain.keys():
#         list_can_contain_directly.add(bag)
#
# ended = False
#
# while not ended:
#     before = len(list_can_contain_directly)
#     for b in list_can_contain_directly:
#         list_can_contain_directly = list_can_contain_directly | set(who_can_contain(b.color, bags))
#     if before == len(list_can_contain_directly):
#         ended = True
#
# pprint(len(list_can_contain_directly))
