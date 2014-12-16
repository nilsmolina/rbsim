import numpy as np
import random

# squirtle 43
# nidoranm 50
def num_hits(hp, acc, no_crit, crit, base_speed=50, samples=500):
    ans = np.zeros(samples)
    crit_rate = float(base_speed)/512 # dunno how to round this
    for i in range(samples):
        # simulate a battle
        cur_hp = hp
        cur_hits = 0
        while cur_hp > 0:
            cur_hits += 1
            # check accuracy
            r = random.random()
            if r >= acc:
                continue
            # check crit
            ri = random.randint(255 - 39 + 1, 255)
            r = random.random()
            if r < crit_rate:
                dmg = ri * crit // 255
            else:
                dmg = ri * no_crit // 255
            cur_hp -= dmg
        ans[i] = cur_hits
    return ans

