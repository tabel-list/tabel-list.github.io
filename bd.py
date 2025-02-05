import requests
import json
import time
from datetime import datetime
import httplib2
import os
import re
import math
from PIL import Image
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

def get_char(id, lang):
    url = "https://gi.yatta.moe/api/v2/" + lang + "/avatar/" + id + "?vh=53F3"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data  # Возвращаем полный ответ API

def get_char_tr(id, lang, el):
    url = "https://gi.yatta.moe/api/v2/" + lang + "/avatar/" + id + "-" + el + "?vh=53F3"
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
],
"characters": 
    {"en": {},
     "ru": {}}
}
char_list = []
char_info = []

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

def compress_image(input_path, output_path, quality=85):
    """Функция для сжатия изображения перед сохранением"""
    with Image.open(input_path) as img:
        img.convert("RGB").save(output_path, "WebP", quality=quality)

h = httplib2.Http()

def compress_image(input_path, output_path, quality=55):
    """Функция для сжатия изображения с сохранением прозрачности"""
    with Image.open(input_path) as img:
        if img.mode in ("RGBA", "LA"):
            img.save(output_path, "WebP", quality=quality)
        else:
            img.convert("RGB").save(output_path, "WebP", quality=quality)

def downRes(resID):
    os.makedirs(f'data/res', exist_ok=True)
    if not os.path.exists(f'data/res/mora.png'):
        url = f'https://gi.yatta.moe/assets/UI/UI_ItemIcon_202.png'
        response, content = h.request(url)
        save_path = f'data/res/mora.png'
        with open(save_path, 'wb') as out:
            out.write(content)

    if not os.path.exists(f'data/res/{resID}.png'):
        url = f'https://gi.yatta.moe/assets/UI/UI_ItemIcon_{resID}.png'
        response, content = h.request(url)
        save_path = f'data/res/{resID}.png'
        with open(save_path, 'wb') as out:
            out.write(content)

def downC(constI, charN):
    url = f'https://gi.yatta.moe/assets/UI/{constI}.png'
    response, content = h.request(url)

    os.makedirs(f'character/{charN}', exist_ok=True)
    save_path = f'character/{charN}/{constI}.png'
    with open(save_path, 'wb') as out:
        out.write(content)

def downS(skillN, charN):
    url = f'https://gi.yatta.moe/assets/UI/{skillN}.png'
    response, content = h.request(url)

    os.makedirs(f'character/{charN}', exist_ok=True)
    save_path = f'character/{charN}/{skillN}.png'
    with open(save_path, 'wb') as out:
        out.write(content)

def down(char_list_api_en, i, url):
    """Скачивание и сжатие изображения"""
    if url == 'https://enka.network/ui/UI_AvatarIcon_':
        response, content = h.request(url + cor_name(char_list_api_en['categories']['outfits']['characterName'][i], name_replacements) + '.png')
    else:
        response, content = h.request(url + cor_name(char_list_api_en['categories']['outfits']['characterName'][i], namecard_replacements) + '_P.png')

    # Создание папки, если её нет
    char_name = char_list_api_en['categories']['outfits']['characterName'][i]
    os.makedirs(f'data/characters/{char_name}', exist_ok=True)

    # Определяем путь для сохранения
    if url == 'https://enka.network/ui/UI_AvatarIcon_':
        save_path = f'data/characters/{char_name}/{char_name}_icon.png'
        compressed_path = f'data/characters/{char_name}/{char_name}_icon.webp'
    else:
        save_path = f'data/characters/{char_name}/{char_name}_namecard.png'
        compressed_path = f'data/characters/{char_name}/{char_name}_namecard.webp'

    # Сохранение оригинала (временный файл)
    with open(save_path, 'wb') as out:
        out.write(content)

    # Сжатие изображения
    compress_image(save_path, compressed_path)

    # Удаление оригинального PNG (оставляем только WebP)
    os.remove(save_path)

def rel(timestamp):
    dt = datetime.utcfromtimestamp(timestamp)  # UTC-время
    formatted_date = dt.strftime('%d.%m.%Y')
    return formatted_date

