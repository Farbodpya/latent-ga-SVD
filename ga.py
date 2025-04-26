import numpy as np
import random
from projection import decode
from utils import blend_crossover, mutate

def dynamic_ga_latent(func, z_dim=2, n_pop_init=500, max_it=200, pc=0.8, pm=0.3, mu=0.02):
    n_pop = n_pop_init
    pop = [{'Position': np.random.uniform(-5, 5, size=z_dim), 'Cost': None} for _ in range(n_pop)]
    for ind in pop:
        ind['Cost'] = func(decode(ind['Position']))
    pop.sort(key=lambda x: x['Cost'])
    best_sol = pop[0]
    best_cost = [best_sol['Cost']]

    for it in range(max_it):
        popc = []
        nc = 2 * round(pc * n_pop / 2)
        for _ in range(nc // 2):
            p1, p2 = random.sample(pop, 2)
            y1, y2 = blend_crossover(p1['Position'], p2['Position'])
            popc.append({'Position': y1, 'Cost': func(decode(y1))})
            popc.append({'Position': y2, 'Cost': func(decode(y2))})

        popm = []
        nm = round(pm * n_pop)
        for _ in range(nm):
            p = random.choice(pop)
            y = mutate(p['Position'], mu)
            popm.append({'Position': y, 'Cost': func(decode(y))})

        pop.extend(popc + popm)
        pop.sort(key=lambda x: x['Cost'])
        pop = pop[:n_pop]

        best_sol = pop[0]
        best_cost.append(best_sol['Cost'])

        n_pop = max(50, int(n_pop * 0.99))

    return best_cost
