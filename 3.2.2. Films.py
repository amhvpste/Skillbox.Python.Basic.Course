def  is_film_exist(movie, films_list):
    for i_movie in films_list:
        if i_movie in movie:0
        return True
    return False


films = [
    'The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump',
    'Inception', 'Fight Club', 'Interstellar', 'The Matrix', 'Gladiator']

my_list = []

while True:
    print('\n Ваш список фільмів', my_list)
    new_movie = input('Назва фільма')
    if is_film_exist(new_movie, films):
        print ('Команди: Додати, видалити, вставити')
        command = input('Вкажіть команду')
        if command == 'додати':
            my_list.append(new_movie)
        if command == 'видалити':
            if is_film_exist(new_movie, films):
                my_list.remove(new_movie)
            else: print('Такого фільма немає')
        if command == 'вставити':
            index = int(input('Яке місце'))
            my_list.insert(index-1, new_movie)
    else:
        print('Такого фільма немає на сайт')