def format_value(value, format_type):
    """Форматирует значение в соответствии с типом"""
    if format_type == "P":
        formatted = f"{value * 100:.1f}".rstrip("0").rstrip(".")  # Убираем лишние нули и точки
        return f"{formatted}%"
    elif format_type == "F1P":
        formatted = f"{value * 100:.1f}".rstrip("0").rstrip(".")
        return f"{formatted}%"
    elif format_type == "F1":
        return f"{value:.1f}".rstrip("0").rstrip(".")  # Убираем лишние нули и точки
    elif format_type == "I":
        return f"{int(value)}"  # Целое число
    return str(value)

def replace_params(template, values):
    def replacer(match):
        param_name = match.group(1)
        format_type = match.group(2)
        param_index = int(param_name.replace("param", "")) - 1
        if format_type in ["P", "F1P", "F1", "I"]:
            return format_value(values[param_index], format_type)
        return match.group(0)  # Оставляем неизменным, если формат не найден
    
    return re.sub(r"\{(param\d+):(P|F1P|F1|I)\}", replacer, template)

def desc(tall):
    s = 1
    descript = {}
    if 'promote' in tall:
        while(s <= len(tall['promote'])):
            f = 0
            descript[s] = {}
            while f < len(tall['promote'][str(s)]['description']):
                #print(replace_params(tall['promote'][str(s)]['description'][f], tall['promote'][str(s)]['params']).replace("|", " "))
                if tall['promote'][str(s)]['description'][f] != '':
                    descript[s][f] = replace_params(tall['promote'][str(s)]['description'][f], tall['promote'][str(s)]['params']).replace("|", " ") 
                f += 1
            s += 1
    return descript

def ggh(it, cos):
    i = 0
    ffg = {}
    while(i < len(it)):
        ffg[i] = {"id": it[i], "cost": cos[it[i]]}
        downRes(it[i])
        i += 1
    return ffg

def costItems(items):
    if 'promote' in items:
        itemCost = {}
        i = 1
        while(i <= len(items['promote'])):
            if items['promote'][str(i)]['costItems'] == None:
                itemCost[i] = {"res" : None, "mora": None}
            else:
                #print(list((items['promote'][str(i)]['costItems']).keys()))
                itemCost[i] = {"res" : ggh(list((items['promote'][str(i)]['costItems']).keys()), items['promote'][str(i)]['costItems']), "mora": items['promote'][str(i)]['coinCost']}
            i += 1
        return itemCost

def tal(tall, name):
    a = 0
    talents = {}
    print(tall['data']['talent'], name)
    while(a <= len(tall['data']['talent'])):
        try:
            downS(tall['data']['talent'][str(a)]['icon'], name)
            talents[a] = {"name": tall['data']['talent'][str(a)]['name'],
                          "description": tall['data']['talent'][str(a)]['description'],
                          "icon": tall['data']['talent'][str(a)]['icon'],
                          "descriptionStat": desc(tall['data']['talent'][str(a)]),
                          "costItems" : costItems(tall['data']['talent'][str(a)])
                        }
            a += 1
        except KeyError:
            downS(tall['data']['talent'][str(a + 1)]['icon'], name)
            talents[a] = {"name": tall['data']['talent'][str(a + 1)]['name'],
                          "description": tall['data']['talent'][str(a + 1)]['description'],
                          "icon": tall['data']['talent'][str(a + 1)]['icon'],
                          "descriptionStat": desc(tall['data']['talent'][str(a + 1)]),
                          "costItems" : costItems(tall['data']['talent'][str(a + 1)])
                        }
            a += 1
        
    return talents

