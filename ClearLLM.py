import os

def remove_transcription_lines(file_path):
    """Удаляет строки, начинающиеся с 'Transcription', из указанного файла."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                if not line.startswith('Word'):
                    file.write(line)
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
    except Exception as e:
        print(f"Ошибка при обработке файла {file_path}: {e}")

def process_directory(directory):
    """Рекурсивно проходит по директории и удаляет строки 'Transcription' из файлов info.txt."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == 'info.txt':
                file_path = os.path.join(root, file)
                remove_transcription_lines(file_path)

if __name__ == "__main__":
    directory_path = "C:\\Users\\AdminX\\PycharmProjects\\pythonProject\\folder"
    process_directory(directory_path)
    print("Обработка завершена.")
