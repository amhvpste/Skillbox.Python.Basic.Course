import os

def find_file(cur_path, file_name):
    print('Переходимо до каталогу:', cur_path)

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print(' Дивимось:', path)

        if file_name == i_elem:
            return path

        if os.path.isdir(path):
            print('Це папка, йдемо глибше')
            result = find_file(path, file_name)
            if result:
                return result

    return None
