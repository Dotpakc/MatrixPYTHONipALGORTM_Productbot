from aiogram import types

from loader import dp
from keyboards.main_kb import *


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привіт!\nЯ бот компанії \"Hillel\".\nОбери пункт меню:", reply_markup=main_keyboard)
    
@dp.callback_query_handler(text='main_back')
async def process_main_back_command(call: types.CallbackQuery):
    if call.message.photo:
        await call.message.delete()
        await call.message.answer("Обери пункт меню:", reply_markup=main_keyboard)
    else:
        await call.message.edit_text("Обери пункт меню:", reply_markup=main_keyboard)
    


@dp.callback_query_handler(text='support')
async def process_support_command(call: types.CallbackQuery):
    await call.message.edit_text("Привіт! Служба підтримки компанії \"Hillel\".\nНапишіть своє питання:",
                                 reply_markup=main_back_keyboard)


@dp.callback_query_handler(text='contacts')
async def process_contacts_command(call: types.CallbackQuery):
    await call.message.edit_text("На всі ваші запитання дадуть відповідь адміністратори.\n"
                                 "📞Телефон: 0800 20 8020 безкоштовно по Україні\n"
                                 "📧Email:online@ithillel.ua\n"
    , reply_markup=main_back_keyboard)
    
@dp.callback_query_handler(text='about_us')
async def process_about_us_command(call: types.CallbackQuery):
    await call.message.edit_text("Комп'ютерна школа Hillel — одна з найбільших IT-шкіл в Україні, і з кожним роком ми продовжуємо розвиватися і впроваджувати інновації у навчання."
                                "\n\nДо нас приходять і ті, хто хоче придбати нову професію або «прокачати» вже існуючі знання, і люди, які бажають підвищити свою кваліфікацію."
                                "\n\nОдним з ключових показників нашої роботи є відсоток працевлаштованих студентів. Для того, щоб цей показник був максимально високим, до викладацького складу ми запрошуємо тільки практикуючих фахівців з кращих IT-компаній, підбираємо корисні відеоматеріали і максимально комфортно організовуємо навчальний процес."
                                "\n\nЗнання допомагають змінювати життя на краще. Вчися заради мрії 🚀"
                                 , reply_markup=main_back_keyboard)


@dp.callback_query_handler(text='merch')
async def process_merch_command(call: types.CallbackQuery):
    link_button = types.InlineKeyboardMarkup(row_width=1)
    link_button.add(types.InlineKeyboardButton(text='Замовити подарунковий сертифікат', url='https://gift.ithillel.ua'))
    link_button.add(main_back_keyboard_but)
    await call.message.edit_text("Вважаєте, що інвестиція в майбутнє — це найкращий подарунок? Ми теж 😉"
                                 "\n\nТому тепер у вас є можливість подарувати радість здобування нових навичок та професій вашій коханій людині, друзям або членам родини"
                                 "\n\nКнига це кращій подарунок, а курс у Комп'ютерній школі Hillel — найкорисніший ;) "
                                , reply_markup=link_button)







