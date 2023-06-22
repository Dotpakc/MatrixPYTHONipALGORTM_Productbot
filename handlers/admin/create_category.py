import os
import json

from slugify import slugify

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from states.admin import AdminMenu

from keyboards.admin_kb import admin_main_keyboard, admin_main_back_keyboard
from utils import (find_files_courses, 
                   decode_files, generate_kb_courses, get_image_course, 
                   generate_kb_lvl_course, get_product)


from aiogram.dispatcher.filters.state import State, StatesGroup

class AddCategory(StatesGroup):
    name = State()
    description = State()
    image = State()


@dp.callback_query_handler(text='add_category', state=AdminMenu.menu)
async def add_category(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text('Введіть назву категорії: ')
    await AddCategory.name.set()
    
@dp.message_handler(state=AddCategory.name)
async def add_category_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    
    await message.answer('Введіть опис категорії: ')
    await AddCategory.next()

@dp.message_handler(state=AddCategory.description)
async def add_category_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    
    await message.answer('Відправте фото категорії: ')
    await AddCategory.next()
    
@dp.message_handler(content_types=types.ContentType.PHOTO, state=AddCategory.image)
async def add_category_image(message: types.Message, state: FSMContext):
    await state.update_data(image=message.photo[-1].file_id)
    
    data = await state.get_data()
    
    payload = {
        'name': data.get('name'),
        'description': data.get('description'),
        'image': data.get('image'),
        'products': []
        }
    
    slug_name = slugify(data.get('name'),replacements=[['#','-sharp'],['&','-and'],['+','-plus']])
    json.dump(payload,
              open(
                  f'shop/course/{slug_name}.json', 
                  'w', 
                  encoding='utf-8'), 
              indent=4, 
              ensure_ascii=False)
    
    
    
    await message.answer('Категорія додана!', reply_markup=admin_main_back_keyboard)
    await AdminMenu.menu.set()