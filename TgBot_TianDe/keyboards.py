from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Рассчитать"), KeyboardButton("Информация"))
keyboard.add(KeyboardButton("Купить"))

inline_keyboard = InlineKeyboardMarkup(row_width=1)
inline_keyboard.add(
    InlineKeyboardButton("Рассчитать норму калорий", callback_data="calories"),
    InlineKeyboardButton("Формула расчёта", callback_data="formulas")
)

buy_menu = InlineKeyboardMarkup(row_width=1)
buy_menu.add(
    InlineKeyboardButton("Белковый коктейль", callback_data="product_buying_1"),
    InlineKeyboardButton("Имбирный чай", callback_data="product_buying_2"),
    InlineKeyboardButton("Слимчай", callback_data="product_buying_3"),
    InlineKeyboardButton("Фитоформула", callback_data="product_buying_4")
)
