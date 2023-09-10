from aiogram.dispatcher.filters.state import StatesGroup, State


class EditingStates(StatesGroup):
    Editing_Name = State()
    Editing_Desc = State()
    Editing_Program = State()
