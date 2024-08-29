from colorama import Fore
from threading import Thread
from collections import Counter
from os import path
from json import dump

from Core.Tools.HPV_Getting_File_Paths import HPV_Get_Config, HPV_Get_Accounts
from Core.Tools.HPV_Config_Setup import HPV_Config_Setup
from Core.Tools.HPV_Proxy import HPV_Request, HPV_Proxy_Checker
from Core.Tools.HPV_Headers import HPV_Headers
from Core.Tools.HPV_Upgrade import HPV_Upgrade



def HPV_Checking(File: str, Content: str) -> bool:
    '''Создание конфигурационных файлов'''

    try:
        with open(File, 'w') as HPV:
            if File.endswith('.json'):
                dump(Content, HPV, indent=4)
            else:
                HPV.write(Content)
    except:
        pass



def HPV_Check_Configs():
    '''Проверка наличия конфигурационных файлов'''

    HPV_Account_json = path.join(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))), 'Core', 'Config', 'HPV_Account.json')
    HPV_Config_json = path.join(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))), 'Core', 'Config', 'HPV_Config.json')
    HPV_Config_py = path.join(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))), 'Core', 'Config', 'HPV_Config.py')
    HPV_Proxy_txt = path.join(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))), 'Core', 'Proxy', 'HPV_Proxy.txt')

    FILES = {
        HPV_Account_json: {'ACCOUNT_1': 'https://cryptocklicker-frontend-rnd-prod.100hp.app/#tgWebAppData=....', 'ACCOUNT_2': 'https://cryptocklicker-frontend-rnd-prod.100hp.app/#tgWebAppData=....'},
        HPV_Config_json: {},
        HPV_Config_py: '\n\n# Желаемое кол-во кликов за раз. Рандомным путём будет выбрано значение в следующих диапазонах\nCOINS = [11, 46] # 11 - минимальное значение /// 46 - максимальное\n# Ставить максимальное значение выше 100 не рекомендуется! В лучшем случае - монеты не засчитаются на баланс, в худшем - аккаунт забанят!\n\n\n# Максимальный уровень прокачки одной карточки\nMAX_LVL = 20\n# По дефолту установлен самый оптимальный уровень карточки (20). Также 20 является максимальным уровнем прокачки - выше просто невозможно!\n\n\n# Максимальный уровень хранилища восстановленной энергии\nMAX_ENERGY_LIMIT = 10\n# По дефолту установлен самый оптимальный уровень буста (10). Изменять данный параметр не рекомендуется, или на свой страх и риск!\n\n\n# Максимальный уровень скорости восстановления энергии\nMAX_ENERGY_REGEN = 10\n# По дефолту установлен самый оптимальный уровень буста (10). Изменять данный параметр не рекомендуется, или на свой страх и риск!\n\n\n# Автоматическое обновление программы\nAUTO_UPDATE = True # Для включения установите значение True, для отключения — False.\n# По умолчанию автообновление включено, и рекомендуется не изменять этот параметр. Однако, вы можете его отключить по соображениям безопасности!\n\n',
        HPV_Proxy_txt: ''
    }

    for File, Content in FILES.items():
        if not path.exists(File):
            HPV_Checking(File, Content)



