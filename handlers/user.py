from aiogram import types

from loader import dp




@dp.message_handler(commands=['help_user'])
async def process_help_user_command(message: types.Message):
    await message.reply("Ти натиснув /help_user. Спробуй /help_admin.")