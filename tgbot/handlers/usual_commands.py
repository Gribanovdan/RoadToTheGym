from aiogram import Dispatcher
import aiogram.types
import tgbot.filters as filters
from config import help_message
import tgbot.states as states


async def start_handler(message: aiogram.types.Message):
    await help_handler(message)


async def help_handler(message: aiogram.types.Message):
    await message.answer(text='\n'.join(help_message.help_message_tgbot))


# Начало adding -> подробнее смотрим в adding_handlers
async def add_handler(message: aiogram.types.Message):
    text = [
        'Введите название тренировки: '
    ]
    await message.answer(text='\n'.join(text))
    await states.AddingStates.Adding_Name.set()


async def show_handler(message: aiogram.types.Message):
    # Получаем тренировки пользователя
    bot = message.bot.get('bot')
    user_id = message.from_user.id
    training_set = bot.trainings_db.get_training_set(user_id)
    trainings = training_set.trainings
    # Есть ли тренировки
    if len(trainings) == 0:
        await message.answer(text="You have no trainings yet! Use /add to add new training")
        return
    # Выводим
    counter = 0
    for tr in trainings:
        counter += 1
        text = [
            str(counter) + '. <b>' + tr.name + '</b>',
            tr.description
        ]
        await message.answer('\n'.join(text))


async def choose_handler(message: aiogram.types.Message):
    commands = message.text.split()
    if len(commands) < 2:
        await message.answer(text='Enter name of the training you want to see. \nExample: /choose first training')
        return
    # Подгружаем сет тренировок
    bot = message.bot.get('bot')
    training_set = bot.trainings_db.get_training_set(message.from_user.id)
    # Находим тренировку
    name = ' '.join(commands[1:])
    if name.isdigit():
        t = training_set.get_training_by_id(int(name))
    else:
        t = training_set.get_training(name)
    # Отправляем ответ
    if t is None:
        await message.answer(text='Cannot find such training. Use /show to see all your trainings')
    else:
        text = [
            '<b>' + t.name + '</b>',
            t.description,
            '',
            t.program
        ]
        await message.answer(text='\n'.join(text))


async def delete_handler(message: aiogram.types.Message):
    commands = message.text.split()
    if len(commands) < 2:
        await message.answer(text='Enter name of the training you want to delete\nExample: /delete my training')
        return
    name = ' '.join(commands[1:])
    bot = message.bot.get('bot')
    response = bot.trainings_db.get_training_set(message.from_user.id).delete_training_by_name(name)
    await message.answer(text=response)


async def edit_handler(message: aiogram.types.Message):
    commands = message.text.split()
    old_name = ' '.join(commands[1:])
    if old_name == '':
        await message.answer(text='Введите название тренировки. \nНапример: /edit my training')
        return
    # Подгружаем тренировки
    bot = message.bot.get('bot')
    training_set = bot.trainings_db.get_training_set(message.from_user.id)
    old_training = training_set.get_training(old_name)
    # Проверяем есть ли такая тренировка
    if old_training is None:
        await message.answer(text='Такой тренировки не существует. Если хотите добавить её, введите /add')
        return
    # Начинаем цепочку изменения
    await message.answer(text='Введите новое название для этой тренировки: ')
    await states.EditingStates.Editing_Name.set()
    # Запоминаем имя старой тренировки - понадобится в самом конце
    state = Dispatcher.get_current().current_state()
    await state.update_data(old_name=old_name)


async def base_handler(message: aiogram.types.Message):
    await states.GeneralStates.BaseState.set()
    await message.answer(text='Вы перешли в режим <b>base</b>.\nВведите /help для помощи')


def register_all_usual_command_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, filters.StartCommand())
    dp.register_message_handler(help_handler, filters.HelpCommand())
    dp.register_message_handler(add_handler, filters.AddCommand())
    dp.register_message_handler(show_handler, filters.ShowCommand())
    dp.register_message_handler(choose_handler, filters.ChooseCommand())
    dp.register_message_handler(delete_handler, filters.DeleteCommand())
    dp.register_message_handler(edit_handler, filters.EditCommand())
    dp.register_message_handler(base_handler, filters.BaseCommand())
