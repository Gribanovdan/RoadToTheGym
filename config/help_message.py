'''
Идея по улучшению:
Хранить структуру Комманла в файле с командами, где будет сама команда и ее описание. Тогда по ключу команды можно брать как саму команду, так и описание, которое можно использовать здесь
'''

from config.formatting import Color

help_message = '\n' + \
               Color.BOLD + 'This is brief guid of using this project!\n' + Color.END + \
               '- ' + Color.PURPLE + 'base' + Color.END + ' - \'base\' mod\n' \
                                                          '-️' + Color.PURPLE + 'add' + Color.END + ' - add new training\n' \
                                                                                                    '-️' + Color.PURPLE + 'delete [name]' + Color.END + ' - delete training\n' \
                                                                                                                                                        '-️' + Color.PURPLE + 'edit [name]' + Color.END + ' - edit training\n' \
                                                                                                                                                                                                          '-️' + Color.PURPLE + 'show' + Color.END + ' - show all your trainings\n' \
                                                                                                                                                                                                                                                     '-️' + Color.PURPLE + 'choose [name/index]' + Color.END + ' - show training that by name\n' \
                                                                                                                                                                                                                                                                                                               '-️' + Color.PURPLE + 'help' + Color.END + ' - show help message\n' \
                                                                                                                                                                                                                                                                                                                                                          'That\'s all for now!' \
                                                                                                                                                                                                                                                                                                                                                          '\n'

base_help_message = '\n' + \
                    Color.BOLD + 'This is a \'base\' mod, where you can see base (inplace) trainings from developers!\n' + Color.END + \
                    '-️' + Color.PURPLE + 'quit' + Color.END + ' - quit from \'base\' mod\n' \
                                                               '-️' + Color.PURPLE + 'show' + Color.END + ' - show all your trainings\n' \
                                                                                                          '-️' + Color.PURPLE + 'choose [name]' + Color.END + ' - show training that by name\n' \
                                                                                                                                                              '-️' + Color.PURPLE + 'help' + Color.END + ' - show help message\n' \
                                                                                                                                                                                                         'That\'s all for now!' \
                                                                                                                                                                                                         '\n'

help_message_tgbot = [  # HTML
    '<b>This is brief guid of using this project!</b>',
    '▫️ /base - \'base\' mod',
    '▫️ /add - add new training',
    '▫️ /delete [name] - delete training',
    '▫️ /edit - edit training',
    '▫️ /show - show all your trainings',
    '▫️ /choose [name/index] - show training that by name',
    '▫️ /help - show help message',
    'That\'s all for now!'
]

base_help_message_tgbot = [
    'This is a \'base\' mod, where you can see base (inplace) trainings from developers!',
    '▫ /quit - quit from \'base\' mod',
    '▫ /show - show all your trainings',
    '▫ /choose [name/index] - show training that by name',
    '▫ /help - show help message\n',
    'That\'s all for now!'
]
