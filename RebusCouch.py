#получить пути которые в обектах класса Word.
#1 обьект  , получить его  потом произвести анализ слова
#т.е поискать слова похожие по начало этого слова ...расширить... но пока
# так же что бы у этого слва была инфо наполненность.те картинка или антонимы
# процедура рандомного выбора из 3ех вариантов 1картинка похожее(докидывание ) по совпадению букв.
# 2 по антониму и наличию картинок +ребус (модификация картинки)
# 3 ... после анализа твоих фото
# 4 после балаганного анализа твоих картинкок
# 5 фраза демотиватор !!! возможно это другая тренировка. Но as for as.. и тд предлоги


# 2.6 ИНСТРУМЕНТ СОЗДАНИЯ СКРЫТОГО  эТАЛОНОГО Сущности
# 2.7 выбор метода по которому будет осуществлена перересовка картинки
# 2.8 перересовка картинки
# 3 выдача модернезированной картинки
# ожидание от пользователя  воода или правильного слова или кнопка не могу вспомнить и -1 bronze monet

from PIL import Image
import  ScanerOOP_Bot

path = 'C:\\Users\\AdminX\\PycharmProjects\\pythonProject\\folder'  # Замените на путь к директории, которую вы хотите обойти
processor = ScanerOOP_Bot.DirectoryProcessor(path)
processor.process_directory()
processor.print_results()

# Путь к основным изображениям
background_image_path = r"D:\7 Photo\DDs-bot\1.jpg"
overlay_image_path = r"D:\7 Photo\DDs-bot\4.png"

# Открытие изображений
background = Image.open(background_image_path)
overlay = Image.open(overlay_image_path)

# Получаем размеры основного изображения
bg_width, bg_height = background.size

# Изменяем размер накладываемого изображения (если нужно)
overlay = overlay.resize((int(bg_width / 4), int(bg_height / 4)))  # Масштабирование до 1/4 размера основного изображения

# Выбираем позицию для накладываемого изображения (например, сверху справа)
position = (bg_width - overlay.width, 0)

# Наложение изображений
background.paste(overlay, position, overlay)

# Сохранение результата
result_image_path = r"D:\7 Photo\DDs-bot\result.jpg"
background.save(result_image_path)

# Вывод результата
background.show()
