import random
import string
import time

from PIL import Image
from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, FSInputFile
from aiogram.enums import ParseMode
from aiogram.utils import markdown

from keyboards.common_keyboards import (
    ButtonText,
    get_on_start_kb,
    get_on_help_kb,
    get_actions_kb,
)
from keyboards.inline_keyboards.info_kb import build_info_kb

from googletrans import Translator

import PutToDir

from RebusCouch2 import RebusImageProcessor

router = Router(name=__name__)

Sesions={}

@router.message(CommandStart())
async def handle_start(message: types.Message):
    # идинтификация пользователя

    # Создаем клавиатуру с двумя кнопками
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="/My progress"      ),
             KeyboardButton(text="/flashCardsStart"  ),
             KeyboardButton(text="/Memloud"          )]

        ],
        resize_keyboard=True  # Делает кнопки меньше, чтобы они соответствовали размеру экрана
    )

    # Отправляем одно сообщение с клавиатурой
    await message.answer(
        text=f"Hello, {message.from_user.full_name}!",
        reply_markup=keyboard
    )


@router.message(Command("help"))
async def handle_help(message: types.Message):
    text = "I'm an echo bot.\nSend me any message!"
    await message.answer(text=text)

@router.message(Command("Тренировка"))
async def handle_traning(message: types.Message):
    await message.answer(text="Тренировка началась")
    path = 'C:\\Users\\AdminX\\PycharmProjects\\pythonProject\\folder'
    result_image_path = "D:\\7 Photo\\DDs-bot\\4.png"
    rebus_processor = RebusImageProcessor(path, result_image_path)
    Sesions[message.from_user.id]=rebus_processor #передали обьект класса в глобальную среду
    # user_query = text11 тут не используется слово, набор будет
    rebus_processor.process_hint(1)

    await message.answer(text="Выбираю")
    await message.answer(text="Я обратился в твою базу знаний")
    # collect_images_main = collect_images(path)
    photo1 = FSInputFile('D:\\7 Photo\\DDs-bot\\4.png')
    time.sleep(1)
    await message.answer(text="Я подумал")
    await message.answer_photo(photo=photo1)
    await message.answer(text="если вы не разгадали слово то вы можете воспользоваться подсказкой")
    await message.answer(text="ввести ответ:")

@router.message(Command("подсказка"))
async def resume_traning(message: types.message):
    await message.answer(text="Тренировка продолжается")
    path = 'C:\\Users\\AdminX\\PycharmProjects\\pythonProject\\folder'
    result_image_path = "D:\\7 Photo\\DDs-bot\\result.jpg"
    user_try = 0
    rebus_processor2=Sesions[message.from_user.id] # получили  обьект класса из глобальной среды
    
    rebus_processor2.process_hint(user_query="2")
    await message.answer(text="Я думаю")
    photo1 = FSInputFile('D:\\7 Photo\\DDs-bot\\4.png')
    await message.answer_photo(photo=photo1)

    # серриализация(сохранение) информации о текущем обекте для последующей тренировки ...info.txt


    # while True:
    #     if user_try >= 4:
    #         break
    #     user_try = + 1
    #     rebus_processor2.process_hint(1)
    #     photo2 = FSInputFile('D:\\7 Photo\\DDs-bot\\result.jpg')
    #     await message.answer_photo(photo=photo2)

@router.message(Command("Конец"))
async def handle_traning(message: types.Message):
     await message.answer(text="я удаляю предыдущюю тренировку")
     rebus_processor_end=Sesions[message.from_user.id]
     rebus_processor_end.__del__()



@router.message(Command("more", prefix="!/"))
async def handle_more(message: types.Message):
    markup = get_actions_kb()
    await message.answer(
        text="Choose action:",
        reply_markup=markup,
    )

@router.message(Command("more", prefix="!/"))
async def handle_more(message: types.Message):
    markup = get_actions_kb()
    await message.answer(
        text="Choose action:",
        reply_markup=markup,
    )


@router.message(Command("flashCardsStart"))
# Обработчик команды "flashCardsStart"
async def handle_training(message: types.Message):
    await message.answer(text="Тренировка началась")

    # Указание путей для работы с изображениями
    path = 'C:\\Users\\AdminX\\PycharmProjects\\pythonProject\\folder'
    result_image_path = "D:\\7 Photo\\DDs-bot\\4.png"

    # Имитация работы с классом RebusImageProcessor
    # Предположим, что он создает какое-то изображение
    # Вам нужно будет интегрировать ваш класс RebusImageProcessor сюда
    # rebus_processor = RebusImageProcessor(path, result_image_path)
    # Sesions[message.from_user.id] = rebus_processor  # Сохраняем объект класса в глобальной среде
    # rebus_processor.process_hint(1)  # Обрабатываем подсказку

    await message.answer(text="Выбираю")
    await message.answer(text="Я обратился в твою базу знаний")

    # Загружаем изображение
    photo = FSInputFile(result_image_path)

    # Подождем немного (если это нужно)
    time.sleep(1)

    await message.answer(text="Я подумал")

    # Создаем инлайн-клавиатуру с 5 кнопками
    markup = get_actions_kb()
    # Отправляем фото с текстом и инлайн-клавиатурой
    sent_message = await message.answer_photo(
        photo=photo,
        caption="Это ваша картинка и описание с выбором кнопок.",
        reply_markup=markup,
        reply_to_message_id=message.message_id  # Отправляем как ответ на сообщение пользователя
    )

    # Возвращаем ID отправленного сообщения
    sent_message_id = sent_message.message_id
    await message.answer(text=f"ID этого сообщения: {sent_message_id}")

    # Этот ID можно сохранить для будущих ответов, например, в базе данных или глобальном словаре
    # Например: Sessions[message.from_user.id]["last_message_id"] = sent_message_id


@router.message()
async def echo_message(message: types.Message):
    await message.answer(text="I am start")
    try:

        text11 = message.text
        await message.answer(text11)
        # Trenning
        await message.answer(text="1")


        # Блок перевода
        translator = Translator()
        translator_word = translator.translate(text11, src='en', dest='ru').text
        await message.answer(translator_word)
        # print(text11, translator_word)

        # Раскладка слова в директорию и ответ есть ли картинка для слова
        pathOfpictureForSendUser, InfoTxt = PutToDir.alfabet(text11)
        print(pathOfpictureForSendUser)

        if pathOfpictureForSendUser != 'NOTPicture':
            photo22 = FSInputFile(pathOfpictureForSendUser)
          #  photo22 = 'D:/7 Photo/DDs-bot/1.jpg'
            await message.answer_photo( photo=photo22)

        await message.reply(text="Количество запросов = " + str(InfoTxt))

    except ValueError as exc:
        print(exc.with_traceback())
        print('Искл Value erorr1 (потому что не текст)')

    except TypeError as exc:
        print('Отработал exeption 70 str', exc.with_traceback())
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


