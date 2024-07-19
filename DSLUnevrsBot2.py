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


# @dp.message()
# async def send_image_to_telegram(image_path, chat_id):
# Открываем изображение
# with open(image_path, 'rb') as photo:
# Отправляем изображение через бота
#  await bot.send_photo(chat_id=message.chat.id, photo)



@dp.message()
async def echo_message(message: types.Message):  # эта функция вызвывается  каждый раз когда в тг что то проискходит
    """

    :type message: object
    """
    await message.answer(
        text="I am start ",)
#33Блок блок отсылки картинки
    photo22 = FSInputFile('D://1.2PythonTelegBot Dss//apple.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo22)
#33end
    # try:
    #
    #      with open('D://1.2PythonTelegBot Dss//apple.jpg') as photofile:
    #         chat_id1 = message.chat.id
    #         print('2222', chat_id1)
    #         print('3333',type(photofile))
    #
    #      await bot.send_photo(chat_id=chat_id1, photo=photofile)
    #      await message.answer_photo(photofile, caption="new phpoto")
    # except Exception as e:
    #      await message.reply(f"Произошла ошибка: {e}")
    #
    # try:
    #     photo22=InputFile('D://1.2PythonTelegBot Dss//apple.jpg')
    #
    #     await message.answer_photo(photo22, caption="new phpoto")
    #
    #


    await message.send_copy(chat_id=message.chat.id)
    text11 = message.text
#блок перевода
    translator = Translator()
    translator_word = translator.translate(text11, src='en', dest='ru').text
    await message.answer(translator_word)
    print(text11, translator_word)
#блок перевода end
    #
    # with open("C:/Users/AdminX/PycharmProjects/pythonProject/folder/l/lie/lie.jpg", 'rb') as photofile:
    #         await bot.send_photo(photo= photofile)
    #     pathOfpictureForSendUser='NOTPicture'
    #     pathOfpictureForSendUser =PutToDir.alfabet(text11)
    #
    #     if(pathOfpictureForSendUser != 'NOTPicture'):
    #       #  photo = InputFile(pathOfpictureForSendUser)
    #         await message.reply_photo(photo='C:/Users/AdminX/PycharmProjects/pythonProject/folder/l/lie/lie.jpg')

#блок отправки картинки пользователю если она есть


    # except ValueError as exc:
    #     print('Искл  Value erorr1 (потому что не текст')
    #   #  print(repr(exc.errors()[0]['type']))
    #
    # except TypeError:
    #     print('отработал exeption 70 str')
    #     await message.reply(text="TypeError wrong 🙂")
    #     print("3")

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
    print("0 !!! Sn programm started")