def HPV_Config_Check() -> None:
    '''Проверка конфига на валидность'''

    print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Проверка конфига... Подождите немного!')
    HPV_Check_Configs() # Проверка наличия конфигурационных файлов
    HPV_Upgrade() # Автоматическая проверка и установка обновления
    Config = HPV_Get_Config() # Получение конфигурационных данных

    if Config:
        Accounts = HPV_Get_Accounts() # Получение списка аккаунтов
        ALL_PROXY = HPV_Proxy_Checker(_print=False) # Список всех доступных проксей
        USE_PROXY = [Proxy['Proxy'] for Proxy in Config] # Список используемых проксей
        INVALID_PROXY = [] # Список невалидных проксей

        USE_HEADERS = [Headers['Headers'] for Headers in Config] # Список используемых параметров для Headers

        THREADS = [] # Список потоков
        NEW_CONFIG = [] # Данные нового конфига, в случае изменений
        CHANGES = False # Были / небыли изменения


        # Проверка проксей каждой личности
        def HPV_Proxy_Check(Proxy) -> None:
            if not HPV_Request(Proxy):
                INVALID_PROXY.append(Proxy)


        # Получение свободного или малоиспользуемого прокси
        def HPV_New_Proxy():
            if FREE_PROXY: # Если есть свободные прокси из всего списка
                return FREE_PROXY.pop(0) # Берётся первый свободный прокси
            else: # Если свободных проксей нет
                PROXY_USE = Counter(USE_PROXY)
                return min(PROXY_USE, key=PROXY_USE.get) # Берётся прокси, который используется реже всего


        # Генерация новых параметров для Headers
        def HPV_New_Headers():
            while True:
                Headers = HPV_Headers() # Новые сгенерированные параметры для Headers
                if Headers not in USE_HEADERS:
                    return Headers


        # Проверка всех прокси, привязанных к аккаунтам
        print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Проверка проксей каждой личности... Подождите немного!')
        for Account in Config:
            if Account['Proxy']:
                THREAD = Thread(target=HPV_Proxy_Check, args=(Account['Proxy'],))
                THREAD.start()
                THREADS.append(THREAD)


        for THREAD in THREADS:
            THREAD.join()


        # Определение свободных прокси
        FREE_PROXY = [PROXY for PROXY in ALL_PROXY if PROXY not in USE_PROXY]


        # Замена невалидных прокси
        for Account in Config:
            if Account['Proxy'] in INVALID_PROXY: # Если прокси уникальной личности невалиден
                print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + f' — Найден невалидный прокси у `{Account["Name"]}`!')
                Account['Proxy'] = HPV_New_Proxy() # Новый прокси, взамен старого - нерабочего
                print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + f' — Прокси у `{Account["Name"]}` успешно заменён!')
                CHANGES = True


        # Сравнение аккаунтов в `HPV_Account.json` и `HPV_Config.json`
        print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Проверка наличия изменений в конфиге с аккаунтами... Подождите немного!')
        HPV_Account_Json, HPV_Config_Json = {(Name, URL) for Name, URL in Accounts.items()}, {(account['Name'], account['URL']) for account in Config}
        ACCOUNTS_TO_REMOVE = HPV_Config_Json - HPV_Account_Json # Неактуальные аккаунты
        NEW_ACCOUNTS = HPV_Account_Json - HPV_Config_Json # Новые аккаунты

        # Удаление неактуальных аккаунтов
        if ACCOUNTS_TO_REMOVE:
            print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Обнаружены неактуальные аккаунты. Производится их удаление...')
            NEW_CONFIG = [Account for Account in Config if (Account['Name'], Account['URL']) not in ACCOUNTS_TO_REMOVE] # Удаление неактуальных аккаунтов
            CHANGES = True

        # Добавление новых аккаунтов
        if NEW_ACCOUNTS:
            if not ACCOUNTS_TO_REMOVE:
                NEW_CONFIG = [Account for Account in Config] # Добавление текущих актуальных аккаунтов
            print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Обнаружены новые аккаунты. Выполняется их добавление...')
            for Name, URL in NEW_ACCOUNTS:
                Headers = HPV_New_Headers() # Генерация новых уникальных параметров для Headers
                NEW_CONFIG.append({'Name': Name, 'URL': URL, 'Proxy': HPV_New_Proxy(), 'Headers': Headers})
                USE_HEADERS.append(Headers)
                CHANGES = True


        # Сохранение данных при наличии изменений
        if CHANGES:
            print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Сохранение конфигурационных данных!')
            PATH = path.join(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))), 'Core', 'Config', 'HPV_Config.json')
            with open(PATH, 'w', encoding='utf-8') as HPV:
                dump(NEW_CONFIG, HPV, ensure_ascii=False, indent=4)

    else:
        print(Fore.MAGENTA + '[HPV]' + Fore.YELLOW + ' — Конфигурационный файл не настроен или поврежден!')
        HPV_Config_Setup() # Настройка конфига


