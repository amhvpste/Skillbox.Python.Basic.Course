import os

def print_dirs(project):
    print('\nУ середині проекту папки:', project)
    for i_elem in os.listdir(project):  # ❗ Виправлено "fot" на "for"
        path = os.path.join(project, i_elem)
        print('  ', path)  # ❗ Виправлено синтаксис print — замінено крапку на кому

project_list = ['Skillbox', 'My_project']
for i_project in project_list:
    path_to_project = os.path.abspath(os.path.join('..', '..', i_project))
    print_dirs(path_to_project)
