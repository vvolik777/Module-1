from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types.callback_query import CallbackQuery

from keyboards import keyboard, inline_keyboard, buy_menu
from products import products

import logging

logging.basicConfig(level=logging.INFO)

api = '7500178344:AAEa4jeihIn9I0OWt229UMKlFq8nKVVm8_I'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer(
        "Привет! Я бот, помогающий твоему здоровью.\n\n"
        "Выберите действие, нажав на кнопку ниже:",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=keyboard
    )


@dp.message_handler(Text(equals="Рассчитать"))
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)


@dp.callback_query_handler(Text(equals="formulas"))
async def get_formulas(call: CallbackQuery):
    formula = (
        "Формула Миффлина-Сан Жеора:\n"
        "*Для женщин*: 10 × вес (кг) + 6.25 × рост (см) - 5 × возраст (годы) - 161\n"
    )
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


@dp.message_handler(Text(equals="Купить"))
async def show_products(message: types.Message):
    for product_id, info in products.items():
        if product_id == 1:
            product_link = "https://oldsite.tiande.ru/~dRfTC"
        elif product_id == 2:
            product_link = "https://oldsite.tiande.ru/~h6yFz"
        elif product_id == 3:
            product_link = "https://oldsite.tiande.ru/~2pryn"
        elif product_id == 4:
            product_link = "https://oldsite.tiande.ru/~N0dQs"
        else:
            product_link = f"https://example.com/product/{product_id}"

        with open(f'{product_id}.png', 'rb') as img:
            product_info = (
                f"<b>Название:</b> {info['name']}\n"
                f"<b>Описание:</b> {info['description']}\n"
                f"<b>Цена:</b> <a href='{product_link}'>{info['price']} руб.</a>"
            )
            await message.answer_photo(img, product_info, parse_mode=ParseMode.HTML)

    await message.answer("Выберите продукт для покупки:", reply_markup=buy_menu)


@dp.callback_query_handler(Text(startswith="product_buying"))
async def product_bought(call: CallbackQuery):
    product_number = int(call.data.split("_")[-1])
    product_name = products[product_number]["name"]
    await call.message.answer(f"Вы успешно приобрели {product_name}!")
    await call.answer()


@dp.message_handler()
async def unknown_message(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
