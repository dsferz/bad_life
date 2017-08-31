class predators:
    meat_eaters = True
    gross_eaters = False
    def __init__(self):
        pass

class wolves(predators):
    name = 'W'
    aggressive_level = 5
    health = 100
    life_limit = 100
    velocity = 1
    dying_speed = 10
    def __init__(self):
        pass

class wolf_musculine(wolves):
    def __init__(self, age = 50):
        self.name += 'M'
        self.age = age
        pass

class wolf_femenine(wolves):
    def __init__(self, age = 50):
        self.name += 'F'
        self.age = age
        self.pregant = False
        pass

class grasseaters:
    meat_eaters = False
    gross_eaters = True
    bisex = False
    def __init__(self):
        pass

class rabbits(grasseaters):
    health = 50
    name = 'R'
    velocity = 1
    life_limit = 100
    dying_speed = 5
    def __init__(self):
        pass

class rabbit_musculine(rabbits):
    def __init__(self, age = 50):
        self.name += 'M'
        self.age = age
        self.bisex = True
        pass

class rabbit_femenine(rabbits):
    def __init__(self, age = 50):
        self.name += 'F'
        self.age = age
        self.pregant = False
        pass


class grass:
    def __init__(self, fill_level = 100):
        self.name = 'G'
        self.fill_level = 100
        self.growing = 1