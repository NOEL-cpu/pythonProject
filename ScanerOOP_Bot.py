import os
import re

class Word:
    """Класс, представляющий слово, количество его запросов и пути к файлам в директории."""
    def __init__(self, name, count, directory_path):
        self.name = name
        self.count = count
        self.directory_path = directory_path
        self.files = self.find_files_in_directory()

    def find_files_in_directory(self):
        """Находит все файлы в директории и возвращает их пути."""
        file_paths = {}
        for root, _, files in os.walk(self.directory_path):
            for file_name in files:
                # Добавляем пути к файлам в словарь, где ключом будет имя файла
                file_paths[file_name] = os.path.join(root, file_name)
        return file_paths

    def __str__(self):
        files_info = ', '.join([f"{key}: {value}" for key, value in self.files.items()])
        return f"{self.name}: {self.count}\nFiles:\n{files_info}"

class DirectoryProcessor:
    """Класс для обработки директорий и подсчета количества запросов слов."""
    def __init__(self, path):
        self.path = path
        self.top_words = []
        self.single_request_words = []

    def process_directory(self):
        """Проходит по всем директориям и ищет файлы info.txt с количеством запросов."""
        for root, dirs, _ in os.walk(self.path):
            for dir_name in dirs:
                sub_dir_path = os.path.join(root, dir_name)
                self.process_subdirectory(sub_dir_path)

    def process_subdirectory(self, sub_dir_path):
        """Обрабатывает поддиректории и считывает данные из файлов info.txt."""
        for sub_root, sub_dirs, sub_files in os.walk(sub_dir_path):
            for sub_dir_name in sub_dirs:
                info_file_path = os.path.join(sub_root, sub_dir_name, 'info.txt')
                if os.path.exists(info_file_path):
                    with open(info_file_path, 'r', encoding='utf-8') as file:
                        self.process_info_file(file, sub_dir_name, os.path.join(sub_root, sub_dir_name))
            break  # Останавливаем поиск глубже, так как info.txt находится на один уровень ниже

    def process_info_file(self, file, word, directory_path):
        """Обрабатывает файл info.txt и извлекает количество запросов."""
        for line in file:
            if 'запросов' in line:
                find_count = re.search(r'\d+', line)
                if find_count:
                    fcount_int = int(find_count.group(0))
                    word_instance = Word(word, fcount_int, directory_path)
                    if fcount_int > 1:
                        self.top_words.append(word_instance)
                    elif fcount_int == 1:
                        self.single_request_words.append(word_instance)

    def get_top_words(self, top_n=10, single_request_n=5):
        """Возвращает отсортированный список слов по количеству запросов."""
        self.top_words.sort(key=lambda x: x.count, reverse=True)
        top_list = self.top_words[:top_n]
        single_request_list = self.single_request_words[:single_request_n]
        return top_list + single_request_list

    def print_results(self):
        """Выводит результаты обработки директорий."""
        top_words = self.get_top_words()
        print('Топ слова:')
        for word in top_words:
            print(word)
        print('Остальные слова с одним запросом:')
        for word in self.single_request_words:
            if word not in top_words:
                print(word)

if __name__ == '__main__':
    path = 'C:\\Users\\AdminX\\PycharmProjects\\pythonProject\\folder'  # Замените на путь к директории, которую вы хотите обойти
    processor = DirectoryProcessor(path)
    processor.process_directory()
    processor.print_results()
