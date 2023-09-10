from aiogram.dispatcher.filters.state import StatesGroup, State


class AddingStates(StatesGroup):
    Adding_Name = State()
    Adding_Desc = State()
    Adding_Program = State()
