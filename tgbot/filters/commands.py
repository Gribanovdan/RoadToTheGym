from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from config.commands import all_commands
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Bot


async def set_usual_commands(bot: Bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand('start', 'Запустить бота'),
            BotCommand('help', 'Инструкция'),
            BotCommand('base', 'Перейти в режим базовых тренировок'),
            BotCommand('add', 'Добавить тренировку'),
            BotCommand('edit', 'Изменить тренировку'),
            BotCommand('delete', 'Удалить тренировку'),
            BotCommand('show', 'Показать все тренировки'),
            BotCommand('choose', 'Выбрать тренировку'),
        ],
        scope=BotCommandScopeDefault()
    )


class StartCommand(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        command = message.text.split()[0]
        return command == '/' + all_commands.get('start')


class HelpCommand(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        command = message.text.split()[0]
        return command == '/' + all_commands.get('help')


class AddCommand(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        command = message.text.split()[0]
        return command == '/' + all_commands.get('add')


class EditCommand(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        command = message.text.split()[0]
        return command == '/' + all_commands.get('edit')


class DeleteCommand(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        command = message.text.split()[0]
        return command == '/' + all_commands.get('delete')


class ShowCommand(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        command = message.text.split()[0]
        return command == '/' + all_commands.get('show_trainings')


class ChooseCommand(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        command = message.text.split()[0]
        return command == '/' + all_commands.get('choose_training')


class BaseCommand(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        command = message.text.split()[0]
        return command == '/' + all_commands.get('base')


class QuitCommand(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        command = message.text.split()[0]
        return command == '/' + all_commands.get('quit')
