import os
import datetime


def read_increment_value(filename):
    # Проверяем существует ли файл
    if not os.path.exists(filename):
        # Если файл не существует, возвращаем начальное значение 0
        with open(filename, 'w') as file:
            print(file, "успешно создан")
            file.write(str(0))
            print(file, "успешно записаннно число 0")
            return 0

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
    value = read_increment_value(exemple_path)
    print("1  ", value)
    write_increment_value(exemple_path, value + 1)



current_time = datetime.datetime.now()
print("Текущее время:", current_time)
exemple_path = "C:/Users/AdminX/PycharmProjects/pythonProject/folder/e/exemple/info.txt" #для отдельного запуска

#zapros_na_slowo(exemple_path)

