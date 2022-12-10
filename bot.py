import time
import logging
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)
MSG1 = "{}, ты выделил время на постановку целей сегодня?"
MSG2 = "{}, Ты выделил время на учебу сегодня? "

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot) 

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id= } {user_full_name= } {time.asctime()}')
    await message.reply(f"Привет, {user_full_name}")

    for i in range (180):  # здесь количество дней, в течение которых бот будет выполнять работу
           time.sleep(2)  # здесь количество секунд, через которые бот будет повторять сообщение.здеь каждые 2 секунды
           #time.sleep(60*60*24)  # здесь количество секунд, через которые бот будет повторять сообщение. здесь расчетно раз в сутки
           await bot.send_message(user_id, MSG1.format(user_name))
           time.sleep(1)
           await bot.send_message(user_id, MSG2.format(user_name))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
