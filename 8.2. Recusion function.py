site = {
    'html': {
        'head': {
            'title': 'My site'
        },
        'body': {
            'h2': 'text text',
            'div': "generate block",
            'p': 'This is abzac'
        }
    }
}

def find_key(struct, key):
    if key in struct:
        return struct[key]
    
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key)
            if result is not None:
                return result
    return None

user_key = input('Який ключ шукаємо? ')
value = find_key(site, user_key)

if value is not None:
    print(value)
else:
    print('Такого ключа не має')
