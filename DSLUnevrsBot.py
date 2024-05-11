import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command

from aiogram.types import callback_query

import PutToDir
import countOpenWordInfo
from Translator import translator

BOT_TOKEN = "5836801048:AAHrAtSk4LuGMQlITBn6Q3Cz91HxL_1mv94"
dp = Dispatcher()  # шлет  уведомления от телеграм в наш бот, т.е занимается обработкой событий

bot = Bot(token=BOT_TOKEN)  # Экзэмпляр бот


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f"Hello, {message.from_user.full_name}!")


@dp.message(Command("help"))
async def handle_help(message: types.Message):
    text = "I'm and echo bot.\nSend me any message!"
    await message.answer(text=text)


# @dp.message()
# async def send_image_to_telegram(image_path, chat_id):
# Открываем изображение
# with open(image_path, 'rb') as photo:
# Отправляем изображение через бота
#  await bot.send_photo(chat_id=message.chat.id, photo)


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
        text="I am ready",
    )
    try:

        path1111 = str('D:/1.2PythonTelegBot Dss/apple.png')
        # 'C:/Users/AdminX/PycharmProjects/pythonProject//folder/a/apple/apple.png'
        chat_id = message.chat.id
        chat_id_str = str(chat_id)
        print("1блок отправки 111")
        print(chat_id_str,chat_id,'object(chat_id_str)')
        with open(path1111, "rb") as photo_file:
            print('2файл открыт в  8 бит обьекте')
            print('3ff', photo_file)
            #photo_obj = types.file(path1111)

            # await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_file)
            # photo = InputFile("files/any_picture.png")
            print("4!!!!!!!!!", type(message.chat.id), message.chat.id,)
            print('5    ',chat_id_str)
            #await message.answer_document(photo_file)
            #   await message.answer_photo(photo_file)

            await bot.send_photo(chat_id ,photo = photo_file)
           # await bot.send_photo(chat_id_str, photo= photo_obj)

            #  await send_image_to_telegram(path1111, chat_id)

            print("1000отпавка фото успешно")
        await translator(message)
    except ValueError as exc:
        print('Искл  Value erorr1')
        print(repr(exc.errors()[0]['type']))

    except TypeError:
        print('отработал exeception 70 str')
        await message.reply(text="Something new 🙂")
        print("3")


async def main():
    logging.basicConfig(level=logging.DEBUG)
    print("0")
    await dp.start_polling(bot)  # polling - это опрос  #?dp. это диспачер был описан вначале

    print("1")


if __name__ == "__main__":
    asyncio.run(main())
    print("4")
