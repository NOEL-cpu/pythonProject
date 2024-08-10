import random
from PIL import Image
import ScanerOOP_Bot  # Импортируем созданный ранее модуль

class RebusImageProcessor:
    def __init__(self, directory_path, result_image_path):
        self.directory_path = directory_path
        self.processor = ScanerOOP_Bot.DirectoryProcessor(directory_path)
        self.result_image_path = result_image_path
        self.current_image = None
        self.current_position = (0, 0)
        self.overlay_offset = 20  # Смещение для каждой новой наложенной картинки
        self.first_word = None

        # Инициализация
        self.processor.process_directory()
        self.first_image_path = None

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
        self.current_image.paste(overlay, position, overlay)

        # Обновляем текущую позицию для следующего наложения
        self.current_position = position

    def process_hint(self, user_query):
        """Обрабатывает запрос пользователя и возвращает путь к редактированному изображению."""
        if user_query == "подсказка":
            if self.first_word is None:
                # Первый запрос на подсказку
                self.first_word = self.get_random_word_with_bias()
                self.first_image_path = self.send_image_if_exists(self.first_word)

                if self.first_image_path:
                    print(f"Первое слово: {self.first_word.name}")
                    self.current_image = Image.open(self.first_image_path)
                    self.save_image()
                    return self.result_image_path
            else:
                # Выбираем случайный метод выбора слова для подсказки
                methods = ["антоним", "похожесть", "автор"]
                selected_method = random.choice(methods)

                # Загружаем текущее изображение
                self.load_image()
                different_word = self.find_different_word(self.first_word, selected_method)
                if different_word:
                    print(f"Выбрано другое слово для следующей подсказки: {different_word.name} (Метод: {selected_method})")
                    overlay_image_path = self.send_image_if_exists(different_word)

                    if overlay_image_path:
                        self.overlay_image(overlay_image_path)
                        self.save_image()
                        return self.result_image_path
                else:
                    print("Другое слово не найдено.")
                    return None
        else:
            print("Некорректный запрос.")
            return None


def main():
    # Инициализация класса для работы с изображениями
    path = 'C:\\Users\\AdminX\\PycharmProjects\\pythonProject\\folder'
    result_image_path = "D:/7 Photo/DDs-bot/result.jpg"
    rebus_processor = RebusImageProcessor(path, result_image_path)

    # Первый шаг: выбрать случайное слово и отправить картинку
    user_query = "подсказка"
    edited_image_path = rebus_processor.process_hint(user_query)

    if edited_image_path:
        print(f"Редактированное изображение сохранено по пути: {edited_image_path}")
        Image.open(edited_image_path).show()

    # Второй шаг: Обработка следующих запросов на подсказки
    while True:
        user_query = input("Введите команду ('подсказка' или 'конец'): ")
        if user_query == "конец":
            break

        edited_image_path = rebus_processor.process_hint(user_query)

        if edited_image_path:
            print(f"Редактированное изображение сохранено по пути: {edited_image_path}")
            Image.open(edited_image_path).show()
        else:
            print("Ошибка в обработке запроса.")

if __name__ == "__main__":
    main()
