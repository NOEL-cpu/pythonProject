import random
from PIL import Image, ImageDraw, ImageFont
from googletrans import Translator

import ScanerOOP_Bot  # Импортируем созданный ранее модуль
import os
import asyncio
import time
class RebusImageProcessor:
    def __init__(self, directory_path, result_image_path):
        self.directory_path = directory_path
        self.processor = ScanerOOP_Bot.DirectoryProcessor(directory_path) #rename like skaner OOP
        self.result_image_path = result_image_path
        self.current_image = None
        self.current_position = (0, 0)
        self.overlay_offset = 200  # Смещение для каждой новой наложенной картинки
        self.first_word = None

        # Инициализация
        self.processor.process_directory()
        self.first_image_path = None
        self.c_c = 0 #c_c count of call
        self.l_w =6  #len_word

    def alg_choose_method (self,query, method):
        method == "похожесть"
        # Логика для поиска по похожести (например, по общим буквам)
        for word in self.processor.get_top_words():
            if word.name != query.name and len(set(query.name) & set(word.name)) > 2:  # Пример логики
                return word
        return None
    def find_different_word(self, query, method):
        """Находит слово в зависимости от выбранного метода."""
        if method == "антоним":
            # Логика для поиска антонима (в примере упрощена)
            for word in self.processor.get_top_words():
                if word.name != query.name and "антоним" in word.tags:  # Предполагается, что у слова есть теги
                    return word
        elif method == "похожесть":
            # Логика для поиска по похожести (например, по общим буквам)
            for word in self.processor.get_top_words():
                if word.name != query.name and len(set(query.name) & set(word.name)) > 2:  # Пример логики
                    return word
        elif method == "автор":
            # Логика для поиска по автору (предполагается, что есть атрибут автор)
            for word in self.processor.get_top_words():
                if word.name != query.name and word.author == query.author:
                    return word
        return None

    def send_image_if_exists(self, word):
        """Если у слова есть изображение, возвращает его путь."""
        image_files = [f for f in word.files if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        if image_files:
            return word.files[image_files[0]]
        else:
            print("Изображение не найдено для этого слова.")
            return None

    def get_random_word_with_bias(self):
        """Выбирает случайное слово с прицелом на то, у которого больше просмотров."""
        words_sorted = sorted(self.processor.get_top_words(), key=lambda w: w.count, reverse=True)
        word_pool = [word for word in words_sorted for _ in range(word.count)]
        return random.choice(word_pool)

    def load_image(self):
        """Загружает текущее изображение из сохраненного файла."""
        try:
            self.current_image = Image.open(self.result_image_path)
        except FileNotFoundError:
            print(f"Файл {self.result_image_path} не найден. Начинаем с нового изображения.")
            self.current_image = None

    def save_image(self):
        """Сохраняет текущее изображение в файл."""
        if self.current_image:
           self.current_image=self.current_image.convert('RGB')
           self.current_image.save(self.result_image_path)

    def overlay_image(self, overlay_image_path):
        """Накладывает новое изображение на текущее с учетом смещения."""
        if self.current_image is None:
            print("Не загружено текущее изображение.")
            return

        overlay = Image.open(overlay_image_path)
        overlay = overlay.resize((int(self.current_image.width / 4), int(self.current_image.height / 4)))

        # Вычисление новой позиции с учетом смещения
        position = (self.current_position[0] + self.overlay_offset, self.current_position[1])
        self.current_image.paste(overlay, position)

        # Обновляем текущую позицию для следующего наложения
        self.current_position = position

    def process_hint(self, user_query):
        """Обрабатывает запрос пользователя и возвращает путь к редактированному изображению."""

        if user_query != None:
            if self.first_word is None:
                # Первый запрос на подсказку
                self.first_word = self.get_random_word_with_bias()
                self.first_image_path = self.send_image_if_exists(self.first_word)

                if self.first_image_path:
                    print(f"Первое слово: {self.first_word.name}")
                    # Открываем изображение
                    image = Image.open(self.first_image_path)
                    time.sleep(2)
                    print('1Выше этой строчки стоит таймер н 2 сек ')
                    # Создаем объект для рисования

                    # блок прорисовки текста в будующем вынести в отдельную функцию
                    # Указываем шрифт и размер текста
                    font = ImageFont.truetype("arial.ttf", 80)  # Убедитесь, что файл шрифта доступен
                    first_word=str(self.first_word.name)


                    my_translate = Translator()
                    translator_word = my_translate.translate(first_word, src='en', dest='ru').text

                    # # Размеры изображения
                    # width, height = image.size
                    #
                    # # Размеры текста
                    # #text_width, text_height = draw.textsize(translator_word, font=font)
                    #
                    # # Позиция текста (внизу посередине)
                    # position = ((width - 50) // 2, height - 100 )
                    #
                    # # Цвет текста (белый с черной обводкой)
                    # draw.text(position, translator_word, font=font, fill="white", stroke_width=2, stroke_fill="black")
                    time.sleep(2)
                    draw = ImageDraw.Draw(image)
                    time.sleep(2)
                    print('2выше сделано строп на 4 сек')
                    draw.text(
                        (150,300),translator_word,
                        # Добавляем шрифт к изображению
                        font = font,
                        fill='#1C0606')

                    #image.show()

                    # Сохраняем изображение
                    #os.remove(self.result_image_path)
                    time.sleep(2)
                    print("Before save image")
                    image.save(self.result_image_path)
                    print(f"Изображение сохранено по пути: {self.result_image_path}")
                     #
                     # self.save_image()
                     # draw_text=Image
                    return self.result_image_path
            else:
                # Выбираем случайный метод выбора слова для подсказки
                # Кроме того эта часть включается только уже для 2 го вызыва подсказок и
                # и использует уже записанный в буфере картинку
                methods = ["антоним", "похожесть", "автор", "побуквенно"]
                selected_method = random.choice(methods)
                selected_method ="похожесть"
                # еще один алгоритм выбора слова для верхнего поторения, тупо для букв картинок
                #


                letter_association = self.get_l_a(self.c_c,self.l_w)
                # временный возврат
                return
                # Загружаем текущее изображение
                self.load_image()
                different_word  = self.get_random_word_with_bias()
                if different_word:
                    print(f"Выбрано другое слово для следующей подсказки: {different_word.name} (Метод: {selected_method})")
                    overlay_image_path = self.send_image_if_exists(different_word)

                    if overlay_image_path:
                        self.overlay_image(overlay_image_path)
                        time.sleep(1)
                        self.save_image()
                        time.sleep(1)
                        return self.result_image_path
                else:
                    print("Другое слово не найдено.")
                    return None
        else:
            print("Некорректный запрос.")
            return None

    def get_l_a(self, count_call,len_word):

        name = self.first_word.name
        path3='C:\\Users\\AdminX\\PycharmProjects\\pythonProject\\folder\\'
        path4=path3+name[self.c_c]+'\\'+name[self.c_c] +'.png'
        print(path4 , " in letters ")
        if count_call < len_word-1:
            self.c_c=self.c_c + 1
            # вызываем метод который  пересохранит result.png
            self.current_image = Image.open(self.result_image_path)
            #
            self.overlay_image(path4)
            time.sleep(1)
            self.save_image()
            time.sleep(1)

    pass

# Не забывай что выше это класс, и отступы для деф на 1 tab

def collect_images(directory):
    image_extensions = ('.jpg', '.png', '.gif')
    collection = {}

    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        if os.path.isdir(folder_path) and folder_name.isascii() and len(folder_name) == 1:
            for file_name in os.listdir(folder_path):
                if file_name.lower().endswith(image_extensions):
                    file_path = os.path.join(folder_path, file_name)
                    symbol = folder_name.upper()
                    if symbol in collection:
                        collection[symbol].append(file_path)
                    else:
                        collection[symbol] = [file_path]

    return collection

def match_word_with_images(word, image_collection):
    matched_images = []
    for letter in word.upper():
        if letter in image_collection:
            # Берем первое изображение из списка, соответствующего букве
            matched_images.append(image_collection[letter][0])
        else:
            # Если буквы нет в коллекции, добавляем None или placeholder
            matched_images.append(None)
    return matched_images

async def some_async_function():
    print("Start sleeping...")
    await asyncio.sleep(5)  # Ожидание 3 секунды
    print("Awake now!")

def get_l_a(self):
    scaner_OOP=self.processor()

    f_w=self.first_word()
     # scaner_OOP.
    # тут надо взять первое слова разложить его по буквам, положить его  в счетичик вызовов подсказок в self области
    # далее иторировать  по букве, но делать это выше, или в другой функции.
    #хотя создание списка  где уже каждой букве соответствует адрсс может и


def main():
    # Инициализация класса для работы с изображениями
    # Настроен на рботу с aiogramm, main нужен лишь для для дебага
    # нужно стремится к тому что после отработки данной функции, происходила
    # загрузка картинки в тг

    path = 'C:\\Users\\AdminX\\PycharmProjects\\pythonProject\\folder'
    result_image_path = "D:\\7 Photo\\DDs-bot\\result.jpg"
    rebus_processor = RebusImageProcessor(path, result_image_path) #Инициализация
    collect_images_main = collect_images(path)
  #  word= get randonm word with big counter
    word = "hello"
    matched_images_main = match_word_with_images(word, collect_images_main)

#############################
    # Первый шаг: выбрать случайное слово и отправить картинку
    user_query = 'hello'
    edited_image_path = rebus_processor.process_hint(user_query)

    if edited_image_path:
        print(f"Редактированное изображение сохранено по пути: {edited_image_path}")
     #   Image.open(edited_image_path).show()
     #!?! Передать наверх картинку отредактированную, но при этом при команде пользователя продолжить, программа
    # должна знать. что это уже не первая подсказка и пользователю надо сместить на сколько, то картинку подсказку

    # Второй шаг: Обработка следующих запросов на подсказки
    user_count=0
    user_query="apple"
    while True:

        if   user_count >= 4:
            break
        user_count =+ 1

        edited_image_path = rebus_processor.process_hint(user_query)

        if edited_image_path:
            print(f"Редактированное изображение сохранено по пути: {edited_image_path}")
            Image.open(edited_image_path).show()
        else:
            print("Ошибка в обработке запроса.")

if __name__ == "__main__":
    main()
