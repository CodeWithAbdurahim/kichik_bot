from config import API_TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types

 
logging.basicConfig(level=logging.INFO)

 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Salom.  botga xush kelibsiz.")
 
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
