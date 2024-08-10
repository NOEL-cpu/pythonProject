import os
import re


def walk_dir(path, counter_dirs=0, counter_subdirs=0, ):
    countMy = 0
    top_words = []
    for nameDir1 in os.listdir(path):
        nameDir2 = os.path.join(path, nameDir1)
        countMy += 1

        if os.path.isdir(nameDir2):
            counter_subdirs += 1
            countMy += 1
            nameDir3 = os.path.join(path, nameDir1)

            for subitem in os.listdir(nameDir3):  # это в folder\\alfabet
                countMy += 1
                print('subitem= ',subitem)
                object_path = os.path.join(nameDir3, subitem)  # ..\\alfabet\\alfabet.txt

                if os.path.isdir(object_path):

                    for object_info in os.listdir(object_path):
                        # print('!3.1.1! in object(lexema venv) info.txt, jpeg, png, audio,')
                        # !отсюда можно осуществить загрузку в обьект#
                        object_path = object_path + '\\info.txt'    # костыль, считает толлько txt.
                                        # распарсить дирректорию и вообще наполнить обьекты + статистика!?!
                        if os.path.exists(object_path):
                            print(subitem)
                            file= open(object_path, 'r+'
                                                    ''
                                                    '', encoding="utf-8")

                            for line in file:    # in info.txt
                                # print(line, end='')
                                # count = line.isdigit()
                                if 'запросов' in line:
                                    find_count = re.search(r'\d+', line) # re-регулярные выражения, для манипуляц в стр
                                    #print('find_count(не обьеденные цифры)= ', find_count)
                                    fcount_int = int(find_count.group(0))
                                    #print('fcount(не обьеденные цифры)= ', find_count)
                                    #find_count работают ущербно, просто видит
                                    if fcount_int > 1 :
                                       top_words.append((subitem, fcount_int))


                                # тут надо:
                                # обращение к банку картинок, сбор прямой и косвенной инфы -> генерация- сохранение выдача ТоN или трата? картинку образ
                                # работа с линиями мне надо найти количество обращений в файле и сделать топ 5 слов
                                #
                                # далее эти слова нужно передать в тренажер, для изучения.



        else:
            counter_dirs += 1
        #    print('!3!', counter_dirs)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('Всего Слов', countMy)
    print('Всего картинок')
    print('Слова переведенные более 2ух раз', top_words)
    return counter_dirs, counter_subdirs


if __name__ == '__main__':
    path = 'C:\\Users\AdminX\PycharmProjects\pythonProject\\folder'  # Замените на путь к директории, которую вы хотите обойти
    counter_dirs, counter_subdirs = walk_dir(path)


# Замените на путь к директории, которую вы хотите обойти 'C:\\Users\AdminX\PycharmProjects\pythonProject/folder'
