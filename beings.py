import random
from copy import copy


class Being(object):
    birthrate_max = 9
    mortality = 0.91

    def born(self):
        return copy(self)


class SimpleBeing(Being):
    pass


class LessMortalBeing(Being):
    mortality = 0.9


class MutableBeing(Being):
    mutation_chance = 0.1
    mutation_birthrate_step = 0.1
    mutation_mortality_step = 0.01
    basic_mortality = 0.5
    basic_birthrate_max = 1

    def mutate(self):
        if random.random() < self.mutation_chance:
            if random.random() > 0.5:
                if random.random() >= 0.5:
                    self.birthrate_max += self.mutation_birthrate_step
                else:
                    self.birthrate_max -= self.mutation_birthrate_step
            else:
                if random.random() >= 0.5:
                    self.mortality += self.mutation_mortality_step
                else:
                    self.mortality -= self.mutation_mortality_step

    def __init__(self, parent = None):
        if parent:
            self.birthrate_max = parent.birthrate_max
            self.mortality = parent.mortality
            self.mutate()
        else:
            self.birthrate_max = self.basic_birthrate_max
            self.mortality = self.basic_mortality

    def born(self):
        return self.__class__(self)

