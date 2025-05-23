monsters_count = int(input('count monster:'))
mage_index = int(input('mage_index:'))
monsters_damage = []
for monster in range(monsters_count):
    print('damage',monster + 1,'monster', end=' ')
    damage = int(input(''))
    monsters_damage.append(damage)

for i_monster in range(monsters_count):
    if monsters_damage[i_monster] < 100 and i_monster != mage_index -1:
        monsters_damage[i_monster] += monsters_damage[mage_index -1]
print('True Moster Damege',monsters_damage)