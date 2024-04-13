import asyncio
import logging

from googletrans import Translator
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command
import PutToDir
import countOpenWordInfo


BOT_TOKEN = "5836801048:AAHrAtSk4LuGMQlITBn6Q3Cz91HxL_1mv94"
dp = Dispatcher()  # шлет  уведомления от телеграм в наш бот, т.е занимается обработкой событий


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f"Hello, {message.from_user.full_name}!")


@dp.message(Command("help"))
async def handle_help(message: types.Message):
    text = "I'm and echo bot.\nSend me any message!"
    await message.answer(text=text)


@dp.message()
async def echo_message(message: types.Message):  # эта функция вызвывается  каждый раз когда в тг что то проискходит
    # await bot.send_message(
    #     chat_id=message.chat.id,
    #     text="Start processing...",
    # )
    # await bot.send_message(
    #     chat_id=message.chat.id,
    #     text="Detected message...",
    #     reply_to_message_id=message.message_id,
    # )

    await message.answer(
        text="Wait a second...",
    )
    try:

        await message.send_copy(chat_id=message.chat.id)
        text11 = message.text
#блок перевода
        translator = Translator()
        translator_word = translator.translate(text11, src='en', dest='ru').text
        await message.answer(translator_word)

        print(text11, translator_word)
#блок перевода end
        PutToDir.alfabet(text11)
        print("2")
    except TypeError:
        await message.reply(text="Something new 🙂")
        print("3")


async def main():
    logging.basicConfig(level=logging.DEBUG)
    bot = Bot(token=BOT_TOKEN)  # Экзэмпляр бот
    print("0")
    await dp.start_polling(bot)  # polling - это опрос  #?dp. это диспачер был описан вначале

    print("1")


if __name__ == "__main__":
    asyncio.run(main())
    print("4")
