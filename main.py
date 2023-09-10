from classes.Config_classes import Bot, Client
from tgbot.launch import launch
import asyncio


def start_bot_cmd():
    while True:
        bot = Bot()
        try:
            user_id = int(input('Enter your id: '))
        except ValueError:
            print('You need to enter only int value. Restart the program...')
            quit()
        client = Client(bot=bot, user_id=user_id)
        relogin = client.start_looping()
        if not relogin:
            break


def start_tg_bot():
    try:
        asyncio.run(launch())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')


if __name__ == "__main__":
    start_tg_bot()
