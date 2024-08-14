from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

ADMIN_ID = 1234567


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def send_to_admin(message: types.Message):
    await bot.send_photo(chat_id=ADMIN_ID, photo=message.photo[-1].file_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
