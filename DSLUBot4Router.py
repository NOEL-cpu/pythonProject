#__all__ = ("router",)    # контроль при экспорте какие функци будут экспортированы
import asyncio
import logging

from aiogram import Bot, Dispatcher, Router

# ProjectLibrary
from routers import router as main_router



#
async def main():
    logging.basicConfig(level=logging.DEBUG)
    print("0")


    # Создаем диспетчер и регистрируем роутер
    dp = Dispatcher()
    dp.include_router(main_router)
    BOT_TOKEN = "5836801048:AAHrAtSk4LuGMQlITBn6Q3Cz91HxL_1mv94"
    bot = Bot(token=BOT_TOKEN)  # Экзэмпляр бот

    await dp.start_polling(bot)
    print("1")

if __name__ == "__main__":
    asyncio.run(main())
    print("4 кстати интересно когда срабатывает")
