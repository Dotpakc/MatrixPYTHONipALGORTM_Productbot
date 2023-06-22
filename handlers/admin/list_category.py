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



@dp.callback_query_handler(text='list_category', state=AdminMenu.menu)
async def list_category(call: types.CallbackQuery):
    await call.answer()
    
    all_courses = decode_files(find_files_courses()) # Список курсів
    
    all_category = []
    for course in all_courses:
        all_category.append({
            'name': course.get('name'),
            'count_products': len(course.get('products'))
            })
        
        
    text = 'Список категорій:\n\n'
    for i,category in enumerate(all_category):
        text += f'{i+1}. {category.get("name").title()} ({category.get("count_products")} шт.)\n'
        
    await call.message.edit_text(text, reply_markup=admin_main_back_keyboard)
    
        
        
    
    
    
    
