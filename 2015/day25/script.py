def next_iteration(value):
    return (value * 252533) % 33554393


col = row = 1
val = 20151125
while True:
    if row == 2981 and col == 3075:
        break
    val = next_iteration(val)
    col += 1
    row -= 1
    if row == 0:
        row = col
        col = 1

print(val)
