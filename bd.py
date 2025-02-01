import requests
import json
import time
import httplib2
import os
start_time = time.time()

def get_char_list(lang):
    url = "https://genshin-db-api.vercel.app/api/v5/config?resultLanguage=" + lang
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data  # Возвращаем полный ответ API

def get_char_list_more(name, lang):
    url = "https://genshin-db-api.vercel.app/api/v5/characters?query=" + name + "&queryLanguages=en&resultLanguage=" + lang
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data  # Возвращаем полный ответ API
    
def save_to_json(data, filename="genshin_config.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Данные сохранены в {filename}")

char_list_api_ru = get_char_list('ru')
char_list_api_en = get_char_list('en')
#char_list_api_more = get_char_list_more()

data = {"charactersList": [
    #char_list
]}
char_list = []

def cor_name(name, cor_name):
    if name in cor_name:
        return cor_name[name]  # Имя найдено, возвращаем замену
    return name  # Имя не найдено, возвращаем оригинал

name_replacements = {
    "Amber": "Ambor",
    "Raiden Shogun": "Shougun",
    "Aether": "PlayerBoy",
    "Lumine": "PlayerGirl",
    "Yae Miko": "Yae",
    "Alhaitham": "Alhatham",
    "Arataki Itto": "Itto",
    "Baizhu": "Baizhuer",
    "Hu Tao": "Hutao",
    "Jean": "Qin",
    "Kaedehara Kazuha": "Kazuha",
    "Kamisato Ayaka": "Ayaka",
    "Kamisato Ayato": "Ayato",
    "Kirara": "Momoka",
    "Kujou Sara": "Sara",
    "Kuki Shinobu": "Shinobu",
    "Lan Yan": "Lanyan",
    "Lynette": "Linette",
    "Lyney": "Liney",
    "Noelle": "Noel",
    "Ororon": "Olorun",
    "Sangonomiya Kokomi": "Kokomi",
    "Shikanoin Heizou": "Heizo",
    "Thoma": "Tohma",
    "Xianyun": "Liuyun",
    "Yanfei": "Feiyan",
    "Yun Jin": "Yunjin"
}

namecard_replacements = {
    "Amber": "Ambor",
    "Raiden Shogun": "Shougun",
    "Aether": "Ysxf5",
    "Lumine": "Ysxf5",
    "Yae Miko": "Yae1",
    "Alhaitham": "Alhatham",
    "Arataki Itto": "Itto",
    "Baizhu": "Baizhuer",
    "Hu Tao": "Hutao",
    "Jean": "Qin",
    "Kaedehara Kazuha": "Kazuha",
    "Kamisato Ayaka": "Ayaka",
    "Kamisato Ayato": "Ayato",
    "Kirara": "Kirara",
    "Kujou Sara": "Sara",
    "Kuki Shinobu": "Shinobu",
    "Lan Yan": "Lanyan",
    "Lynette": "Linette",
    "Lyney": "Liney",
    "Noelle": "Noel",
    "Ororon": "Olorun",
    "Sangonomiya Kokomi": "Kokomi",
    "Shikanoin Heizou": "Heizo",
    "Thoma": "Tohma",
    "Xianyun": "Liuyun",
    "Yanfei": "Feiyan",
    "Yun Jin": "Yunjin"
}

h = httplib2.Http('.cache')
def down(char_list_api_en, i, url):
    if url == 'https://enka.network/ui/UI_AvatarIcon_':
        response, content = h.request(url + cor_name(char_list_api_en['categories']['outfits']['characterName'][i], name_replacements) + '.png')
    else:
        response, content = h.request(url + cor_name(char_list_api_en['categories']['outfits']['characterName'][i], namecard_replacements) + '_P.png')
    os.makedirs('data/characters/{}'.format(char_list_api_en['categories']['outfits']['characterName'][i]), exist_ok=True)
    if url == 'https://enka.network/ui/UI_AvatarIcon_':
        out = open('data/characters/' + char_list_api_en['categories']['outfits']['characterName'][i] + '/' + char_list_api_en['categories']['outfits']['characterName'][i] + '_icon.png', 'wb')
    else:
        out = open('data/characters/' + char_list_api_en['categories']['outfits']['characterName'][i] + '/' + char_list_api_en['categories']['outfits']['characterName'][i] + '_namecard.png', 'wb')
    out.write(content)
    out.close()

i = 0
while(i < len(char_list_api_en['categories']['outfits']['characterName'])):
    down(char_list_api_en, i, 'https://enka.network/ui/UI_AvatarIcon_')
    down(char_list_api_en, i, 'https://enka.network/ui/UI_NameCardPic_')
    more_data = get_char_list_more(char_list_api_en['categories']['outfits']['characterName'][i], 'en')
    char_res = {"name": char_list_api_en['categories']['outfits']['characterName'][i],
                "name_ru": char_list_api_ru['categories']['outfits']['characterName'][i],
                "id": more_data['id'],
                "rarity": more_data['rarity'],
                "weapon": more_data['weaponText'],
                "element": more_data['elementText'],
                "region": more_data['region']}
    char_list.append(char_res)
    #data['characters'][i] = ("name: " + config_data_en['categories']['outfits']['characterName'][i])
    i += 1
data['charactersList'] = char_list

save_to_json(data)

end_time = time.time()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения
 
print(f"Время выполнения программы: {execution_time} секунд")