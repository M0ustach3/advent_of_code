class Waypoint:
    def __init__(self):
        self.east = 10
        self.north = 1

    def rotate(self, direction, amount):
        if (direction == 'R' or direction == 'L') and amount == 180:
            self.north = -self.north
            self.east = -self.east
        elif (direction == 'L' and amount == 90) or (direction == 'R' and amount == 270):
            temp = self.east
            self.east = -self.north
            self.north = temp
        elif (direction == 'R' and amount == 90) or (direction == 'L' and amount == 270):
            temp = self.east
            self.east = self.north
            self.north = -temp

    def move(self, direction, amount):
        if direction == 'N':
            self.north = self.north + amount
        elif direction == 'S':
            self.north = self.north - amount
        elif direction == 'W':
            self.east = self.east - amount
        elif direction == 'E':
            self.east = self.east + amount


class ShipPart2:
    def __init__(self):
        self.waypoint = Waypoint()
        self.east = 0
        self.north = 0

    def rotate_waypoint(self, direction, amount):
        self.waypoint.rotate(direction, amount)

    def move_waypoint(self, direction, amount):
        self.waypoint.move(direction, amount)

    def advance(self, amount):
        self.east = self.east + self.waypoint.east * amount
        self.north = self.north + self.waypoint.north * amount

    def __str__(self):
        return "Ship has coordinates of {}°N {}°E. Waypoint is {}°N {}°E".format(self.north, self.east,
                                                                                 self.waypoint.north,
                                                                                 self.waypoint.east)


class Ship:
    def __init__(self):
        self.facing = 90
        self.east = 0
        self.north = 0

    def __str__(self):
        direction = ""
        if self.facing == 0:
            direction = "North"
        elif self.facing == 90:
            direction = "East"
        elif self.facing == 180:
            direction = "South"
        elif self.facing == 270:
            direction = "West"
        else:
            direction = "unknown"
        return "Ship is facing {} and has coordinates of {}°N {}°E".format(direction, self.north, self.east)

    def advance(self, direction, amount):
        if direction == 'F':
            if self.facing == 0:
                # North
                self.north = self.north + amount
            elif self.facing == 90:
                # East
                self.east = self.east + amount
            elif self.facing == 180:
                # South
                self.north = self.north - amount
            elif self.facing == 270:
                # West
                self.east = self.east - amount
        elif direction == 'N':
            self.north = self.north + amount
        elif direction == 'S':
            self.north = self.north - amount
        elif direction == 'W':
            self.east = self.east - amount
        elif direction == 'E':
            self.east = self.east + amount

    def rotate(self, direction, amount):
        if direction == 'L':
            self.facing = (self.facing + (360 - amount)) % 360
        elif direction == 'R':
            self.facing = (self.facing + amount) % 360

    def move(self, action, amount):
        if action == 'R' or action == 'L':
            self.rotate(action, amount)
        else:
            self.advance(action, amount)


def part1(p_instructions):
    ship = Ship()
    for instruction in p_instructions:
        ship.move(instruction[0], int(instruction[1]))
    print("Solution is {}".format(abs(ship.east) + abs(ship.north)))


def part2(p_instructions):
    ship = ShipPart2()
    for instruction in p_instructions:
        if instruction[0] == 'F':
            ship.advance(int(instruction[1]))
        else:
            if instruction[0] in ['L', 'R']:
                ship.rotate_waypoint(instruction[0], int(instruction[1]))
            else:
                ship.move_waypoint(instruction[0], int(instruction[1]))
    print("Solution is {}".format(abs(ship.east) + abs(ship.north)))


if __name__ == '__main__':
    with open('input.txt') as file:
        instructions = [[inst[0], inst[1:]] for inst in [li.rstrip() for li in file.readlines()]]
        part2(instructions)
