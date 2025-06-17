from garden import *

gardens = garden.PotatoGarden(5)

for day in range(1, 5):
    print(f'\nДень {day}:')
    gardens.grow_all()
    gardens.print_all_states()

    if gardens.is_all_ripe():
        print('Увесь урожай готовий до збирання!')
        break
