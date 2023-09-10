import aiogram.types
from aiogram import Dispatcher


async def inappropriate_handler(message: aiogram.types.Message):
    text = [
        'Can\'t understand this command.',
        'Type /help for help'
    ]
    await message.answer(text='\n'.join(text))


def register_inappropriate_handler(dp: Dispatcher):
    dp.register_message_handler(inappropriate_handler)
