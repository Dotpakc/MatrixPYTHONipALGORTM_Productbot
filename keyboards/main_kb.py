from aiogram import types

# 1.курси
# 2.Контакти
# 3.Про нас
# 4.Підтримка


main_keyboard = types.InlineKeyboardMarkup(row_width=2)
main_keyboard.add(types.InlineKeyboardButton(text='💻Курси', callback_data='courses'))
main_keyboard.add(
    types.InlineKeyboardButton(text='🛒Мерчь', callback_data='merch'),
    types.InlineKeyboardButton(text='📝Про нас', callback_data='about_us'),
    types.InlineKeyboardButton(text='📞Контакти', callback_data='contacts'),
    types.InlineKeyboardButton(text='📞Підтримка', callback_data='support')
)

main_back_keyboard = types.InlineKeyboardMarkup(row_width=2)
main_back_keyboard_but =types.InlineKeyboardButton(text='👈 В головне меню', callback_data='main_back')
main_back_keyboard.add(main_back_keyboard_but)