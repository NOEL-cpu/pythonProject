import os


def walk_dir(path, counter_dirs=0, counter_subdirs=0):
    countMy = 0
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        countMy += 1
    #    print('!1!', item, countMy)
        if os.path.isdir(item_path):
            counter_subdirs += 1
            countMy += 1
        #    print('!2!', counter_subdirs, '!!22!!', countMy)
            subitem_path = os.path.join(path, item)
            for subitem in os.listdir(subitem_path):  # это в folder\\alfabet
                countMy += 1
          #      print('!2.1!', subitem)
                object_path = os.path.join(subitem_path, subitem)  # ..\\alfabet\\alfabet.txt
            #    print('!2.2.2.1!', subitem_path)
              #  print('!2.2.2!', object_path)
                if os.path.isdir(object_path):
                #    print('!3.1.2!')
                    for object_info in os.listdir(object_path):
                    #    print(object_info)  #
                  #      print('!3.1.1! in object(lexema venv) info.txt, jpeg, png, audio,')
                        # !отсюда можно осуществить загрузку в обьект#
                        object_path = object_path + '\\info.txt'
                        print(object_path)
                        if os.path.exists(object_path):
                            file= open(object_path, 'r+', encoding="utf-8")
                            file.seek(20)
                            cccount= file.read(1)
                            print('!88!', cccount)
                            for line in file:
                                #     print('!31!')
                                print(line, end='')
                                count= line.isdigit()
                                print("!!!5!!",count)
                             #   if line.find('запросов:'):

                                # работа с линиями мне надо найти количество обращений



        else:
            counter_dirs += 1
        #    print('!3!', counter_dirs)
    print('!Всего Слов!', countMy)
    return counter_dirs, counter_subdirs


if __name__ == '__main__':
    path = 'C:\\Users\AdminX\PycharmProjects\pythonProject\\folder'  # Замените на путь к директории, которую вы хотите обойти
    counter_dirs, counter_subdirs = walk_dir(path)
    print(f"Количество директорий: {counter_dirs}")
    print(f"Количество поддиректорий: {counter_subdirs}")

# Замените на путь к директории, которую вы хотите обойти 'C:\\Users\AdminX\PycharmProjects\pythonProject/folder'
