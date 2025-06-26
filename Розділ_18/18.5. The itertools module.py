import itertools

color = ['red', 'green', 'blue', 'yellow',]
for item in itertools.permutations(color, 4):
    print(item)



print('=' * 40)

for item in itertools.combinations(color, 2):
    print(item)
