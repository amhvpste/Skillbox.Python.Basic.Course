data = dict()
data['server'] = {"host": "127.0.1", "port": 8080}
data['configuration'] = {
    "ssh": {
        "access": 'true',
        "login": 'root',
        "password": '12345'
    }
}

print('Дані сервера:')
for key, value in data['server'].items():
    print(f"{key}: {value}")    

print('\nКонфігурація SSH:')
for key, value in data['configuration']['ssh'].items():
    print(f"{key}: {value}")


data['configuration']['ssh']['login'] = 'admin' # Зміна логіна
print('\nОновлена конфігурація SSH:')
for key, value in data['configuration']['ssh'].items():
    print(f"{key}: {value}")
    