class usable:

    def __init__(self, heal, stamina_gain, mana_gain):
        self.heal = heal
        self.stamina_gain = stamina_gain
        self.mana_gain = mana_gain

class weapon:
    
    def __init__(self, damage, stamina_use, speed):
        self.damage = damage
        self.stamina_use = stamina_use
        self.speed = speed

class spell:

    def __init__(self, damage, mana_use, speed):
        self.damage = damage
        self.mana_use = mana_use
        self.speed = speed