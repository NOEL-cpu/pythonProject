import random
from PIL import Image
import ScanerOOP_Bot  # Импортируем созданный ранее модуль

def find_different_word(query, words):
    """Находит слово, которое не совпадает с текущим словом."""
    for word in words:
        if word.name != query.name:
            return word
    return None

def send_image_if_exists(word):
    """Если у слова есть изображение, отправляем его."""
    image_files = [f for f in word.files if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    if image_files:
        image_path = word.files[image_files[0]]
        # Здесь открываем и показываем изображение как пример, в реальном боте вы отправите его пользователю
        image = Image.open(image_path)
        image.show()
        return image_path
    else:
        print("Изображение не найдено для этого слова.")
        return None

def get_random_word_with_bias(words):
    """Выбирает случайное слово с прицелом на то, у которого больше просмотров."""
    # Сортируем слова по количеству просмотров (count), чтобы слова с большим count имели больше шансов быть выбраны
    words_sorted = sorted(words, key=lambda w: w.count, reverse=True)
    # Создаем список, где более популярные слова встречаются чаще
    word_pool = [word for word in words_sorted for _ in range(word.count)]
    return random.choice(word_pool)

# Путь к директории
path = 'C:\\Users\\AdminX\\PycharmProjects\\pythonProject\\folder'
processor = ScanerOOP_Bot.DirectoryProcessor(path)
processor.process_directory()

# Сохраняем первое случайно выбранное слово и изображение
first_word = get_random_word_with_bias(processor.get_top_words())
first_image_path = send_image_if_exists(first_word)

if first_image_path:
    print(f"Первое слово: {first_word.name}")

# Обработка второго запроса на подсказку
user_query = "подсказка"  # Второй пользовательский запрос на подсказку

if user_query == "подсказка":
    different_word = find_different_word(first_word, processor.get_top_words())
    if different_word:
        print(f"Выбрано другое слово для второй подсказки: {different_word.name}")
        overlay_image_path = send_image_if_exists(different_word)

        if overlay_image_path:
            # Дополнительная обработка изображения, если оно было найдено
            background = Image.open(first_image_path)
            overlay = Image.open("D:/7 Photo/DDs-bot/4.png")
           # overlay = Image.open(overlay_image_path)

            # Получаем размеры основного изображения
            bg_width, bg_height = background.size

            # Изменяем размер накладываемого изображения (если нужно)
            overlay = overlay.resize((int(bg_width / 4), int(bg_height / 4)))  # Масштабирование до 1/4 размера основного изображения

            # Выбираем позицию для накладываемого изображения (например, сверху справа)
            position = (bg_width - overlay.width, 0)

            # Наложение изображений
            background.paste(overlay, position, overlay)

            # Сохранение результата
            result_image_path = "D:/7 Photo/DDs-bot/result.jpg"
            background.save(result_image_path)

            # Вывод результата
            background.show()
else:
    print("Другое слово не найдено.")
