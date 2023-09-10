import aiogram.types
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from config import help_message
import tgbot.filters as filters
import tgbot.states as states


async def help_handler(message: aiogram.types.Message):
    await message.answer('\n'.join(help_message.base_help_message_tgbot))


async def show_handler(message: aiogram.types.Message):
    # Получаем тренировки
    bot = message.bot.get('bot')
    training_set = bot.trainings_db.get_base_training_set()
    trainings = training_set.trainings
    # Есть ли тренировки
    if len(trainings) == 0:
        await message.answer(text="К сожалению, базовых тренировок нет")
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
    training_set = bot.trainings_db.get_base_training_set()
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


async def quit_handler(message: aiogram.types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text='Вы вышли из режима <b>base</b>')


def register_all_base_handlers(dp: Dispatcher):
    dp.register_message_handler(help_handler, filters.HelpCommand(), state=states.GeneralStates.BaseState)
    dp.register_message_handler(show_handler, filters.ShowCommand(), state=states.GeneralStates.BaseState)
    dp.register_message_handler(choose_handler, filters.ChooseCommand(), state=states.GeneralStates.BaseState)
    dp.register_message_handler(quit_handler, filters.QuitCommand(), state=states.GeneralStates.BaseState)
