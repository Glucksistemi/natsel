import beings
import random
from copy import copy
# simplest lifecycle
kinds = {
    # "mutable_beings": [beings.MutableBeing() for x in range(1000)],
    "less_mortal_beings": [beings.LessMortalBeing() for x in range(1000)]
}
moves = 1000
# main loop
for i in range(moves):
    out = str(i)
    for kind in kinds:
        for index, being in enumerate(kinds[kind]):
            if random.random() < being.mortality:
                kinds[kind].pop(index)
            if random.randint(0,int(being.birthrate_max)):
                kinds[kind].append(being.born())
        out += " "+str(len(kinds[kind]))
    print(out)

