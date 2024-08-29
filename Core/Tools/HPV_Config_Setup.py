from colorama import Fore
from os import path
from json import dump

from Core.Tools.HPV_Getting_File_Paths import HPV_Get_Accounts
from Core.Tools.HPV_Headers import HPV_Headers
from Core.Tools.HPV_Proxy import HPV_Proxy_Checker



def HPV_Config_Setup() -> None:
    '''Настройка конфига'''

    print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Настройка конфига... Подождите немного!')
    Accounts = HPV_Get_Accounts() # Словарь аккаунтов

    if Accounts:
        Proxys = HPV_Proxy_Checker() # Список проксей
        User_Agents = [] # Список уникальных параметров для Headers
        Uniq = [] # Список с уникальными параметрами для каждого аккаунта


        # Генератор уникальных параметров для Headers в количестве, соответствующем числу аккаунтов
        print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Генерация уникальных параметров Headers для каждого аккаунта!')
        while len(User_Agents) < len(Accounts):
            Headers = HPV_Headers() # Новые сгенерированные параметры для Headers
            if Headers not in User_Agents: # Проверка на отсутствие таких же параметров для Headers
                User_Agents.append(Headers)


        # Создание уникальных личностей для каждого аккаунта
        print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Создание уникальных личностей для каждого аккаунта!')
        for Number, Key in enumerate(Accounts):
            Uniq.append({'Name': Key, 'URL': Accounts[Key], 'Proxy': Proxys[Number % len(Proxys)] if len(Proxys) > 0 else None, 'Headers': User_Agents[Number]})


        # Сохранение данных
        print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Сохранение конфигурационных данных!')
        PATH = path.join(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))), 'Core', 'Config', 'HPV_Config.json')
        with open(PATH, 'w', encoding='utf-8') as HPV:
            dump(Uniq, HPV, ensure_ascii=False, indent=4)

    else:
        print(Fore.MAGENTA + '[HPV]' + Fore.YELLOW + ' — Аккаунты не найдены!')
        exit()


