import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from app.handlers import router
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("TG_BOT_API_KEY"))
dp = Dispatcher()


async def main():
  dp.include_router(router)
  await dp.start_polling(bot)

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  asyncio.run(main())