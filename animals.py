class predators:
    meat_eaters = True
    gross_eaters = False
    def __init__(self):
        pass

class wolves(predators):
    aggressive_level = 5
    health = 100
    life_limit = 100
    velocity = 1
    dying_speed = 10
    def __init__(self):
        pass

class wolf_musculine(wolves):
    def __init__(self, age = 50):
        self.age = age
        pass

class wolf_femenine(wolves):
    def __init__(self, age = 50):
        self.age = age
        self.pregant = False
        pass

class grosseaters:
    meat_eaters = False
    gross_eaters = True
    bisex = False
    def __init__(self):
        pass

class rabbits(grosseaters):
    health = 50
    velocity = 1
    life_limit = 100
    dying_speed = 5
    def __init__(self):
        pass

class rabbit_musculine(rabbits):
    def __init__(self, age = 50):
        self.age = age
        self.bisex = True
        pass

class rabbit_femenine(rabbits):
    def __init__(self, age = 50):
        self.age = age
        self.pregant = False
        pass
