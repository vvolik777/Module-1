from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types.callback_query import CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import keyboard, inline_keyboard, buy_menu
from products import products
from crud_functions import initiate_db, get_all_products, add_user, is_included

import logging

logging.basicConfig(level=logging.INFO)

api = 'Token_Api'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer(
        "Привет! Я бот, помогающий твоему здоровью.\n\n"
        "Выберите действие, нажав на кнопку ниже:",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=keyboard
    )


@dp.message_handler(Text(equals="Регистрация"))
async def sing_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя.")
        return
    await state.update_data(username=username)
    await message.answer("Введите свой email:")
    await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом.")
        await state.update_data(age=age)

        user_data = await state.get_data()
        username = user_data['username']
        email = user_data['email']

        add_user(username, email, age)

        await message.answer(f"Вы успешно зарегистрированы! Добро пожаловать, {username}.")
        await state.finish()

        await start_message(message)

    except ValueError:
        await message.answer("Пожалуйста, введите корректный возраст (целое положительное число).")


@dp.message_handler(Text(equals="Рассчитать"))
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)


@dp.callback_query_handler(Text(equals="formulas"))
async def get_formulas(call: CallbackQuery):
    formula = ("Формула Миффлина-Сан Жеора:\n"
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


initiate_db()

links = {
    "Фитоформула": {"url": "https://oldsite.tiande.ru/~N0dQs", "image": "4.png"},
    "Белковый коктейль": {"url": "https://oldsite.tiande.ru/~dRfTC", "image": "1.png"},
    "Слимчай": {"url": "https://oldsite.tiande.ru/~2pryn", "image": "3.png"},
    "Имбирный чай": {"url": "https://oldsite.tiande.ru/~h6yFz", "image": "2.png"},
}


@dp.message_handler(Text(equals="Купить"))
async def show_products(message: types.Message):
    products = get_all_products()

    if not products:
        await message.answer("На данный момент нет доступных продуктов.")
        return

    for product in products:
        product_id, title, description, price = product

        product_links = links.get(title, {"url": "https://example.com", "image": None})
        product_url = product_links["url"]
        product_image = product_links["image"]

        product_info = (
            f"*Название:* {title}\n"
            f"*Описание:* {description}\n"
            f"*Цена:* [{price} руб.]({product_url})"
        )

        if product_image:
            try:
                with open(f"images/{product_image}", 'rb') as photo:
                    await bot.send_photo(
                        chat_id=message.chat.id,
                        photo=photo,
                        caption=product_info,
                        parse_mode=ParseMode.MARKDOWN
                    )
            except FileNotFoundError:
                await message.answer(f"Изображение для {title} не найдено.")
        else:
            await message.answer(product_info, parse_mode=ParseMode.MARKDOWN)

    await message.answer("Выберите продукт для покупки:", reply_markup=buy_menu)


@dp.callback_query_handler(Text(startswith="product_buying"))
async def product_bought(call: CallbackQuery):
    product_id = int(call.data.split("_")[-1])
    products = get_all_products()
    product = next((p for p in products if p[0] == product_id), None)

    if not product:
        await call.message.answer("Ошибка: выбранный продукт не найден.")
        return

    title = product[1]
    await call.message.answer(f"Вы успешно приобрели {title}!")
    await call.answer()


@dp.message_handler()
async def unknown_message(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
