import animals
from random import randint

initial_wolves_amount = 15
initial_rabbits_amount = 40
field_w, field_l = 20, 10

def mx_init(field_l, field_w):
    return [[ [animals.grass()] for _ in range (field_l)]  for _ in range(field_w)]


def get_coord():
    def propose_coord():
        return randint(0, field_w-1), randint(0, field_l-1)

    x,y = propose_coord()
    while len(field[y][x]) > 1:
        x,y = propose_coord()
    else:
        return x, y

if __name__ == '__main__':
    field = mx_init(field_w, field_l)
    for _ in range(initial_rabbits_amount):
        x, y = map(int, get_coord())
        field[y][x].append(animals.rabbit_femenine())
    for _ in range(initial_wolves_amount):
        x, y = map(int, get_coord())
        field[y][x].append(animals.wolf_musculine())
    for line in field:
        for box in line: 
            print ' '.join(i.name for i in box).ljust(4), 
        print ''