import beings
import random
import math
# simplest lifecycle
kinds = {
    "simple_beings": [beings.SimpleBeing() for x in range(1000)]
    #"mutable_beings": [beings.MutableBeing() for x in range(1500)],
    # "less_mortal_beings": [beings.LessMortalBeing() for x in range(1000)]
}
moves = 10000
# main loop
for i in range(moves):
    out = str(i)
    for kind in kinds:
        sum_mortality = 0
        sum_birthrate = 0
        idx = 0
        for index, being in enumerate(kinds[kind]):
            sum_mortality += kinds[kind][index].mortality
            sum_birthrate += kinds[kind][index].birthrate_mu
            if random.random() < being.mortality:
                kinds[kind].pop(index)
            children = int(math.floor(random.gauss(being.birthrate_mu, being.birthrate_sigma)))
            if children > 0:
                for i in range(children):
                    new_one = being.reproduce()
                    kinds[kind].append(new_one)
            idx += 1
        beings_q = len(kinds[kind])
        out += " "+str(beings_q)+" "+str(round(sum_mortality/idx,5))+" "+str(round(sum_birthrate/idx,5))
    print(','.join(out.split('.')))

