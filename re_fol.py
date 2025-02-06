import os
import json

# Загрузим исходный JSON-файл
with open('genshin_config.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Перебираем каждый персонаж в разделе 'characters'
for name in data['characters']['en']:  # Предполагаем, что все персонажи есть в обоих языках
    # Создаем структуру данных, как указано
    new_data = {
        name: {
            "en": data['characters']['en'][name],  # Данные на английском
            "ru": data['characters']['ru'][name]   # Данные на русском
        }
    }

    # Создаем папку с именем персонажа
    folder_name = name
    os.makedirs(f"character/{folder_name}", exist_ok=True)

    # Сохраняем данные персонажа в один JSON файл
    file_path = os.path.join(f"character/{folder_name}", f"{name}.json")
    with open(file_path, 'w', encoding='utf-8') as char_file:
        json.dump(new_data, char_file, ensure_ascii=False, indent=4)

print("Данные сохранены в отдельных файлах с нужной структурой.")
