from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_categories, get_category_items

main = ReplyKeyboardMarkup(keyboard=[
  [
    KeyboardButton(text="Каталог"),
    KeyboardButton(text="Корзина"),
  ],
  [
    KeyboardButton(text="Контакты"),
    KeyboardButton(text="О нас")
  ]
])

async def categories():
  all_categories = await get_categories()
  keyboard = InlineKeyboardBuilder()
  for category in all_categories:
    keyboard.add(InlineKeyboardButton(
      text=category.name, 
      callback_data=f"category_{category.id}"
    ))
  keyboard.add(InlineKeyboardButton(text="На главную", callback_data="to_main"))
  return keyboard.adjust(2).as_markup()

async def category_items(category_id):
  category_items = await get_category_items(category_id)
  keyboard = InlineKeyboardBuilder()
  for item in category_items:
    keyboard.add(InlineKeyboardButton(
      text=item.name, 
      callback_data=f"item_{item.id}"
    ))
  keyboard.add(InlineKeyboardButton(text="На главную", callback_data="to_main"))
  return keyboard.adjust(2).as_markup()