#__all__ = ("router")    # контроль при экспорте какие функци будут экспортированы
import asyncio
import logging

from aiogram import Bot, Dispatcher

# ProjectLibrary
from routers import router as main_router

from aiogram.enums import ParseMode

BOT_TOKEN = "5836801048:AAHrAtSk4LuGMQlITBn6Q3Cz91HxL_1mv94"




async def main():
    dp = Dispatcher()
    logging.basicConfig(level=logging.DEBUG)
    print("0")
    bot = Bot(token=BOT_TOKEN)  # Экзэмпляр бот
    dp.include_router(main_router)
    # Создаем диспетчер и регистрируем роутер

    await dp.start_polling(bot)
    print("Начался polling")

if __name__ == "__main__":
    asyncio.run(main())
    print("4 кстати интересно когда срабатывает")