def sub(subs, lang):
    if subs == 'FIGHT_PROP_ATTACK_PERCENT':
        if lang == 'en':
            return 'ATK %'
        else:
            return 'Сила атаки %'
    elif subs == 'FIGHT_PROP_DEFENSE_PERCENT':
        if lang == 'en':
            return 'DEF %'
        else:
            return 'Защита %'
    elif subs == 'FIGHT_PROP_HP_PERCENT':
        if lang == 'en':
            return 'HP %'
        else:
            return 'HP %'
    elif subs == 'FIGHT_PROP_CRITICAL':
        if lang == 'en':
            return 'CRIT Rate %'
        else:
            return 'Шанс крит. попадания %'
    elif subs == 'FIGHT_PROP_CRITICAL_HURT':
        if lang == 'en':
            return 'CRIT DMG %'
        else:
            return 'Крит. урон %'
    elif subs == 'FIGHT_PROP_HEAL_ADD':
        if lang == 'en':
            return 'Healing Bonus %'
        else:
            return 'Бонус лечения %'
    elif subs == 'FIGHT_PROP_CHARGE_EFFICIENCY':
        if lang == 'en':
            return 'Energy Recharge %'
        else:
            return 'Восст. энергии %'
    elif subs == 'FIGHT_PROP_ELEMENT_MASTERY':
        if lang == 'en':
            return 'Elemental Mastery'
        else:
            return 'Мастерство стихий'
    elif subs == 'FIGHT_PROP_FIRE_ADD_HURT':
        if lang == 'en':
            return 'Pyro DMG Bonus %'
        else:
            return 'Бонус Пиро урона %'
    elif subs == 'FIGHT_PROP_WATER_ADD_HURT':
        if lang == 'en':
            return 'Hydro DMG Bonus %'
        else:
            return 'Бонус Гидро урона %'
    elif subs == 'FIGHT_PROP_GRASS_ADD_HURT':
        if lang == 'en':
            return 'Dendro DMG Bonus %'
        else:
            return 'Бонус Дендро урона %'
    elif subs == 'FIGHT_PROP_ELEC_ADD_HURT':
        if lang == 'en':
            return 'Electro DMG Bonus %'
        else:
            return 'Бонус Электро урона %'
    elif subs == 'FIGHT_PROP_ICE_ADD_HURT':
        if lang == 'en':
            return 'Cryo DMG Bonus %'
        else:
            return 'Бонус Крио урона %'
    elif subs == 'FIGHT_PROP_WIND_ADD_HURT':
        if lang == 'en':
            return 'Anemo DMG Bonus %'
        else:
            return 'Бонус Анемо урона %'
    elif subs == 'FIGHT_PROP_PHYSICAL_ADD_HURT':
        if lang == 'en':
            return 'Physical DMG Bonus %'
        else:
            return 'Бонус физ. урона %'
    elif subs == 'FIGHT_PROP_ROCK_ADD_HURT':
        if lang == 'en':
            return 'Geo DMG Bonus %'
        else:
            return 'Бонус Гео урона %'

def ite(char_pop, el):
    i = 0
    res = {}
    while(i < len(char_pop['data']['upgrade']['promote'][el]['costItems'])):
        downRes(list(char_pop['data']['upgrade']['promote'][el]['costItems'].keys())[i])
        res[i] = {
                       "id": list(char_pop['data']['upgrade']['promote'][el]['costItems'].keys())[i],
                       "cost": char_pop['data']['upgrade']['promote'][el]['costItems'][list(char_pop['data']['upgrade']['promote'][el]['costItems'].keys())[i]]
                   }
        i += 1
    return res

def multt(x):
    result = x * 100
    
    # Если дробная часть равна 0, то оставляем только целую часть
    if result.is_integer():
        return int(result)  # Преобразуем в целое число
    else:
        return result  # Оставляем с плавающей точкой

