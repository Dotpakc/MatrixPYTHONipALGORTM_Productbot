import os
import json
from slugify import slugify

from aiogram import types

from loader import dp
from keyboards.main_kb import main_back_keyboard, main_back_keyboard_but
from utils import find_files_courses, decode_files, generate_kb_courses, get_image_course, generate_kb_lvl_course

@dp.callback_query_handler(text='courses')
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    all_courses = decode_files(find_files_courses())
    
    markup = generate_kb_courses(all_courses, main_back_keyboard_but)
    if callback_query.message.photo:
        await callback_query.message.delete()
        await callback_query.message.answer(
            text='Виберіть курс: ',
            reply_markup=markup
            )
    else:
        await callback_query.message.edit_text(
            text='Виберіть курс: ',
            reply_markup=markup
            )  
    

@dp.callback_query_handler( lambda c: c.data.startswith('course_') )
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    course_slug = callback_query.data.split('_')[1]
    all_courses = decode_files(find_files_courses())
    
    for course in all_courses:
        if slugify(course['name']) == course_slug:
            markup = generate_kb_lvl_course(course_slug, course['products'], main_back_keyboard_but)
            image = get_image_course(course['image'])
            await callback_query.message.answer_photo(
                image,
                caption=f"<b>{course['name'].title()}</b>\n\n{course['description']}",
                reply_markup=markup,
                parse_mode='HTML')
            await callback_query.message.delete()
            break

@dp.callback_query_handler( lambda c: c.data.startswith('product_') )
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    course_slug = callback_query.data.split('_')[1]
    product_slug = callback_query.data.split('_')[2]
    all_courses = decode_files(find_files_courses())
    
    for course in all_courses:
        if slugify(course['name']) == course_slug:
            for product in course['products']:
                if slugify(product['name']) == product_slug:
                    image = get_image_course(product['image'])
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    markup.add(types.InlineKeyboardButton(text='Придбати', url=product['link']))
                    markup.add(types.InlineKeyboardButton(text='Назад', callback_data=f"course_{course_slug}"))
                    markup.add(main_back_keyboard_but)
                    await callback_query.message.answer_photo(
                        image,
                        caption=f"<b>{product['name'].title()}</b>\n"
                        f"<b>Ціна:</b> {product['price']} грн."
                        f"\n\n{product['description']}",
                        parse_mode='HTML',
                        reply_markup=markup)
                    await callback_query.message.delete()
                    break
            break
