class Pokemon:
    def __init__(self, name, level, type_of, maximum_health, health, alive):
        self.name = name
        self.level = level
        self.type_of = type_of
        self.maximum_health = maximum_health
        self.health = health
        self.alive = alive

    def __repr__(self):
        return "{name} lv:{level} HP:{health}/{maximum_health} Type:{type_of} Alive: {alive}".format(name = self.name, level = self.level, health = self.health, maximum_health = self.maximum_health, type_of = self.type_of, alive= self.alive)

    def lose_health(self, damage):
        if self.health > 1:
            self.health = self.health - damage
            return "{name} health is now {health}".format(name = self.name, health = self.health)
        else:
            self.alive = False
            return "Pokemon is dead"
    
    def heal(self, hp):
        if self.alive is True and self.health < self.maximum_health:
            self.health += hp
            return "Pokemons {health}".format(health = self.health)
        elif self.alive is False:
            return "Pokemon is dead use revive"
        else:
            
    
pikachu = Pokemon("Pikachu", "1", "Electabuzz", 100, 100, True)

print((pikachu))



print((pikachu.lose_health(00)))

print((pikachu.lose_health(42)))

print((pikachu))

