import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from tgbot.conf import config
import tgbot.handlers as hd
import classes
import tgbot.filters as filters

env_path = 'tgbot/.env'


def register_handlers(dp: aiogram.Dispatcher):
    hd.register_all_adding_handlers(dp)
    hd.register_all_editing_handlers(dp)
    hd.register_all_usual_command_handlers(dp)
    hd.register_all_base_handlers(dp)
    hd.register_inappropriate_handler(dp)


async def register_commands(aiobot: aiogram.Bot):
    await filters.set_usual_commands(aiobot)


async def launch():
    # Создаем самого бота - то есть логика + БД
    bot = classes.Bot()

    conf = config.load_config(env_path)  # Подгружаем настройки

    aio_bot = aiogram.Bot(token=conf.tgbot.token, parse_mode=aiogram.types.ParseMode.HTML)  # Создаем бота
    aio_bot['config'] = config  # Сохраняем в бота настройки, чтобы потом можно было легко к ним обратиться
    aio_bot['bot'] = bot

    storage = MemoryStorage()
    dp = aiogram.Dispatcher(bot=aio_bot, storage=storage)  # Dispatcher - объект, который будет отвечать за все процессы
    await register_commands(aio_bot)  # Регистрируем команды для удобного пользования
    register_handlers(dp)  # устанавливаем все хендлеры - обработчики сообщений

    # Сообщаем что бот запущен
    await aio_bot.send_message(text='Bot launched', chat_id=1602737759)  # Мой chat-id

    try:
        await dp.start_polling()  # запускаем отлов изменений update
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await aio_bot.session.close()  # безопасно закрываем бота
