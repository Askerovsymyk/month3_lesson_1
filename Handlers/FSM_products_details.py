from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from db import main_db


class Products_Details(StatesGroup):
    name_product = State()
    size = State()
    price = State()
    product_id = State()
    category = State()
    info_product = State()
    photo = State()
    collection = State()
    submit = State()


async def fsm_start(message: types.Message):
    await Products_Details.name_product.set()
    await message.answer(text="Введите название товара: ")


async def load_name_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name_product"] = message.text
    await Products_Details.next()
    await message.answer(text="Введите размер одежды")


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["size"] = message.text
    await Products_Details.next()
    await message.answer(text="Введите цену:")


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["price"] = message.text
    await Products_Details.next()
    await message.answer(text="Введите продукт id")


async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["product_id"] = message.text
    await Products_Details.next()
    await message.answer(text="Введите информацию о категории:")


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["category"] = message.text
    await Products_Details.next()
    await message.answer(text="Введите информацию о продукте:")


async def load_info_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["info_product"] = message.text
    await Products_Details.next()
    await message.answer(text="Введите коллекцию:")


async def load_collection(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["collection"] = message.text
    await Products_Details.next()
    await message.answer(text="Отправьте фотку товара")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[-1].file_id

        keyboard = InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            InlineKeyboardButton(text="yes", callback_data="yes"),
            InlineKeyboardButton(text="no", callback_data="no")
        )
        await message.answer_photo(photo=data["photo"],
                                   caption=f"Название товара: {data['name_product']}\n"
                                           f"Размер: {data['size']}\n"
                                           f"Цена: {data['price']}\n"
                                           f"Артикул: {data['product_id']}\n"
                                           f"Категория: {data['category']}\n"
                                           f"Информация о продукте: {data['info_product']}\n"
                                           f"Коллекция: {data['collection']}\n"
                                           f"Сохранить данные?",
                                   reply_markup=keyboard)

        await Products_Details.next()


async def submit(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if call.data == "yes":
            await main_db.sql_insert_oline_store(
                name_product=data["name_product"],
                size=data["size"],
                price=data["price"],
                product_id=data["product_id"],
                photo=data["photo"]
            )

            await main_db.sql_insert_products_details(
                product_id=data["product_id"],
                category=data["category"],
                info_product=data["info_product"]
            )

            await main_db.sql_insert_collection_products(
                product_id=data["product_id"],
                collection=data["collection"]
            )

            await call.message.answer("Отлично, регистрация пройдена")
            await state.finish()

        elif call.data == "no":
            await call.message.answer("Регистрация отменена")
            await call.message.delete()
            await state.finish()

        else:
            await call.message.answer(text="Выберите один из кнопак")


def register_fsm_for_products_details(Dp: Dispatcher):
    Dp.register_message_handler(fsm_start, commands="registration")
    Dp.register_message_handler(load_name_product, state=Products_Details.name_product)
    Dp.register_message_handler(load_size, state=Products_Details.size)
    Dp.register_message_handler(load_price, state=Products_Details.price)
    Dp.register_message_handler(load_product_id, state=Products_Details.product_id)
    Dp.register_message_handler(load_category, state=Products_Details.category)
    Dp.register_message_handler(load_info_product, state=Products_Details.info_product)
    Dp.register_message_handler(load_collection, state=Products_Details.collection)  # Register collection handler
    Dp.register_message_handler(load_photo, state=Products_Details.photo, content_types=["photo"])
    Dp.register_callback_query_handler(submit, state=Products_Details.submit)
