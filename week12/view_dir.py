import os

def view_dir(path, level=0):
    for item in os.listdir(path):
        # skip hidden files (for MacOS)
        if item.startswith('.'):
            continue
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print_spaces(level)
            print(f'+ {item}')
            view_dir(item_path, level + 1)
        else:
            print_spaces(level)
            print(f'- {item}')

def print_spaces(level):
    print('  ' * level, end='')


view_dir('/Users/doantrungtung/My Projects/DemoChart')