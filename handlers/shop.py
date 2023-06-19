import os
import json
from slugify import slugify

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.main_kb import main_back_keyboard, main_back_keyboard_but
from utils import (find_files_courses, 
                   decode_files, 
                   generate_kb_courses, 
                   get_image_course, 
                   generate_kb_lvl_course, 
                   get_product)

from states.orderstates import OrderForm


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
    
    product = get_product(all_courses, course_slug, product_slug)
    
    image = get_image_course(product['image'])
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text='Замовити', callback_data=f"order_{course_slug}_{product_slug}"))
    markup.add(types.InlineKeyboardButton(text='Детальна інформація', url=product['link']))
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

@dp.callback_query_handler( lambda c: c.data.startswith('order_') )
async def process_callback_kb1btn1(callback_query: types.CallbackQuery, state: FSMContext):
    course_slug = callback_query.data.split('_')[1]
    product_slug = callback_query.data.split('_')[2]
    all_courses = decode_files(find_files_courses())
    
    product = get_product(all_courses, course_slug, product_slug)

    text = f"Ви замовили: <b>{product['name'].title()}</b>\n" \
            "Ваше замовлення буде оброблено найближчим часом.\n" \
            "ВІДПРАВТЕ СВІЙ НОМЕР ТЕЛЕФОНУ ДЛЯ ЗВ'ЯЗКУ З ВАМИ"\
            "🔽Кнопка знизу🔽"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(text='Відправити номер телефону', request_contact=True))
    await OrderForm.phone.set()
    await state.update_data(course_slug=course_slug, product_slug=product_slug)
    await callback_query.message.answer(
        text=text,
        parse_mode='HTML',
        reply_markup=markup)
    await callback_query.message.delete()
    
@dp.message_handler(state=OrderForm.phone, content_types=types.ContentTypes.CONTACT)
async def process_callback_kb1btn1(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    
    text = f"Ваш номер телефону: {phone}\n" \
        "Ваше замовлення буде оброблено найближчим часом.\n" \
        "Дякуємо за замовлення!"
    markup = types.ReplyKeyboardRemove()
    await message.answer(
        text=text,
        parse_mode='HTML',
        reply_markup=markup)
    await message.delete()
    await message.answer(
        text='Головне меню',
        reply_markup=main_back_keyboard
    )
    
    #Відправка повідомлення адміну
    data = await state.get_data()
    all_courses = decode_files(find_files_courses())
    product = get_product(all_courses, data['course_slug'], data['product_slug'])
    await message.bot.send_message(
        222201019,
        text=f"Нове замовлення!\n"
        f"Номер телефону: {phone}\n"
        f"Курс: {product['name']}\n"
        f"Ціна: {product['price']} грн."
    )
    await state.finish()