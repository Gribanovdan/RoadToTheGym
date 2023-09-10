from classes.User_classes import UserDB, UserMaker
from classes.Trainings_classes import *
from config.commands import user_commands, base_commands
from config.help_message import help_message, base_help_message
from config.formatting import Color


class Bot:
    cnt = 0

    def __init__(self):
        self.user_db: UserDB = None
        self.trainings_db: TrainingsDB = None
        self.trainings_maker: TrainingMaker = None
        self.user_maker: UserMaker = None
        self.create_user_db()
        self.create_trainings_db()
        self.create_trainings_maker()
        self.create_user_maker()

    def create_user_db(self):
        if not self.user_db:
            self.user_db = UserDB()
            return 'UserDB created.'
        return 'UserDB already exists'

    def create_trainings_db(self):
        if not self.trainings_db:
            self.trainings_db = TrainingsDB()
            return 'TrainingsDB created.'
        return 'TrainingsDB already exists!'

    def create_trainings_maker(self):
        if not self.trainings_maker:
            self.trainings_maker = TrainingMaker()
            return 'Trainings Maker created.'
        return 'Training Maker already exists!'

    def create_user_maker(self):
        if not self.user_maker:
            self.user_maker = UserMaker(self.user_db)
            return 'User Maker created.'
        return 'User Maker already exists!'


class Client:
    def __init__(self, user_id, bot: Bot):
        self.bot = bot
        self.bot.user_maker.create_user(user_id)
        self.my_user = self.bot.user_db.get_user(user_id)
        self.my_set: TrainingSet = self.bot.trainings_db.get_training_set(user_id)
        self.tr = Transmitter(bot, self)

    def start_looping(self) -> bool:  # Возвращает relogin - нужно ли перелогиниться, или мы завершаем программу?
        stop = False
        while not stop:
            command = self.get_command('Enter command: ')
            if len(command) < 2:
                continue
            if command.strip().split()[
                0].lower() == 'login':  # Данная команда - чисто консольная, т.к. в самом боте не будет возможности перелогиниться. Поэтому ее можно вынести из process_query
                return True
            stop = self.process_query(command.strip())
        return False

    def get_command(self, message=None):
        if isinstance(message, str):
            self.send_message(message)
        return input()

    def get_text(self, message=None):
        if isinstance(message, str):
            self.send_message(message)
        text = ''
        while True:
            line = input()
            if line == '':
                break
            text += line + '\n'
        return text

    def send_message(self, message: str = ''):
        print(message)

    def process_query(self, command: str) -> bool:
        commands = command.split()
        #  Stop command
        commands[0] = commands[0].lower()
        self.bot.trainings_maker.set_training_set(self.my_set)
        if commands[0] == 'stop':  # Чисто консольная команда, так как должна быть только у админа
            self.send_message('Ok, that\'s all for now. See you later️!')
            return True
        elif commands[0] == user_commands.get('add'):
            self.tr.add()
        elif commands[0] == user_commands.get('edit'):
            if len(commands) < 2:
                self.send_message('Enter a name of training you want to edit.')
                return False
            self.tr.edit(commands[1])
        elif commands[0] == user_commands.get('delete'):
            self.tr.delete(commands)
        elif commands[0] == user_commands.get('show_trainings'):
            self.tr.show_trainings(self.my_set.trainings)
        elif commands[0] == user_commands.get('choose_training'):
            self.tr.choose(commands, self.my_set)
        elif commands[0] == user_commands.get('help'):
            self.tr.help(help_message)
        elif commands[0] == user_commands.get('base'):
            self.base_processing()
        else:
            self.send_message('Wrong command! Type \"help\" for info')
        return False

    def base_processing(self):  # Отвечает за принятие и обработку команд в режиме базовых тренировок
        while True:
            inp = self.get_command('Enter command ' + Color.DARKCYAN + '(mod base): ' + Color.END)
            command = inp.split()[0].lower()
            base_training_set = self.bot.trainings_db.base_training_set
            if command == base_commands.get('help'):
                self.tr.help(base_help_message)
            elif command == base_commands.get('show_trainings'):
                self.tr.show_trainings(base_training_set.trainings)
            elif command == base_commands.get('choose_training'):
                self.tr.choose(inp.split(), base_training_set)
            elif command == base_commands.get('quit'):
                return
            else:
                self.send_message('Wrong command! Type \"help\" for info')


class Transmitter:
    def __init__(self, bot: Bot, my_client: Client):
        self.bot = bot
        self.my_client = my_client

    def add(self):
        name = self.my_client.get_command('Enter name:')
        if self.my_client.my_set.get_training(name) is not None:
            command = self.my_client.get_command('Such training already exists. Do you want to edit it? [Yes/No]:')
            if command[0].lower() == 'y':
                self.edit(name)
            return
        description = self.my_client.get_command('Enter description:')
        program = self.my_client.get_text('Enter program of your training (use double Enter to end typing)')
        #  Add receiving media
        self.my_client.send_message(self.bot.trainings_maker.make_training(name, description,
                                                                           program))

    def edit(self, old_name):
        old_tr: Training = self.my_client.my_set.get_training(old_name)
        if old_tr is None:
            command = self.my_client.get_command('Such training does not exist! Do you want to add it? [Yes/No]:')
            if command[0].lower() == 'y':
                self.add()
            return
        name = self.my_client.get_command('Enter name:')
        description = self.my_client.get_command('Enter description:')
        program = self.my_client.get_text('Enter program of your training (use double Enter to end typing)')
        new_training = self.bot.trainings_maker.just_create(name, description, program)
        response = self.my_client.my_set.edit_training(old_tr, new_training)
        self.my_client.send_message(response)

    def delete(self, commands):
        if len(commands) < 2:
            self.my_client.send_message('Enter name of the training you want to delete')
            return

        response = self.bot.trainings_db.get_training_set(self.my_client.my_user.id).delete_training_by_name(
            commands[1])
        self.my_client.send_message(response)

    def show_trainings(self, trainings):
        # trainings = self.my_client.my_set.trainings
        if len(trainings) == 0:
            self.my_client.send_message("You have no trainings yet! Use \"add\" to add new training")
        counter = 0
        for tr in trainings:
            counter += 1
            self.my_client.send_message(str(counter) + '. ' + tr.name)

    def choose(self, commands, training_set: TrainingSet):
        if len(commands) < 2:
            self.my_client.send_message('Enter name of the training you want to see')
            return
        name = ' '.join(commands[1:])
        if name.isdigit():
            t = training_set.get_training_by_id(int(name))
        else:
            t = training_set.get_training(name)
        if t is None:
            self.my_client.send_message('Cannot find such training. Use \"show\" to see all your trainings')
        else:
            self.my_client.send_message(Color.RED + f'{t.name}\n' + Color.END +
                                        f'{t.description}\n\n' +
                                        Color.CYAN + f'{t.program}' + Color.END)

    def help(self, message):
        self.my_client.send_message(message)
