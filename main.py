# let's count the number of lines in a given file

import sys
import os
from pathlib import Path

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
a = 'утес'

#2 Управление  анализатором лексемы для записи новых директорий с названиями

for i in range(ord('а'), ord('я')):
 #   print(chr(i), end='')
    if a[0] == chr(i):
        print(chr(i), 'Буква нашлась \n')
        creatingfolder = 'C:/Users/AdminX/PycharmProjects/pythonProject/folder/'+a[0]
        if  os.path.isdir(creatingfolder): #Если заглавная буква существует то создавать папку заглавной не надо
            creatingfolder += '/' + a
            if os.path.isdir(creatingfolder):# если такое слово уже есть то добавим к счетчику простмотров +1
                print("!Такое слово уже есть")
                creatingfolder += '/counter.txt'
                file3=open(creatingfolder,'w')
                file3.write('1raz')
                file3.close()
            else :# если такого слова нет( а только буква) то создадим
                creatingfolder += '/' + a
                os.mkdir(creatingfolder)
        else :# если ни буквы ни директории не существует
             os.mkdir(creatingfolder)
             creatingfolder += '/' + a
             os.mkdir(creatingfolder)
# КОНЕЦ Управление  анализатором лексемы для записи новых директорий с названиями

print("Это в глабальной среде путь base_path=.", creatingfolder)
#inp_path = Path(os.path.join(base_path, "inputs.txt"))

