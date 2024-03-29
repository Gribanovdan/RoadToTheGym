from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tgbot: TgBot


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tgbot=TgBot(
            token=env.str("BOT_TOKEN")
        )
    )
