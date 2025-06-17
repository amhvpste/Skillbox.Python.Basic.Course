class Potato:
    states = {0: 'Немає', 1: 'Росте', 2: 'Зелена', 3: 'Копати!'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1

    def print_state(self):
        print('Картопля №{}, стан: {}'.format(self.index, Potato.states[self.state]))


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        for potato in self.potatoes:
            potato.grow()

    def print_all_states(self):
        for potato in self.potatoes:
            potato.print_state()

    def is_all_ripe(self):
        return all(p.state == 3 for p in self.potatoes)