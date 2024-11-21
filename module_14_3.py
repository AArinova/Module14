from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from babel.plural import skip_token
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = "7245377370:AAHM2WCQKtOFuRQzZyuV2MakYowLQgObyyA"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

"""keyboard1"""
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="Рассчитать")
button_info = KeyboardButton(text="Информация")
button_buy = KeyboardButton(text="Купить")
kb.row(button, button_info, button_buy)

"""keyboard2"""
ib = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
button2 = InlineKeyboardButton(text="Формулы расчёта", callback_data='formulas')
ib.add(button1, button2)


"""buy keyboard3"""
ib_buy = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text="Product1", callback_data='product_buying')
btn2 = InlineKeyboardButton(text="Product2", callback_data="product_buying")
btn3 = InlineKeyboardButton(text="Product3", callback_data="product_buying")
btn4 = InlineKeyboardButton(text="Product4", callback_data="product_buying")
ib_buy.add(btn1, btn2, btn3, btn4)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for i_product in range(1, 5):
        await message.answer(f'Название: Product{i_product} | Описание: Это номер {i_product} | Цена: {i_product * 100}')
    await message.answer("Выберите продукт для покупки:", reply_markup=ib_buy)


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=ib)


@dp.message_handler(text=['Информация'])
async def main_menu(message):
    await (message.answer("Не знаю о чём Вас проинформировать.", reply_markup=ib))
           #("Тут покупают нашу божественную продукцию.", reply_markup=ib))


@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("10*ВЕС+6.25*РОСТ-5*ВОЗРАСТ-161:", reply_markup=ib)


#Создайте Inline меню из 4 кнопок с надписями . У всех кнопок назначьте callback_data="product_buying"

@dp.callback_query_handler(text='calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

"""кнопка Старт"""

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью", reply_markup=kb)


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    await UserState.weight.set()
    data = await state.get_data()
    norma = 10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) - 161
    await message.answer(f"Ваша норма калорий: {norma} Ккал в день.")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)