import os

def walk_dir(path, counter_dirs=0, counter_subdirs=0):
    countMy = 0
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        countMy += 1
        print('!1!', item, countMy)
        if os.path.isdir(item_path):
            counter_subdirs += 1
            countMy += 1
            print('!2!',counter_subdirs,'!!22!!', countMy)
            subitem_path = os.path.join(path, item)
            for subitem in os.listdir(subitem_path): #
                countMy +=1
                print('!2.1!', subitem)
        else:
            counter_dirs += 1
            print('!3!',counter_dirs)
    print('!4!')
    return counter_dirs, counter_subdirs

if __name__ == '__main__':
    path = 'C:\\Users\AdminX\PycharmProjects\pythonProject/folder'  # Замените на путь к директории, которую вы хотите обойти
    counter_dirs, counter_subdirs = walk_dir(path)
    print(f"Количество директорий: {counter_dirs}")
    print(f"Количество поддиректорий: {counter_subdirs}")


  # Замените на путь к директории, которую вы хотите обойти 'C:\\Users\AdminX\PycharmProjects\pythonProject/folder'



