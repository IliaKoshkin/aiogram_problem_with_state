from aiogram import Router, F
from aiogram import types
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from main import bot


class Commands(StatesGroup):
    command_02 = State()


router = Router()

@router.message(Command("start"))
async def start(message: Message):
    buttons = [
        [
            types.InlineKeyboardButton(text=f"command_01", callback_data=f"command_01"),
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer(text=f"Выберите команду.", reply_markup=keyboard)

@router.callback_query(F.data == "command_01")
async def cmd_01(callback_query: types.CallbackQuery, state: FSMContext):
    global bot # экземпляр бота, импортирован из файла main.py
    await state.set_state(Commands.command_02)
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    buttons = [
        [
            types.InlineKeyboardButton(text=f"command_02", callback_data=f"command_02{chat_id}"),
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    # бот шлет сообщение юзеру, тот выбирает команду -> должно прийти сообщение в чат chat_id
    await bot.send_message(user_id, f"Выберите команду:",
                           reply_markup=keyboard)

@router.callback_query(Commands.command_02, F.data.starttswith('command_02'))
async def cmd_02(callback_query: types.CallbackQuery, state: FSMContext):
    global bot
    #chat_id в который бот должен написать сообщение когда пользователь в личке нажмет command_02
    chat_id = callback_query.data.removeprefix('command_02')
    await bot.send_message(chat_id=chat_id, text=f"Пользователь {callback_query.from_user.id} выполнил команду command_02!")
    await state.clear()