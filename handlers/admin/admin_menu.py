import os
import json

from slugify import slugify

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from states.admin import AdminMenu

from keyboards.main_kb import main_back_keyboard
from keyboards.admin_kb import admin_main_keyboard
from utils import (find_files_courses, 
                   decode_files, generate_kb_courses, get_image_course, 
                   generate_kb_lvl_course, get_product)

ADMIN_LIST = [  # Список адмінів
            283941818,
            283941818,
]

#Задача додавання товарів

@dp.message_handler(commands=['admin'], state='*')
async def admin_menu(message: types.Message, state: FSMContext):
    # if not message.from_user.id in ADMIN_LIST:
    #     return
    markup = admin_main_keyboard
    await message.answer('Виберіть дію: ', reply_markup=markup)
    await state.finish()
    await AdminMenu.menu.set()
    
@dp.callback_query_handler(text='admin_main_back', state=AdminMenu)
async def admin_main_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_text('Виберіть дію: ', reply_markup=admin_main_keyboard)
    await state.finish()
    await AdminMenu.menu.set()

@dp.callback_query_handler(text='exit_admin_menu', state=AdminMenu)
async def exit_admin_menu(call: types.CallbackQuery, state: FSMContext):
    await call.answer("Ви вийшли з адмін меню")
    await state.finish()
    
    await call.message.edit_text('Назад до головного меню бота ', reply_markup=main_back_keyboard)