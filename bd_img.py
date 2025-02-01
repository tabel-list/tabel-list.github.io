def cor_name(name, cor_name):
    if name in cor_name:
        return cor_name[name]  # Имя найдено, возвращаем замену
    return name  # Имя не найдено, возвращаем оригинал

name_replacements = {
    "Amber": "Эмбер",
    "Xianyun": "Сянь Юнь",
    "Charlotte": "Шарлотта",
    "Emilie": "Эмилия",
    "Collei": "Коллеи"
}

print(cor_name('Amber', name_replacements))