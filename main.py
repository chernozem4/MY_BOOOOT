import logging
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile
from aiogram.utils import executor
from aiogram.dispatcher.filters import Command
from dotenv import load_dotenv

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Загрузка токена из .env файла
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Список уникальных пользователей
unique_users = set()

@dp.message_handler(Command("start"))
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    if user_id not in unique_users:
        unique_users.add(user_id)
    count = len(unique_users)
    await message.answer(f"Привет, {message.from_user.first_name}! Наш бот обслуживает уже {count} пользователя(ей).")

@dp.message_handler(Command("myinfo"))
async def myinfo_handler(message: types.Message):
    user = message.from_user
    await message.answer(f"Ваш id: {user.id}\nВаше имя: {user.first_name}\nВаш никнейм: @{user.username}")

@dp.message_handler(Command("random"))
async def random_handler(message: types.Message):
    image_dir = 'images'
    random_image = random.choice(os.listdir(image_dir))
    image_path = os.path.join(image_dir, random_image)
    await message.answer_photo(InputFile(image_path))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
