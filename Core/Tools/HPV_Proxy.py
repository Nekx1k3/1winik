from requests import get
from threading import Thread
from colorama import Fore

from Core.Tools.HPV_Getting_File_Paths import HPV_Get_Proxy



def HPV_Request(proxy: dict) -> bool:
    try:
        get('https://ipecho.net/plain', proxies=proxy)
        return True
    except:
        return False



def HPV_Checker(proxy) -> dict:
    PROXY = f"{proxy['Login']}:{proxy['Password']}@{proxy['IP']}:{proxy['Port']}"
    PROXY_HTTPS = {'http': f'http://{PROXY}', 'https': f'https://{PROXY}'}
    PROXY_SOCKS5 = {'http': f'socks5://{PROXY}', 'https': f'socks5://{PROXY}'}

    if HPV_Request(PROXY_HTTPS):
        return PROXY_HTTPS
    elif HPV_Request(PROXY_SOCKS5):
        return PROXY_SOCKS5



def HPV_Proxy_Checker(_print: bool = True) -> list:
    '''Проверка HTTPS, SOCKS5 проксей на валидность'''

    print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Получение списка проксей!') if _print else None
    PROXY_LIST = HPV_Get_Proxy() # Список всех доступных проксей с файла
    VALID_PROXY = [] # Список валидных проксей
    THREADS = [] # Список потоков

    if PROXY_LIST:
        print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Проверка прокси на работоспособность... Подождите немного!') if _print else None

        def _HPV_Checker(proxy):
            HPV = HPV_Checker(proxy)
            if HPV:
                VALID_PROXY.append(HPV)

        for proxy in PROXY_LIST:
            THREAD = Thread(target=_HPV_Checker, args=(proxy,))
            THREAD.start()
            THREADS.append(THREAD)

        for THREAD in THREADS:
            THREAD.join()

        print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + f' — Проверка прокси окончена! Работоспособные: {len(VALID_PROXY)}') if _print else None
    
    else:
        print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Прокси не обнаружены!') if _print else None

    return VALID_PROXY


