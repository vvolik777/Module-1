from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types.callback_query import CallbackQuery

import logging

logging.basicConfig(level=logging.INFO)

api = 'Telegram_Token_Api
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Рассчитать"), KeyboardButton("Информация"))

inline_keyboard = InlineKeyboardMarkup(row_width=1)
inline_keyboard.add(
    InlineKeyboardButton("Рассчитать норму калорий", callback_data="calories"),
    InlineKeyboardButton("Формула расчёта", callback_data="formulas"))


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.\n\n"
                         "Выберите действие, нажав на кнопку ниже:",
                         parse_mode=ParseMode.MARKDOWN,
                         reply_markup=keyboard)


@dp.message_handler(Text(equals="Рассчитать"))
async def main_menu(message: types.Message):
    # Отправляем Inline меню
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)


@dp.callback_query_handler(Text(equals="formulas"))
async def get_formulas(call: CallbackQuery):
    formula = ("Формула Миффлина-Сан Жеора:\n"
               "*Для женщин*: 10 × вес (кг) + 6.25 × рост (см) - 5 × возраст (годы) - 161\n")
    await call.message.answer(formula, parse_mode=ParseMode.MARKDOWN)
    await call.answer()


@dp.callback_query_handler(Text(equals="calories"))
async def set_age(call: CallbackQuery):
    await UserState.age.set()
    await call.message.answer("Введите свой возраст:")
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом.")
        await state.update_data(age=age)
        await UserState.growth.set()
        await message.answer("Введите свой рост (в см):")
    except ValueError:
        await message.answer("Пожалуйста, введите корректный возраст (целое положительное число).")


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    try:
        growth = int(message.text)
        if growth <= 0:
            raise ValueError("Рост должен быть положительным числом.")
        await state.update_data(growth=growth)
        await UserState.weight.set()
        await message.answer("Введите свой вес (в кг):")
    except ValueError:
        await message.answer("Пожалуйста, введите корректный рост (целое положительное число).")


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    try:
        weight = int(message.text)
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом.")
        await state.update_data(weight=weight)

        data = await state.get_data()
        age = data['age']
        growth = data['growth']

        calories = 10 * weight + 6.25 * growth - 5 * age - 161  # Формула для женщин

        await message.answer(f"Ваша норма калорий: {calories:.2f} ккал")
        await state.finish()
    except ValueError:
        await message.answer("Пожалуйста, введите корректный вес (целое положительное число).")


@dp.message_handler()
async def unknown_message(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
