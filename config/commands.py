'''
Вариант улучшения:
ключи - сами команды
значения - объекты функций, которые должны выполняться

Проблема:
Так как это методы, которые привязаны к конкретным объектам, непонятно, как они будут изменять экземпляры
'''

user_commands = {
    'add': 'add',
    'edit': 'edit',
    'delete': 'delete',
    'show_trainings': 'show',
    'choose_training': 'choose',
    'help': 'help',
    'base': 'base'
}

admin_commands = {
    'stop_bot': 'stop'
}

base_commands = {
    'show_trainings': 'show',
    'choose_training': 'choose',
    'help': 'help',
    'quit': 'quit'
}

all_commands = {
    'start': 'start',
    'add': 'add',
    'edit': 'edit',
    'delete': 'delete',
    'show_trainings': 'show',
    'choose_training': 'choose',
    'help': 'help',
    'base': 'base',
    'quit': 'quit'
}
