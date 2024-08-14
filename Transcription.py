# - если ты ее еще раз запустишь то получишь еще одну строчку transcription: абилитьти.
# - не запускай просто так нужно сделать так что бы она только если не видит этой строки
import os

# Правила транскрипции
transcription_rules = {
    'a': 'æ', 'e': 'ɛ', 'i': 'ɪ', 'o': 'ɒ', 'u': 'ʌ',
    'ai': 'aɪ', 'au': 'aʊ', 'ch': 'ʧ', 'sh': 'ʃ', 'th': 'θ',
    'ee': 'iː', 'oo': 'uː', 'ng': 'ŋ', 'ph': 'f', 'qu': 'kw',
    'ie': 'aɪ', 'ou': 'aʊ', 'ea': 'iː'
}

def transcribe(word, rules):
    def replace_substring(word, rules):
        for key in sorted(rules.keys(), key=lambda x: -len(x)):  # сортируем ключи по убыванию длины
            word = word.replace(key, rules[key])
        return word
    return replace_substring(word, rules)

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            word = dir_name  # Название папки — это слово
           # transcribed_word = transcribe(word, transcription_rules)

            sub_dir = os.path.join(root, dir_name)
            for sub_root, sub_dirs, sub_files in os.walk(sub_dir):
                for sub_dir_name in sub_dirs:
                    info_file_path = os.path.join(sub_root, sub_dir_name, 'info.txt')
                    if os.path.exists(info_file_path):
                        with open(info_file_path, 'a', encoding='utf-8') as f:
                            transcribed_word = transcribe(sub_dir_name, transcription_rules)
                            f.write(f"Transcription: {transcribed_word}\n")
                break  # Останавливаем поиск глубже, так как info.txt находится на один уровень ниже

if __name__ == "__main__":
    directory_path = "C:\\Users\\AdminX\\PycharmProjects\\pythonProject\\folder"
    process_directory(directory_path)
