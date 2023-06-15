from aiogram import types

from loader import dp


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привіт!\nНатисни /help щоб дізнатись що я вмію.")
    