def elev(char_pop, lang):
    i = 0
    mm = lambda x, y: y * 2.594 if x == 5 else y * 2.569
    cc = lambda x, y, c, a, b: y * a + c if x == 5 else y * b + c
    stat = {}
    stat["sub"] = sub(char_pop['data']['specialProp'], lang)
    stat[0] = {"stats": {
               "HP": round(char_pop['data']['upgrade']['prop'][0]['initValue']),
               "ATK": round(char_pop['data']['upgrade']['prop'][1]['initValue']),
               "DEF": round(char_pop['data']['upgrade']['prop'][2]['initValue']),
               "sub": 0 
               },
               "res": {
                   
               }
               }
    stat[1] = {"stats": {
               "HP": round(mm(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][0]['initValue'])),
               "ATK": round(mm(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][1]['initValue'])),
               "DEF": round(mm(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][2]['initValue'])),
               "sub": 0
               },
               "res": ite(char_pop, 1) 
               }
    stat[2] = {"stats": {
               "HP": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][0]['initValue'], char_pop['data']['upgrade']['promote'][1]['addProps']['FIGHT_PROP_BASE_HP'], 2.594, 2.569)),
               "ATK": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][1]['initValue'], char_pop['data']['upgrade']['promote'][1]['addProps']['FIGHT_PROP_BASE_ATTACK'], 2.594, 2.569)),
               "DEF": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][2]['initValue'], char_pop['data']['upgrade']['promote'][1]['addProps']['FIGHT_PROP_BASE_DEFENSE'], 2.594, 2.569)),
               "sub": 0
               },
               "res": {} 
               }
    stat[3] = {"stats": {
               "HP": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][0]['initValue'], char_pop['data']['upgrade']['promote'][1]['addProps']['FIGHT_PROP_BASE_HP'], 4.307, 4.22)),
               "ATK": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][1]['initValue'], char_pop['data']['upgrade']['promote'][1]['addProps']['FIGHT_PROP_BASE_ATTACK'], 4.307, 4.22)),
               "DEF": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][2]['initValue'], char_pop['data']['upgrade']['promote'][1]['addProps']['FIGHT_PROP_BASE_DEFENSE'], 4.307, 4.22)),
               "sub": 0 #int(char_pop['data']['upgrade']['promote'][2]['addProps'][char_pop['data']['specialProp']] * 100)
               },
               "res": ite(char_pop, 2) 
               }
    stat[4] = {"stats": {
               "HP": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][0]['initValue'], char_pop['data']['upgrade']['promote'][2]['addProps']['FIGHT_PROP_BASE_HP'], 4.307, 4.22)),
               "ATK": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][1]['initValue'], char_pop['data']['upgrade']['promote'][2]['addProps']['FIGHT_PROP_BASE_ATTACK'], 4.307, 4.22)),
               "DEF": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][2]['initValue'], char_pop['data']['upgrade']['promote'][2]['addProps']['FIGHT_PROP_BASE_DEFENSE'], 4.307, 4.22)),
               "sub": float(multt(char_pop['data']['upgrade']['promote'][2]['addProps'][char_pop['data']['specialProp']]))
               },
               "res": {}
               }
    stat[5] = {"stats": {
               "HP": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][0]['initValue'], char_pop['data']['upgrade']['promote'][2]['addProps']['FIGHT_PROP_BASE_HP'], 5.176, 5.046)),
               "ATK": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][1]['initValue'], char_pop['data']['upgrade']['promote'][2]['addProps']['FIGHT_PROP_BASE_ATTACK'], 5.176, 5.046)),
               "DEF": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][2]['initValue'], char_pop['data']['upgrade']['promote'][2]['addProps']['FIGHT_PROP_BASE_DEFENSE'], 5.176, 5.046)),
               "sub": multt(char_pop['data']['upgrade']['promote'][2]['addProps'][char_pop['data']['specialProp']])
               },
               "res": ite(char_pop, 3)
               }
    stat[6] = {"stats": {
               "HP": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][0]['initValue'], char_pop['data']['upgrade']['promote'][3]['addProps']['FIGHT_PROP_BASE_HP'], 5.176, 5.046)),
               "ATK": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][1]['initValue'], char_pop['data']['upgrade']['promote'][3]['addProps']['FIGHT_PROP_BASE_ATTACK'], 5.176, 5.046)),
               "DEF": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][2]['initValue'], char_pop['data']['upgrade']['promote'][3]['addProps']['FIGHT_PROP_BASE_DEFENSE'], 5.176, 5.046)),
               "sub": multt(char_pop['data']['upgrade']['promote'][3]['addProps'][char_pop['data']['specialProp']])
               },
               "res": {}
               }
    stat[7] = {"stats": {
               "HP": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][0]['initValue'], char_pop['data']['upgrade']['promote'][3]['addProps']['FIGHT_PROP_BASE_HP'], 5.966, 5.872)),
               "ATK": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][1]['initValue'], char_pop['data']['upgrade']['promote'][3]['addProps']['FIGHT_PROP_BASE_ATTACK'], 5.966, 5.872)),
               "DEF": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][2]['initValue'], char_pop['data']['upgrade']['promote'][3]['addProps']['FIGHT_PROP_BASE_DEFENSE'], 5.966, 5.872)),
               "sub": multt(char_pop['data']['upgrade']['promote'][3]['addProps'][char_pop['data']['specialProp']])
               },
               "res": ite(char_pop, 4)
               }
    stat[8] = {"stats": {
               "HP": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][0]['initValue'], char_pop['data']['upgrade']['promote'][4]['addProps']['FIGHT_PROP_BASE_HP'], 5.966, 5.872)),
               "ATK": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][1]['initValue'], char_pop['data']['upgrade']['promote'][4]['addProps']['FIGHT_PROP_BASE_ATTACK'], 5.966, 5.872)),
               "DEF": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][2]['initValue'], char_pop['data']['upgrade']['promote'][4]['addProps']['FIGHT_PROP_BASE_DEFENSE'], 5.966, 5.872)),
               "sub": multt(char_pop['data']['upgrade']['promote'][4]['addProps'][char_pop['data']['specialProp']])
               },
               "res": {}
               }
    stat[9] = {"stats": {
               "HP": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][0]['initValue'], char_pop['data']['upgrade']['promote'][4]['addProps']['FIGHT_PROP_BASE_HP'], 7.029, 6.697)),
               "ATK": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][1]['initValue'], char_pop['data']['upgrade']['promote'][4]['addProps']['FIGHT_PROP_BASE_ATTACK'], 7.029, 6.697)),
               "DEF": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][2]['initValue'], char_pop['data']['upgrade']['promote'][4]['addProps']['FIGHT_PROP_BASE_DEFENSE'], 7.029, 6.697)),
               "sub": multt(char_pop['data']['upgrade']['promote'][4]['addProps'][char_pop['data']['specialProp']])
               },
               "res": ite(char_pop, 5)
               }
    stat[10] = {"stats": {
               "HP": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][0]['initValue'], char_pop['data']['upgrade']['promote'][5]['addProps']['FIGHT_PROP_BASE_HP'], 7.029, 6.697)),
               "ATK": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][1]['initValue'], char_pop['data']['upgrade']['promote'][5]['addProps']['FIGHT_PROP_BASE_ATTACK'], 7.029, 6.697)),
               "DEF": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][2]['initValue'], char_pop['data']['upgrade']['promote'][5]['addProps']['FIGHT_PROP_BASE_DEFENSE'], 7.029, 6.697)),
               "sub": multt(char_pop['data']['upgrade']['promote'][5]['addProps'][char_pop['data']['specialProp']])
               },
               "res": {}
               }
    stat[11] = {"stats": {
               "HP": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][0]['initValue'], char_pop['data']['upgrade']['promote'][5]['addProps']['FIGHT_PROP_BASE_HP'], 7.836, 7.523)),
               "ATK": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][1]['initValue'], char_pop['data']['upgrade']['promote'][5]['addProps']['FIGHT_PROP_BASE_ATTACK'], 7.836, 7.523)),
               "DEF": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][2]['initValue'], char_pop['data']['upgrade']['promote'][5]['addProps']['FIGHT_PROP_BASE_DEFENSE'], 7.836, 7.523)),
               "sub": multt(char_pop['data']['upgrade']['promote'][5]['addProps'][char_pop['data']['specialProp']])
               },
               "res": ite(char_pop, 6)
               }
    stat[12] = {"stats": {
               "HP": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][0]['initValue'], char_pop['data']['upgrade']['promote'][6]['addProps']['FIGHT_PROP_BASE_HP'], 7.836, 7.523)),
               "ATK": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][1]['initValue'], char_pop['data']['upgrade']['promote'][6]['addProps']['FIGHT_PROP_BASE_ATTACK'], 7.836, 7.523)),
               "DEF": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][2]['initValue'], char_pop['data']['upgrade']['promote'][6]['addProps']['FIGHT_PROP_BASE_DEFENSE'], 7.836, 7.523)),
               "sub": multt(char_pop['data']['upgrade']['promote'][6]['addProps'][char_pop['data']['specialProp']])
               },
               "res": {}
               }
    stat[13] = {"stats": {
               "HP": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][0]['initValue'], char_pop['data']['upgrade']['promote'][6]['addProps']['FIGHT_PROP_BASE_HP'], 8.739, 8.349)),
               "ATK": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][1]['initValue'], char_pop['data']['upgrade']['promote'][6]['addProps']['FIGHT_PROP_BASE_ATTACK'], 8.739, 8.349)),
               "DEF": round(cc(char_pop['data']['rank'], char_pop['data']['upgrade']['prop'][2]['initValue'], char_pop['data']['upgrade']['promote'][6]['addProps']['FIGHT_PROP_BASE_DEFENSE'], 8.739, 8.349)),
               "sub": multt(char_pop['data']['upgrade']['promote'][6]['addProps'][char_pop['data']['specialProp']])
               },
               "res": {}
               }
    return stat
    #while(i < 8):
    #    
    #print(stat)




