import sys
import os
import datetime
import countOpenWordInfo
import re

from pathlib import Path
# def create_info_file(data):
#     """
#     Создает файл с именем info.txt и заполняет его данными.
#     Каждая строка файла будет содержать пары ключ:значение из словаря.
#
#     Args:
#     data (dict): Словарь с данными, которые будут записаны в файл.
#     """
#     info = {
#     'Имя': 'Алексей',
#     'Возраст': 28,
#     'Город': 'Москва',
#     'Профессия': 'Программист'}
#     with open('info.txt', 'w', encoding='utf-8') as file:
#         for key, value in  info.items():
#             file.write(f"{key}:{value}\n")

def read_increment_value(filename):
    # Проверяем существует ли файл
    filename += '/info.txt'
    if not os.path.exists(filename):
        # если нет файла
        info = {
        'количество запросов': '1',
        'синоним': "-",
        'антоним': '-',
        'path_sound': '-'}

        with open(filename, 'w', encoding='utf-8') as file:
            for key, value in info.items():
                 file.write(f"{key}:{value}\n")
        # with open(filename, 'w') as file:
        #     print(file, "успешно создан")
        #     file.write(str(1))
        #     print(file, "успешно записаннно число 1")
        #     return 0

    # Читаем значение из файла
    with open(filename, 'r') as file:
        increment_value = int(file.read().strip())
        print("найденное значение, создать поля count id i td", increment_value)
    return increment_value


def write_increment_value(filename, value):
    # Записываем значение в файл
    with open(filename, 'w') as file:
        file.write(str(value))


def zapros_na_slowo(exemple_path):
    # когда слово уже существует однако нужно обновить количество просмотров
    with open(exemple_path,  'r', encoding='utf-8') as file:
        lines=file.readline()
        for line in lines:
            if 'количество' in lines:
                print(lines)
                counter = re.search(r'\d+',lines)
                print(type(counter))
                counter_int= int(counter.group(0))
                counter_int += 1
                info = {
                  'количество запросов': counter_int,
                  'синоним': "-",
                  'антоним': '-',
                  'path_sound': '-'}
                with open(exemple_path, 'w', encoding='utf-8') as file:
                    for key, value in info.items():
                        file.write(f"{key}:{value}\n")
                return 0

    print("1 повысил количество обращений ")




def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
        print("Показать путь который находится в файле спек", base_path)
    except Exception:
        base_path = os.path.abspath(relative_path)
        print("если тут значит создался по exception.  ", base_path)

    return os.path.join(base_path, relative_path)


# ввод слова.
# через tg бота?
# a = str(input())

def alfabet(message):
    a = message  # не создает для заглавных букв!!!
    print(a)


    creatingfolder = 'C:/Users/AdminX/PycharmProjects/pythonProject/folder/' + a[0] + '/' + a
    print("1Это в глабальной среде путь base_path=.", creatingfolder)
     # Если заглавная буква существует то создавать папку заглавной не надо
    if os.path.isdir(creatingfolder):  # если такое слово уже есть то добавим к счетчику простмотров +1
        print("!Такое слово уже есть")
        creatingfolder += '/info.txt'
        zapros_na_slowo(creatingfolder)

    if not os.path.isdir(creatingfolder):  # если ни буквы ни директории не существует
        os.mkdir(creatingfolder) # это делает директорию
        read_increment_value(creatingfolder)
        print("3Это в глабальной среде путь base_path=.", creatingfolder)






# 2 Управление  анализатором лексемы для записи новых директорий с названиями
def alfabet0(message):
    a = message  # не создает для заглавных букв!!!
    print(a)


    for i in range(
            0x110000):  # range(ord('а'), ord('я')): #11000000 - длиной от 2 до 4 байт, в которых первый байт всегда имеет маску 11xxxxxx, а остальные — 10xxxxxx???
        print(chr(i), end='')
        if a[0] == chr(i):  # !!!!Нада сделать по всей длинне слова
            print(chr(i), 'Буква нашлась \n')
            creatingfolder = 'C:/Users/AdminX/PycharmProjects/pythonProject/folder/' + a[0]
            print("1Это в глабальной среде путь base_path=.", creatingfolder)
            if os.path.isdir(creatingfolder):  # Если заглавная буква существует то создавать папку заглавной не надо
                creatingfolder += '/' + a
                if os.path.isdir(creatingfolder):  # если такое слово уже есть то добавим к счетчику простмотров +1
                    print("!Такое слово уже есть")

                    creatingfolder += 'info.txt'
                    zapros_na_slowo(creatingfolder)
                 #  file3 = open(creatingfolder, 'w')  # тут необходимо организавать чтение либо дописывать +1
                 #  print("fadfa",file3)

                 #  info = int(file3.read().strip())
                 #  print("fadfa",info)
                 #  info += 1
                 #  file3.write(info)
                 #  file3.close()
                else:  # если такого слова нет( а только буква) то создадим

                    os.mkdir(creatingfolder)

                    print("2Это в глабальной среде путь base_path=.", creatingfolder)
            else:  # если ни буквы ни директории не существует
                os.mkdir(creatingfolder)
                creatingfolder += '/' + a
                os.mkdir(creatingfolder)
                print("3Это в глабальной среде путь base_path=.", creatingfolder)

# КОНЕЦ Управление  анализатором лексемы для записи новых директорий с названиями


# inp_path = Path(os.path.join(base_path, "inputs.txt"))
