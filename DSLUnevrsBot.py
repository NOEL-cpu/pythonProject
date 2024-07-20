import asyncio
import logging
import string
import random

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile

from aiogram.types import callback_query
from googletrans import Translator

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

@dp.message()
async def echo_message(message: types.Message):  # эта функция вызвывается  каждый раз когда в тг что то проискходит

    await message.answer(
        text="I am start",)
    try:
        text11 = message.text
#блок перевода
        translator = Translator()
        translator_word = translator.translate(text11, src='en', dest='ru').text
        await message.answer(translator_word)
        print(text11, translator_word)
#блок перевода end
#67 Раскладка слова в директорию и ответ есть ли картинка для слова.
        pathOfpictureForSendUser='NOTPicture'
        InfoTxt=0
        pathOfpictureForSendUser, InfoTxt =PutToDir.alfabet(text11)
        print('!1111!',pathOfpictureForSendUser)

        if(pathOfpictureForSendUser != 'NOTPicture'):
            #33Блок блок отсылки картинки
            photo22 = FSInputFile(pathOfpictureForSendUser)
            await bot.send_photo(chat_id=message.chat.id, photo=photo22)

        await message.reply(text="Количество запросов = " + str(InfoTxt))
#end67

    except ValueError as exc:
        print('Искл  Value erorr1 (потому что не текст')
      #  print(repr(exc.errors()[0]['type']))

    except TypeError:
        print('отработал exeption 70 str')
        await message.reply(text="Something new 🙂")
        print("3")

    try:
        #65 подготовка имени картинки
        # Базовый URL
        base_url = "C://Users//AdminX//PycharmProjects//pythonProject//folder//bankOfPictures//"
        #D://1.2PythonTelegBot Dss//
        # Генерация случайной строки
        length = 8  # Длина случайной строки
        letters_and_digits = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(letters_and_digits) for i in range(length))
        # Формирование имени файла
        random_filename = random_string + ".jpg"
        # Генерация нового URL
        new_url = base_url + random_filename
        # Вывод нового URL
        print(new_url)
        #65 end

        #66 блок загрузки картинки
        await bot.download(message.photo[-1], destination=new_url)
         #   print (type(message.photo))
        print("отпавка фото успешно")
        #66
    except ValueError as exc2:
        print('Искл  Value erorr2 (потому что не картинка')



async def main():
    logging.basicConfig(level=logging.DEBUG)
    print("0")
    await dp.start_polling(bot)  # polling - это опрос  #?dp. это диспачер был описан вначале

    print("1")


if __name__ == "__main__":
    asyncio.run(main())
    print("4")
