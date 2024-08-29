from os import path
from json import load
from colorama import Fore



def HPV_Get_Accounts() -> dict:
    '''Получение списка аккаунтов'''

    print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Получение списка аккаунтов!')
    PATH = path.join(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))), 'Core', 'Config', 'HPV_Account.json')

    try:
        with open(PATH, 'r') as HPV:
            return load(HPV)
    except:
        print(Fore.MAGENTA + '[HPV]' + Fore.RED + ' — Ошибка чтения `HPV_Account.json`, ссылки указаны некорректно!')
        exit()



def HPV_Get_Proxy() -> list:
    '''Получение списка proxy'''

    PATH = path.join(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))), 'Core', 'Proxy', 'HPV_Proxy.txt')
    PROXY = []

    with open(PATH, 'r') as HPV:
        for Proxy in HPV.read().split('\n'):
            if Proxy:
                try:
                    Proxy = Proxy.split(':')
                    PROXY.append({'IP': Proxy[0], 'Port': Proxy[1], 'Login': Proxy[2], 'Password': Proxy[3]})
                except:
                    pass

        return PROXY



def HPV_Get_Config(_print: bool = True) -> list:
    '''Получение конфигурационных данных'''

    if _print:
        print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Получение конфигурационных данных!')

    PATH = path.join(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))), 'Core', 'Config', 'HPV_Config.json')

    try:
        with open(PATH, 'r') as HPV:
            return load(HPV)
    except:
        return []



def HPV_Get_Empty_Request() -> dict:
    '''Получение данных c пустыми запросами'''

    PATH = path.join(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))), 'Core', 'Config', 'HPV_Empty_Request.json')

    try:
        with open(PATH, 'r') as HPV:
            return load(HPV)
    except:
        return {}



def HPV_Get_Accept_Language() -> dict:
    '''Получение данных с языковыми заголовками'''

    PATH = path.join(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))), 'Core', 'Config', 'HPV_Accept_Language.json')

    try:
        with open(PATH, 'r') as HPV:
            return load(HPV)
    except:
        return {}


