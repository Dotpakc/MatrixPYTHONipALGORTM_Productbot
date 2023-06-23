from aiogram import types

# 1.🟢 Додати категорію курсів  🟡 Список категорій курсів  
# 2.🟢 Додати курс  🟡 Список курсів  🔴 Видалити курс
# 3.🟡 Список замовлень  
# 4.👈 Вийти з адмін меню


# СRUD - Це абревіатура від англійських слів Create, Read, Update, Delete, що в перекладі означає «Створити, Прочитати, Оновити, Видалити».

admin_main_keyboard = types.InlineKeyboardMarkup()

admin_main_keyboard.add(
    types.InlineKeyboardButton(
        text='🟢 Додати категорію курсів',
        callback_data='add_category'
    ),
    types.InlineKeyboardButton(
        text='🟡 Список категорій курсів',
        callback_data='list_category'
    )           
    )

admin_main_keyboard.add(
    types.InlineKeyboardButton(
        text='🟢 Додати курс',
        callback_data='add_course'
    ),
    types.InlineKeyboardButton(
        text='🟡 Список курсів',
        callback_data='list_course'
    ),
    types.InlineKeyboardButton(
        text='🔴 Видалити курс',
        callback_data='delete_course'
    )
    )

admin_main_keyboard.add(
    types.InlineKeyboardButton(
        text='🟡 Список замовлень',
        callback_data='list_orders'
    )
    )

admin_main_keyboard.add(
    types.InlineKeyboardButton(
        text='👈 Вийти з адмін меню',
        callback_data='exit_admin_menu'
    )   
    )




admin_main_back_keyboard = types.InlineKeyboardMarkup(row_width=2)
admin_main_back_keyboard_but =types.InlineKeyboardButton(text='👈 В головне меню Адміна', callback_data='admin_main_back')
admin_main_back_keyboard.add(admin_main_back_keyboard_but)