import os 
import json

from aiogram import types

from slugify import slugify



def find_files_courses(file_path='shop/course'):
    files = []
    for file in os.listdir(file_path):
        if file.endswith(".json"):
            files.append(os.path.join(file_path, file))
    return files

def decode_files(files):
    files_decoded = []
    for file in files:
        files_decoded.append(
            json.load(
                open(file, encoding='utf-8')
                )
            )
    return files_decoded

def generate_kb_courses(all_courses,button_back):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    for course in all_courses:
        markup.add(
            types.InlineKeyboardButton(
                text=course['name'].capitalize(),
                callback_data=f"course_{slugify(course['name'])}"
                )
            )
    
    markup.add(button_back)
    return markup


def generate_kb_lvl_course(course_slug, products, button_back):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    for product in products:
        markup.add(
            types.InlineKeyboardButton(
                text=product['name'],
                callback_data=f"product_{course_slug}_{slugify(product['name'])}"
                )
            )
        
    markup.add(types.InlineKeyboardButton(text='Назад', callback_data=f"courses"))
    markup.add(button_back)
    return markup

def get_image_course(image):
    if os.path.exists(f'shop/course/img/{image}'):
        return types.InputFile(f'shop/course/img/{image}')
    else:
        return types.InputFile(f'shop/course/img/default.jpg')






if __name__ == '__main__':
    
    
    print(find_files_courses())
    print(decode_files(find_files_courses()))
    print(generate_kb_courses(decode_files(find_files_courses()), 'main_back'))
    print(slugify('Курс по Python'))