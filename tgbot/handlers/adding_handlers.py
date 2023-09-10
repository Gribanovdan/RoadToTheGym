from aiogram import Dispatcher
import aiogram.types
import tgbot.states as states
from aiogram.dispatcher.storage import FSMContext


# Запоминают имя, описание и программу тренировки
# Отсылают сообщение, мол, введите следующее
# Переключают состояние пользователя
async def adding_name_handler(message: aiogram.types.Message, state: FSMContext):
    training_name = message.text
    bot = message.bot.get('bot')  # в launch записывали в aiobot значение самого bot
    user_id = message.from_user.id
    training_set = bot.trainings_db.get_training_set(user_id)
    if training_set.get_training(training_name) is not None:
        await message.answer('Тренировка с таким названием уже существует! Придется повторять ещё раз!')
        await state.finish()
        return
    await message.answer(text='Введите краткое описание тренировки:')
    await state.update_data(training_name=training_name)
    await states.AddingStates.Adding_Desc.set()


async def adding_description_handler(message: aiogram.types.Message, state: FSMContext):
    training_description = message.text
    await message.answer(text='Введите программу тренировки:')
    await state.update_data(training_description=training_description)
    await states.AddingStates.Adding_Program.set()


async def adding_program_handler(message: aiogram.types.Message, state: FSMContext):
    training_program = message.text
    # Добавление тренировки в бд
    data = await state.get_data()
    bot = message.bot.get('bot')
    training_name = data.get('training_name')
    training_description = data.get('training_description')
    training_set = bot.trainings_db.get_training_set(message.from_user.id)
    from classes.Trainings_classes import Training
    training_set.add_training(
        Training(training_name, training_description, training_program))  # пока не поддерживает медиа файлы
    # Выходим из "добавления"
    await state.finish()
    await message.answer(text='Тренировка успешно добавлена!')


def register_all_adding_handlers(dp: Dispatcher):
    dp.register_message_handler(adding_name_handler, state=states.AddingStates.Adding_Name)
    dp.register_message_handler(adding_description_handler, state=states.AddingStates.Adding_Desc)
    dp.register_message_handler(adding_program_handler, state=states.AddingStates.Adding_Program)
