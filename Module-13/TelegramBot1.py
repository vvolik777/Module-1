from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = 'Telegram_Token_Api'
bot = Bot(token=api)  # инициализация бота
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['Vasilisa', 'ff'])
async def vasilisa_message(message: types.Message):
    await message.answer('Vasilisa message!')


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer('Привет, рады Вас видеть!')


@dp.message_handler()
async def all_message(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