def const(char_pop, charN):
    c = 0
    constt = {}
    while(c < len(char_pop['data']['constellation'])):
        downC(char_pop['data']['constellation'][str(c)]['icon'], charN)
        constt[c] = {"name": char_pop['data']['constellation'][str(c)]['name'],
                     "description": char_pop['data']['constellation'][str(c)]['description'],
                     "icon": char_pop['data']['constellation'][str(c)]['icon']}
        c += 1
    return constt

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

    def charr(lang):
        if i != 71:
            if i != 72:
                char_pop = get_char(str(more_data['id']), lang)
                print(more_data['id'])
                data["characters"][lang][char_list_api_en['categories']['outfits']['characterName'][i]] = {
                            "name": char_list_api_en['categories']['outfits']['characterName'][i],
                            "name_ru": char_list_api_ru['categories']['outfits']['characterName'][i],
                            "id": more_data['id'],
                            "rarity": more_data['rarity'],
                            "weapon": more_data['weaponText'],
                            "element": more_data['elementText'],
                            "region": more_data['region'],
                            "more": {
                                "title": char_pop['data']['fetter']['title'],
                                "detail": char_pop['data']['fetter']['detail'],
                                "constellation": char_pop['data']['fetter']['constellation'],
                                "group": char_pop['data']['fetter']['native'],
                                "birthday": str(char_pop['data']['birthday'][1]) + '.' + str(char_pop['data']['birthday'][0]),
                                "release": rel(char_pop['data']['release']),
                                "cv": {
                                    "en": char_pop['data']['fetter']['cv']['EN'],
                                    "chs": char_pop['data']['fetter']['cv']['CHS'],
                                    "jp": char_pop['data']['fetter']['cv']['JP'],
                                    "kr": char_pop['data']['fetter']['cv']['KR']
                                }
                            },
                            "skills": tal(char_pop, char_list_api_en['categories']['outfits']['characterName'][i]),
                            "constellations": const(char_pop, char_list_api_en['categories']['outfits']['characterName'][i]),
                            "elevation": elev(char_pop, lang)
                        }
        #else:
           # ...
            #element = [{"element": "anemo"},
            #    {"element": "geo"},
            #    {"element": "pyro"},
            #    {"element": "hydro"},
            #    {"element": "electro"},
            #    {"element": "dendro"},
            #    {"element": "geo"}]
            #for elem in element:
            #    print(elem['element'])
            #char_pop = get_char_tr(str(more_data['id']), lang)
            #data["characters"][lang][char_list_api_en['categories']['outfits']['characterName'][i]] = {
            #            "name": char_list_api_en['categories']['outfits']['characterName'][i],
            #            "name_ru": char_list_api_ru['categories']['outfits']['characterName'][i],
            #            "id": more_data['id'],
            #            "rarity": more_data['rarity'],
            #            "weapon": more_data['weaponText'],
            #            "element": more_data['elementText'],
            #            "region": more_data['region'],
            #            "more": {
            #                "title": char_pop['data']['fetter']['title'],
            #                "detail": char_pop['data']['fetter']['detail'],
            #                "constellation": char_pop['data']['fetter']['constellation'],
            #                "group": char_pop['data']['fetter']['native'],
            #                "birthday": str(char_pop['data']['birthday'][1]) + '.' + str(char_pop['data']['birthday'][0]),
            #                "release": rel(char_pop['data']['release']),
            #                "cv": {
            #                    "en": char_pop['data']['fetter']['cv']['EN'],
            #                    "chs": char_pop['data']['fetter']['cv']['CHS'],
            #                    "jp": char_pop['data']['fetter']['cv']['JP'],
            #                    "kr": char_pop['data']['fetter']['cv']['KR']
            #                }
            #            },
            #            "skills": tal(char_pop, char_list_api_en['categories']['outfits']['characterName'][i]),
            #            "constellations": const(char_pop, char_list_api_en['categories']['outfits']['characterName'][i]),
            #            "elevation": elev(char_pop, lang)
            #        }

    charr('en')
    charr('ru')
    #data['characters'][i] = ("name: " + config_data_en['categories']['outfits']['characterName'][i])
    i += 1
data['charactersList'] = char_list
#data['characters'] = char_info

save_to_json(data)

end_time = time.time()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения
 
print(f"Время выполнения программы: {execution_time} секунд")