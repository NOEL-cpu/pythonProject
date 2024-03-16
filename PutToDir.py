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


#2 Управление  анализатором лексемы для записи новых директорий с названиями
def alfabet(message):
    a = message  #не создает для заглавных букв!!!
    print(a)
    for i in range(0x110000): # range(ord('а'), ord('я')):
        print(chr(i), end='')
        if a[0] == chr(i):# !!!!Нада сделать по всей длинне слова
            print(chr(i), 'Буква нашлась \n')
            creatingfolder = 'C:/Users/AdminX/PycharmProjects/pythonProject/folder/'+a[0]
            print("1Это в глабальной среде путь base_path=.", creatingfolder)
            if  os.path.isdir(creatingfolder): #Если заглавная буква существует то создавать папку заглавной не надо
                creatingfolder += '/' + a
                if os.path.isdir(creatingfolder):# если такое слово уже есть то добавим к счетчику простмотров +1
                    print("!Такое слово уже есть")
                    creatingfolder += '/counter.txt'
                    file3=open(creatingfolder,'w') #тут необходимо организавать чтение либо дописывать +1
                    file3.write('1raz')
                    file3.close()
                else :# если такого слова нет( а только буква) то создадим

                    os.mkdir(creatingfolder)
                    print("2Это в глабальной среде путь base_path=.", creatingfolder)
            else :# если ни буквы ни директории не существует
                 os.mkdir(creatingfolder)
                 creatingfolder += '/' + a
                 os.mkdir(creatingfolder)
                 print("3Это в глабальной среде путь base_path=.", creatingfolder)

# КОНЕЦ Управление  анализатором лексемы для записи новых директорий с названиями


#inp_path = Path(os.path.join(base_path, "inputs.txt"))

