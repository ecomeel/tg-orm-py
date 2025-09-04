from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.requests as rq

router = Router()

@router.message(CommandStart())
async def greeting(message: Message):
  await rq.set_user(message.from_user.id)
  await message.answer("Добро пожаловать в магазин кроссовок!", reply_markup=kb.main)

@router.message(F.text == "Каталог")
async def open_catalog(message: Message):
  await message.answer("Выберите категорию товара", reply_markup=await kb.categories())

@router.callback_query(F.data.startswith("category_"))
async def category(callback: CallbackQuery):
  await callback.answer("Вы выбрали категорию")
  await callback.message.answer("Выберите товар",
                                reply_markup=await kb.category_items(callback.data.split("_")[1]))
  
@router.callback_query(F.data.startswith("item_"))
async def category(callback: CallbackQuery):
  seleted_item = await rq.get_item(callback.data.split("_")[1])
  await callback.answer("Вы выбрали товар")
  await callback.message.answer(f"Название: {seleted_item.name}\nЦены: {seleted_item.price} р.\nОписание: {seleted_item.description}")