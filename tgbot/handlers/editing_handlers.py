from aiogram import Dispatcher
import aiogram.types
import tgbot.states as states
from aiogram.dispatcher.storage import FSMContext


# по аналогии с adding. Можно даже придумать, как можно было бы их совместить, чтобы не копипастить код
async def editing_name_handler(message: aiogram.types.Message, state: FSMContext):
    training_name = message.text
    await message.answer(text='Введите новое краткое описание тренировки:')
    await state.update_data(training_name=training_name)
    await states.EditingStates.Editing_Desc.set()


async def editing_description_handler(message: aiogram.types.Message, state: FSMContext):
    training_description = message.text
    await message.answer(text='Введите новую программу тренировки:')
    await state.update_data(training_description=training_description)
    await states.EditingStates.Editing_Program.set()


async def editing_program_handler(message: aiogram.types.Message, state: FSMContext):
    training_program = message.text
    # Добавление тренировки в бд
    data = await state.get_data()
    bot = message.bot.get('bot')
    training_name = data.get('training_name')
    training_description = data.get('training_description')
    training_set = bot.trainings_db.get_training_set(message.from_user.id)
    # Находим старую тренировку
    old_name = data.get('old_name')
    old_training = training_set.get_training(old_name)
    from classes.Trainings_classes import Training
    training_set.edit_training(old_training, Training(training_name, training_description,
                                                      training_program))  # пока не поддерживает медиа файлы
    # Выходим из "добавления"
    await state.finish()
    await message.answer(text='Тренировка успешно добавлена!')


def register_all_editing_handlers(dp: Dispatcher):
    dp.register_message_handler(editing_name_handler, state=states.EditingStates.Editing_Name)
    dp.register_message_handler(editing_description_handler, state=states.EditingStates.Editing_Desc)
    dp.register_message_handler(editing_program_handler, state=states.EditingStates.Editing_Program)
