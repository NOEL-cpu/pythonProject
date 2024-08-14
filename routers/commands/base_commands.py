import random
import string

from PIL import Image
from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, FSInputFile
from googletrans import Translator

import PutToDir

from RebusCouch2 import RebusImageProcessor

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="/Тренировка",)]])
    keyboard1 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="/подсказка",)]])
    await message.answer(text=f"Hello, {message.from_user.full_name}!", reply_markup=keyboard)
    await message.answer(text=f"Hello, {message.from_user.full_name}!", reply_markup=keyboard1)


@router.message(Command("help"))
async def handle_help(message: types.Message):
    text = "I'm an echo bot.\nSend me any message!"
    await message.answer(text=text)


@router.message()
async def echo_message(message: types.Message):
    await message.answer(text="I am start")
    try:
        text11 = message.text
        # Trenning
        if text11.startswith("/"):
            if text11 == '/Тренировка':
                path = 'C:\\Users\\AdminX\\PycharmProjects\\pythonProject\\folder'
                result_image_path = "D:/7 Photo/DDs-bot/result.jpg"
                rebus_processor = RebusImageProcessor(path, result_image_path)
                user_query = text11
                edited_image_path = rebus_processor.process_hint(user_query)
                if edited_image_path:
                    print(f"Редактированное изображение сохранено по пути: {edited_image_path}")
                    Image.open(edited_image_path).show()

                    while True:
                        await message.answer(text="Введите команду посказка или конец")
                        user_query = input("Введите команду ('1' или 'конец'): ")
                        if user_query == "конец":
                            break
                        elif user_query == "1":
                            edited_image_path = rebus_processor.process_hint(user_query)

                            if edited_image_path:
                                print(f"Редактированное изображение сохранено по пути: {edited_image_path}")
                                Image.open(edited_image_path).show()
                            else:
                                print("Ошибка в обработке запроса.")

        # Блок перевода
        translator = Translator()
        translator_word = translator.translate(text11, src='en', dest='ru').text
        await message.answer(translator_word)
        print(text11, translator_word)

        # Раскладка слова в директорию и ответ есть ли картинка для слова
        pathOfpictureForSendUser, InfoTxt = PutToDir.alfabet(text11)
        print('!1111!', pathOfpictureForSendUser)

        if pathOfpictureForSendUser != 'NOTPicture':
            photo22 = FSInputFile(pathOfpictureForSendUser)
            await bot.send_photo(chat_id=message.chat.id, photo=photo22)

        await message.reply(text="Количество запросов = " + str(InfoTxt))

    except ValueError as exc:
        print('Искл Value erorr1 (потому что не текст)')

    except TypeError:
        print('Отработал exeption 70 str')
        await message.reply(text="Something new 🙂")

    try:
        # Подготовка имени картинки
        base_url = "C://Users//AdminX//PycharmProjects//pythonProject//folder//bankOfPictures//"
        length = 8  # Длина случайной строки
        letters_and_digits = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(letters_and_digits) for i in range(length))
        random_filename = random_string + ".jpg"
        new_url = base_url + random_filename
        print(new_url)

    except ValueError as exc2:
        print('Искл Value erorr2 (потому что не картинка)')
