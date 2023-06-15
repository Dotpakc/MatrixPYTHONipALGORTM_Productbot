from aiogram import types

from loader import dp
from keyboards.main_kb import main_back_keyboard

@dp.callback_query_handler(text='courses')
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("В процесі розробки", reply_markup=main_back_keyboard)