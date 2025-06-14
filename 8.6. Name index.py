def ask_user(quaestion, complaint, retries):
    while True:
        answer = input(quaestion).lower()
        if answer == 'yes':
            return 1
        if answer == 'no':
            return -1
        if answer == 0 :
            print('kilkist shansiv')
            break

ask_user('Ви хочете вийти?')
ask_user('Видалити фаайл',4)
ask_user('Записати файл',4)
