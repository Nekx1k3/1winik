from requests import Session
from urllib.parse import unquote, parse_qs
from colorama import Fore
from datetime import datetime, timedelta
from threading import Thread, Lock
from typing import Literal
from random import randint, shuffle
from os import system as sys
from platform import system as s_name
from time import sleep
from re import sub
from json import loads

from Core.Tools.HPV_Banner import HPV_Banner
from Core.Tools.HPV_Config_Check import HPV_Config_Check
from Core.Tools.HPV_Upgrade import HPV_Upgrade_Alert
from Core.Tools.HPV_Getting_File_Paths import HPV_Get_Config, HPV_Get_Empty_Request, HPV_Get_Accept_Language

from Core.Config.HPV_Config import *







class HPV_1win:
    '''
    AutoBot Ferma /// HPV
    ---------------------
    [1] - `Выполнение заданий связанные с подписками`
    
    [2] - `Сбор монет за рефералов`
    
    [3] - `Получение ежедневной награды`
    
    [4] - `Улучшение бустов`
    
    [5] - `Апгрейд всех карточек до максимально возможно уровня`
    
    [6] - `30 минут беспрерывного тапания`
    
    [7] - `Ожидание от 3 до 5 часов`
    
    [8] - `Повторение действий через 3-5 часа`
    '''



    def __init__(self, Name: str, URL: str, Proxy: dict, Headers: dict) -> None:
        self.HPV_PRO = Session()       # Создание `requests` сессии
        self.Name = Name               # Ник аккаунта
        self.Proxy = Proxy             # Прокси (при наличии)

        INFO = self.URL_Clean(URL)
        self.TG_ID = INFO['ID']        # ID аккаунта
        self.URL = INFO['URL']         # Уникальная ссылка для авторизации в mini app
        self.Domain = INFO['Domain']   # Домен игры

        # Уникальные параметров для Headers
        self.USER_AGENT = Headers['USER_AGENT']
        self.SEC_CH_UA = Headers['SEC_CH_UA']
        self.SEC_CH_UA_MOBILE = Headers['SEC_CH_UA_MOBILE']
        self.SEC_CH_UA_PLATFORM = Headers['SEC_CH_UA_PLATFORM']
        self.X_REQUESTED_WITH = Headers['X_REQUESTED_WITH']
        self.ACCEPT_LANGUAGE = self.Get_Accept_Language()

        self.Token = self.Authentication()   # Токен аккаунта



    def URL_Clean(self, URL: str) -> dict:
        '''Очистка уникальной ссылки от лишних элементов'''

        try:
            ID = str(loads(unquote(unquote(unquote(URL.split('tgWebAppData=')[1].split('&tgWebAppVersion')[0]))).split('&')[1].split('user=')[1])['id'])
        except:
            ID = ''

        try:
            _URL = {KEY: VALUE[0] for KEY, VALUE in parse_qs(unquote(unquote(unquote(URL.split('#tgWebAppData=')[1].split('&tgWebAppVersion')[0])))).items()}
        except:
            _URL = ''

        return {'ID': ID, 'URL': _URL, 'Domain': 'https://crypto-clicker-backend-go-prod.100hp.app/'}



    def Current_Time(self) -> str:
        '''Текущее время'''

        return Fore.BLUE + f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'



    def Logging(self, Type: Literal['Success', 'Warning', 'Error'], Smile: str, Text: str) -> None:
        '''Логирование'''

        with Console_Lock:
            COLOR = Fore.GREEN if Type == 'Success' else Fore.YELLOW if Type == 'Warning' else Fore.RED # Цвет текста
            DIVIDER = Fore.BLACK + ' | '   # Разделитель

            Time = self.Current_Time()        # Текущее время
            Name = Fore.MAGENTA + self.Name   # Ник аккаунта
            Smile = COLOR + str(Smile)        # Смайлик
            Text = COLOR + Text               # Текст лога

            print(Time + DIVIDER + Smile + DIVIDER + Text + DIVIDER + Name)



    def Get_Accept_Language(self) -> str:
        '''Получение языкового параметра, подходящего под IP'''

        Accept_Language = HPV_Get_Accept_Language() # Получение данных с языковыми заголовками

        # Определение кода страны по IP
        try:
            COUNTRY = self.HPV_PRO.get('https://ipwho.is/', proxies=self.Proxy).json()['country_code'].upper()
        except:
            COUNTRY = ''

        return Accept_Language.get(COUNTRY, 'en-US,en;q=0.9')



    def Authentication(self) -> str:
        '''Аутентификация аккаунта'''

        URL = self.Domain + 'game/start'
        HEADERS_1 = {'User-Agent': self.USER_AGENT, 'Accept': 'application/json, text/plain, */*', 'sec-ch-ua': self.SEC_CH_UA, 'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarySnDW4AzsItae5rbR', 'sec-ch-ua-mobile': self.SEC_CH_UA_MOBILE, 'x-user-id': self.TG_ID, 'sec-ch-ua-platform': self.SEC_CH_UA_PLATFORM, 'origin': 'https://cryptocklicker-frontend-rnd-prod.100hp.app', 'x-requested-with': self.X_REQUESTED_WITH, 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://cryptocklicker-frontend-rnd-prod.100hp.app/', 'accept-language': self.ACCEPT_LANGUAGE}
        HEADERS_2 = {'User-Agent': self.USER_AGENT, 'access-control-request-method': 'POST', 'access-control-request-headers': 'x-user-id', 'origin': 'https://cryptocklicker-frontend-rnd-prod.100hp.app', 'sec-fetch-mode': 'cors', 'x-requested-with': self.X_REQUESTED_WITH, 'sec-fetch-site': 'same-site', 'sec-fetch-dest': 'empty', 'referer': 'https://cryptocklicker-frontend-rnd-prod.100hp.app/', 'accept-language': self.ACCEPT_LANGUAGE}

        self.Empty_Request('Authentication_1') # Пустой запрос
        self.Empty_Request('Authentication_2') # Пустой запрос
        self.Empty_Request('Authentication_3') # Пустой запрос
        self.Empty_Request('Authentication_4') # Пустой запрос
        self.Empty_Request('Authentication_5') # Пустой запрос
        self.Empty_Request('Authentication_6') # Пустой запрос
        self.Empty_Request('Authentication_7') # Пустой запрос
        self.Empty_Request('Authentication_8') # Пустой запрос
        self.Empty_Request('Authentication_9') # Пустой запрос
        self.Empty_Request('Authentication_10') # Пустой запрос
        self.Empty_Request('Authentication_11') # Пустой запрос
        self.Empty_Request('Authentication_12') # Пустой запрос

        try:
            self.HPV_PRO.options(URL, headers=HEADERS_2, params=self.URL, proxies=self.Proxy) # Пустой запрос
            Token = self.HPV_PRO.post(URL, headers=HEADERS_1, params=self.URL, proxies=self.Proxy).json()['token']
            self.Logging('Success', '🟢', 'Инициализация успешна!')
            return Token
        except:
            self.Logging('Error', '🔴', 'Ошибка инициализации!')
            return ''



    def ReAuthentication(self) -> None:
        '''Повторная аутентификация аккаунта'''

        self.Token = self.Authentication()



    def Empty_Request(self, Empty: str) -> None:
        '''Отправка пустых запросов с подгрузкой дополнений сайта, чтобы казаться человеком'''

        Request: dict = HPV_Get_Empty_Request()[Empty]

        for header_key in list(Request['Headers'].keys()):
            header_key_lower = header_key.lower()

            if header_key_lower == 'user-agent':
                Request['Headers'][header_key] = self.USER_AGENT
            elif header_key_lower == 'sec-ch-ua':
                Request['Headers'][header_key] = self.SEC_CH_UA
            elif header_key_lower == 'sec-ch-ua-mobile':
                Request['Headers'][header_key] = self.SEC_CH_UA_MOBILE
            elif header_key_lower == 'authorization':
                Request['Headers'][header_key] = f'Bearer {self.Token}'
            elif header_key_lower == 'x-user-id':
                Request['Headers'][header_key] = self.TG_ID
            elif header_key_lower == 'sec-ch-ua-platform':
                Request['Headers'][header_key] = self.SEC_CH_UA_PLATFORM
            elif header_key_lower == 'x-requested-with':
                Request['Headers'][header_key] = self.X_REQUESTED_WITH
            elif header_key_lower == 'accept-language':
                Request['Headers'][header_key] = self.ACCEPT_LANGUAGE

        try:
            self.HPV_PRO.request(method=Request['Method'], url=Request['Url'], params=Request.get('Params'), data=Request.get('Data'), json=Request.get('Json'), headers=Request.get('Headers'), proxies=self.Proxy)
        except:
            pass



    def Get_Info(self) -> dict:
        '''Получение информации о балансе, прибыли в час и силе клика'''

        URL = self.Domain + 'user/balance'
        HEADERS = {'User-Agent': self.USER_AGENT, 'sec-ch-ua': self.SEC_CH_UA, 'sec-ch-ua-mobile': self.SEC_CH_UA_MOBILE, 'authorization': f'Bearer {self.Token}', 'x-user-id': self.TG_ID, 'sec-ch-ua-platform': self.SEC_CH_UA_PLATFORM, 'origin': 'https://cryptocklicker-frontend-rnd-prod.100hp.app', 'x-requested-with': self.X_REQUESTED_WITH, 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://cryptocklicker-frontend-rnd-prod.100hp.app/', 'accept-language': self.ACCEPT_LANGUAGE}

        self.Empty_Request('Authentication_13') # Пустой запрос
        self.Empty_Request('Authentication_14') # Пустой запрос
        self.Empty_Request('Authentication_15') # Пустой запрос
        self.Empty_Request('Balance_1') # Пустой запрос
        self.Empty_Request('Balance_2') # Пустой запрос
        self.Empty_Request('Balance_3') # Пустой запрос
        self.Empty_Request('Balance_4') # Пустой запрос
        self.Empty_Request('Balance_5') # Пустой запрос
        self.Empty_Request('Balance_6') # Пустой запрос
        self.Empty_Request('Balance_7') # Пустой запрос
        self.Empty_Request('Balance_1') # Пустой запрос
        self.Empty_Request('Balance_8') # Пустой запрос

        try:
            HPV = self.HPV_PRO.get(URL, headers=HEADERS, proxies=self.Proxy).json()

            Balance = HPV['coinsBalance'] # Баланс
            Hour_Profit = HPV['miningPerHour'] # Прибыль в час
            Click_Power = HPV['coinsPerClick'] # Сила клика

            return {'Balance': f'{Balance:,}', 'Hour_Profit': f'{Hour_Profit:,}', 'Click_Power': f'{Click_Power:,}'}
        except:
            return {'Balance': '0', 'Hour_Profit': '0', 'Click_Power': '0'}



    def Get_Config(self, Type: str) -> list:
        '''Получение конфига аккаунта на серверах 1win'''

        URL = self.Domain + 'game/config'
        HEADERS = {'User-Agent': self.USER_AGENT, 'sec-ch-ua': self.SEC_CH_UA, 'sec-ch-ua-mobile': self.SEC_CH_UA_MOBILE, 'authorization': f'Bearer {self.Token}', 'x-user-id': self.TG_ID, 'sec-ch-ua-platform': self.SEC_CH_UA_PLATFORM, 'origin': 'https://cryptocklicker-frontend-rnd-prod.100hp.app', 'x-requested-with': self.X_REQUESTED_WITH, 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://cryptocklicker-frontend-rnd-prod.100hp.app/', 'accept-language': self.ACCEPT_LANGUAGE}

        self.Empty_Request('Balance_3') # Пустой запрос

        try:
            HPV = loads(self.HPV_PRO.get(URL, headers=HEADERS, proxies=self.Proxy).json())
            return HPV[Type]
        except:
            return []



    def Run_Tasks(self, Task: dict) -> None:
        '''Выполнение задания'''

        URL = self.Domain + 'tasks/subscription'
        HEADERS_1 = {'User-Agent': self.USER_AGENT, 'sec-ch-ua': self.SEC_CH_UA, 'sec-ch-ua-mobile': self.SEC_CH_UA_MOBILE, 'authorization': f'Bearer {self.Token}', 'x-user-id': self.TG_ID, 'sec-ch-ua-platform': self.SEC_CH_UA_PLATFORM, 'origin': 'https://cryptocklicker-frontend-rnd-prod.100hp.app', 'x-requested-with': self.X_REQUESTED_WITH, 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://cryptocklicker-frontend-rnd-prod.100hp.app/', 'accept-language': self.ACCEPT_LANGUAGE}
        HEADERS_2 = {'User-Agent': self.USER_AGENT, 'access-control-request-method': 'POST', 'access-control-request-headers': 'authorization,x-user-id', 'origin': 'https://cryptocklicker-frontend-rnd-prod.100hp.app', 'sec-fetch-mode': 'cors', 'x-requested-with': self.X_REQUESTED_WITH, 'sec-fetch-site': 'same-site', 'sec-fetch-dest': 'empty', 'referer': 'https://cryptocklicker-frontend-rnd-prod.100hp.app/', 'accept-language': self.ACCEPT_LANGUAGE}
        PARAMS = {'task_id': Task['id']}

        try:
            for Num in range(1, 3):
                if Num == 2:
                    sleep(randint(3, 6)) # Промежуточное ожидание

                self.HPV_PRO.options(URL, headers=HEADERS_2, params=PARAMS, proxies=self.Proxy) # Пустой запрос
                HPV = self.HPV_PRO.post(URL, headers=HEADERS_1, params=PARAMS, proxies=self.Proxy).json()

                self.Empty_Request('Balance_2') # Пустой запрос
                self.Empty_Request('Balance_5') # Пустой запрос
                self.Empty_Request('Balance_1') # Пустой запрос
                self.Empty_Request('Balance_4') # Пустой запрос
                self.Empty_Request('user_profit_options') # Пустой запрос
                self.Empty_Request('user_profit_get') # Пустой запрос

                if Num == 2 and HPV['isCollected']:
                    self.Logging('Success', '⚡️', f'Задание с {Task["type"]} выполнено! +{HPV["money"]:,}')
        except:
            pass



    def AutoTasks(self) -> None:
        '''Выполнение заданий связанные с подписками'''

        try:
            Tasks = self.Get_Config('Quests') # Список доступных заданий

            self.Empty_Request('favicon_ico') # Пустой запрос

            # Старт выполнения заданий
            for Task in Tasks:
                self.Run_Tasks(Task) # Выполнение задания
                sleep(randint(2, 5)) # Промежуточное ожидание
        except:
            pass



    def Referal_Claim(self) -> dict:
        '''Сбор монет за рефералов'''

        URL_1 = self.Domain + 'friends/collect'
        URL_2 = self.Domain + 'friends?offset=0&limit=5'
        HEADERS = {'User-Agent': self.USER_AGENT, 'sec-ch-ua': self.SEC_CH_UA, 'sec-ch-ua-mobile': self.SEC_CH_UA_MOBILE, 'authorization': f'Bearer {self.Token}', 'x-user-id': self.TG_ID, 'sec-ch-ua-platform': self.SEC_CH_UA_PLATFORM, 'origin': 'https://cryptocklicker-frontend-rnd-prod.100hp.app', 'x-requested-with': self.X_REQUESTED_WITH, 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://cryptocklicker-frontend-rnd-prod.100hp.app/', 'accept-language': self.ACCEPT_LANGUAGE}

        self.Empty_Request('AutoRefClaim_1') # Пустой запрос
        self.Empty_Request('favicon_ico') # Пустой запрос

        try:
            RefClaim = self.HPV_PRO.get(URL_2, headers=HEADERS, proxies=self.Proxy).json()['total_coins'] # Наличие монет за рефералов

            if RefClaim:
                HPV = self.HPV_PRO.post(URL_1, headers=HEADERS, proxies=self.Proxy).json()['coinsCollected']
                self.Empty_Request('AutoRefClaim_1') # Пустой запрос
                self.Empty_Request('AutoRefClaim_2') # Пустой запрос
                return {'Status': True, 'Collected': f'{HPV:,}'}

            return {'Status': False}
        except:
            return {'Status': False}



    def AutoRefClaim(self) -> None:
        '''Автоматический сбор монет за рефералов'''

        try:
            Referal_Claim = self.Referal_Claim() # Сбор монет за рефералов

            if Referal_Claim['Status']:
                self.Logging('Success', '🟢', f'Монеты за рефералов собраны! +{Referal_Claim["Collected"]}')
                sleep(randint(3, 6)) # Промежуточное ожидание
        except:
            pass



    def Get_Card_ID(self, ID: str) -> dict:
        '''Получение ID карточек'''

        URL = self.Domain + 'minings'
        HEADERS = {'User-Agent': self.USER_AGENT, 'sec-ch-ua': self.SEC_CH_UA, 'sec-ch-ua-mobile': self.SEC_CH_UA_MOBILE, 'authorization': f'Bearer {self.Token}', 'x-user-id': self.TG_ID, 'sec-ch-ua-platform': self.SEC_CH_UA_PLATFORM, 'origin': 'https://cryptocklicker-frontend-rnd-prod.100hp.app', 'x-requested-with': self.X_REQUESTED_WITH, 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://cryptocklicker-frontend-rnd-prod.100hp.app/', 'accept-language': self.ACCEPT_LANGUAGE}

        self.Empty_Request('minings_options_get') # Пустой запрос

        try:
            HPV = self.HPV_PRO.get(URL, headers=HEADERS, proxies=self.Proxy).json()

            for CARD in HPV:
                if ID in CARD['id']:
                    return {'Status': True, 'Current': CARD['level'], 'New': f'{ID}{CARD["level"] + 1}'}

            return {'Status': True, 'Current': 0, 'New': f'{ID}1'}
        except:
            return {'Status': False}



    def Upgrade_Card(self, ID: str) -> bool:
        '''Апгрейд карточек'''

        URL = self.Domain + 'minings'
        HEADERS = {'User-Agent': self.USER_AGENT, 'sec-ch-ua': self.SEC_CH_UA, 'sec-ch-ua-mobile': self.SEC_CH_UA_MOBILE, 'authorization': f'Bearer {self.Token}', 'x-user-id': self.TG_ID, 'sec-ch-ua-platform': self.SEC_CH_UA_PLATFORM, 'origin': 'https://cryptocklicker-frontend-rnd-prod.100hp.app', 'x-requested-with': self.X_REQUESTED_WITH, 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://cryptocklicker-frontend-rnd-prod.100hp.app/', 'accept-language': self.ACCEPT_LANGUAGE}
        JSON = {'id': ID}

        self.Empty_Request('minings_options_post') # Пустой запрос

        try:
            self.HPV_PRO.post(URL, headers=HEADERS, json=JSON, proxies=self.Proxy).json()['totalProfit']
            return True
        except:
            return False



    def AutoUpgradeCard(self) -> None:
        '''Автоматический апгрейд всех карточек до максимально возможно уровня'''

        try:
            Updates = {}
            CARDS = list(set(sub(r'\d+', '', CARD['id']) for CARD in self.Get_Config('PassiveProfit'))) # Список всех карточек

            self.Empty_Request('favicon_ico') # Пустой запрос
            self.Empty_Request('minings_options_get') # Пустой запрос
            self.Empty_Request('tasks_everydayreward_options_get') # Пустой запрос
            self.Empty_Request('energy_improvements_options_get') # Пустой запрос
            self.Empty_Request('energy_bonus_options') # Пустой запрос
            self.Empty_Request('minings_get') # Пустой запрос
            self.Empty_Request('tasks_everydayreward_get') # Пустой запрос
            self.Empty_Request('energy_improvements_get') # Пустой запрос
            self.Empty_Request('energy_bonus_get') # Пустой запрос
            self.Empty_Request('AutoRefClaim_1') # Пустой запрос
            self.Empty_Request('AutoRefClaim_2') # Пустой запрос

            while True:
                # Остановка цикла, если все карточки улучшены (или нет) до максимально возможно уровня
                if all(Updates) and len(Updates) == len(CARDS): break

                for CARD in CARDS:
                    CARD_ID = self.Get_Card_ID(CARD) # Получение ID карточки

                    if CARD_ID['Current'] < MAX_LVL:
                        if self.Upgrade_Card(CARD_ID['New']): # Апгрейд карточки
                            self.Logging('Success', '🟢', f'Апгрейд {CARD} успешен! Новый уровень: {CARD_ID["New"][-1]}')
                        else:
                            Updates[CARD] = True

                        self.Empty_Request('minings_options_get') # Пустой запрос
                        self.Empty_Request('minings_get') # Пустой запрос
                        sleep(randint(2, 5)) # Промежуточное ожидание

                    else:
                        Updates[CARD] = True
        except:
            pass



    def Daily_Reward(self) -> dict:
        '''Получение ежедневной награды'''

        URL = self.Domain + 'tasks/everydayreward'
        HEADERS = {'User-Agent': self.USER_AGENT, 'sec-ch-ua': self.SEC_CH_UA, 'sec-ch-ua-mobile': self.SEC_CH_UA_MOBILE, 'authorization': f'Bearer {self.Token}', 'x-user-id': self.TG_ID, 'sec-ch-ua-platform': self.SEC_CH_UA_PLATFORM, 'origin': 'https://cryptocklicker-frontend-rnd-prod.100hp.app', 'x-requested-with': self.X_REQUESTED_WITH, 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://cryptocklicker-frontend-rnd-prod.100hp.app/', 'accept-language': self.ACCEPT_LANGUAGE}
        Reward = {1000: '1', 1500: '2', 2000: '3', 3000: '4', 4000: '5', 5000: '6', 6000: '7', 7000: '8', 8000: '9', 10000: '10', 13000: '11', 16000: '12', 20000: '13', 25000: '14', 30000: '15', 40000: '16', 50000: '17', 70000: '18', 90000: '19', 100000: '20', 125000: '21', 150000: '22', 200000: '23', 300000: '24'}

        self.Empty_Request('tasks_everydayreward_options_post') # Пустой запрос

        try:
            HPV = self.HPV_PRO.post(URL, headers=HEADERS, proxies=self.Proxy).json()['collectedCoins']
            return {'Status': True, 'Collected': f'{HPV:,}', 'Day': f'{Reward[HPV]}'}
        except:
            return {'Status': False}



    def AutoDailyReward(self) -> None:
        '''Автоматическое получение ежедневной награды'''

        URL = self.Domain + 'tasks/everydayreward'
        HEADERS = {'User-Agent': self.USER_AGENT, 'sec-ch-ua': self.SEC_CH_UA, 'sec-ch-ua-mobile': self.SEC_CH_UA_MOBILE, 'authorization': f'Bearer {self.Token}', 'x-user-id': self.TG_ID, 'sec-ch-ua-platform': self.SEC_CH_UA_PLATFORM, 'origin': 'https://cryptocklicker-frontend-rnd-prod.100hp.app', 'x-requested-with': self.X_REQUESTED_WITH, 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://cryptocklicker-frontend-rnd-prod.100hp.app/', 'accept-language': self.ACCEPT_LANGUAGE}

        self.Empty_Request('Balance_1') # Пустой запрос
        self.Empty_Request('Balance_4') # Пустой запрос
        self.Empty_Request('user_profit_options') # Пустой запрос
        self.Empty_Request('user_profit_get') # Пустой запрос
        self.Empty_Request('tasks_everydayreward_options_get') # Пустой запрос

        try:
            HPV = self.HPV_PRO.get(URL, headers=HEADERS, proxies=self.Proxy).json()['days']

            if not all(Day['isCollected'] for Day in HPV):
                Daily_Reward = self.Daily_Reward() # Получение ежедневной награды

                if Daily_Reward['Status']:
                    self.Logging('Success', '🟢', f'Ежедневная награда получена! День: {Daily_Reward["Day"]}! +{Daily_Reward["Collected"]}')

                    self.Empty_Request('tasks_everydayreward_options_get') # Пустой запрос
                    self.Empty_Request('tasks_everydayreward_get') # Пустой запрос
                    sleep(randint(3, 6)) # Промежуточное ожидание
        except:
            pass



    def Click(self) -> None:
        '''Совершение тапов'''

        URL = self.Domain + 'tap'
        HEADERS = {'User-Agent': self.USER_AGENT, 'sec-ch-ua': self.SEC_CH_UA, 'sec-ch-ua-mobile': self.SEC_CH_UA_MOBILE, 'authorization': f'Bearer {self.Token}', 'x-user-id': self.TG_ID, 'sec-ch-ua-platform': self.SEC_CH_UA_PLATFORM, 'origin': 'https://cryptocklicker-frontend-rnd-prod.100hp.app', 'x-requested-with': self.X_REQUESTED_WITH, 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://cryptocklicker-frontend-rnd-prod.100hp.app/', 'accept-language': self.ACCEPT_LANGUAGE}
        JSON = {'tapsCount': randint(COINS[0], COINS[1])}

        self.Empty_Request('tap_options') # Пустой запрос

        try:
            self.HPV_PRO.post(URL, headers=HEADERS, json=JSON, proxies=self.Proxy)
            self.Logging('Success', '🟢', 'Тап совершён!')
        except:
            self.Logging('Error', '🔴', 'Не удалось тапнуть!')



    def AutoClick(self) -> None:
        '''30 минут беспрерывного тапания'''

        try:
            for _ in range(randint(900, 1_800)):
                self.Click()
                sleep(randint(1, 2)) # Промежуточное ожидание
        except:
            pass



    def Get_Boosts(self) -> list:
        '''Получение списка доступных бустов'''

        URL = self.Domain + 'energy/improvements'
        HEADERS = {'User-Agent': self.USER_AGENT, 'sec-ch-ua': self.SEC_CH_UA, 'sec-ch-ua-mobile': self.SEC_CH_UA_MOBILE, 'authorization': f'Bearer {self.Token}', 'x-user-id': self.TG_ID, 'sec-ch-ua-platform': self.SEC_CH_UA_PLATFORM, 'origin': 'https://cryptocklicker-frontend-rnd-prod.100hp.app', 'x-requested-with': self.X_REQUESTED_WITH, 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://cryptocklicker-frontend-rnd-prod.100hp.app/', 'accept-language': self.ACCEPT_LANGUAGE}

        self.Empty_Request('energy_improvements_options_get') # Пустой запрос

        try:
            return [{'ID': Card['id'], 'LVL': Card['level']} for Card in self.HPV_PRO.get(URL, headers=HEADERS, proxies=self.Proxy).json() if not Card['isMaxLevel']]
        except:
            return []



    def Upgrade_Boosts(self, ID: str) -> bool:
        '''Апгрейд буста'''

        URL = self.Domain + 'energy/improvements'
        HEADERS = {'User-Agent': self.USER_AGENT, 'sec-ch-ua': self.SEC_CH_UA, 'sec-ch-ua-mobile': self.SEC_CH_UA_MOBILE, 'authorization': f'Bearer {self.Token}', 'x-user-id': self.TG_ID, 'sec-ch-ua-platform': self.SEC_CH_UA_PLATFORM, 'origin': 'https://cryptocklicker-frontend-rnd-prod.100hp.app', 'x-requested-with': self.X_REQUESTED_WITH, 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://cryptocklicker-frontend-rnd-prod.100hp.app/', 'accept-language': self.ACCEPT_LANGUAGE}
        JSON = {'id': ID}

        self.Empty_Request('energy_improvements_options_post') # Пустой запрос

        try:
            self.HPV_PRO.post(URL, headers=HEADERS, json=JSON, proxies=self.Proxy).json()['NextLevel']
            return True
        except:
            return False



    def AutoUpgradeBoosts(self) -> None:
        '''Автоматический апгрейд бустов'''

        try:
            for Boost in self.Get_Boosts(): # Получение списка доступных бустов

                # Улучшение `Запас энергии` буста (максимальная ёмкость энергии)
                if 'energylimit' in Boost['ID'] and Boost['LVL'] < MAX_ENERGY_LIMIT:
                    if self.Upgrade_Boosts(Boost['ID']):
                        self.Logging('Success', '⚡️', 'Буст `Запас энергии` улучшен!')
                        sleep(randint(3, 6)) # Промежуточное ожидание

                # Улучшение `Восстановление энергии` буста (скорость восстановления энергии)
                if 'energyregen' in Boost['ID'] and Boost['LVL'] < MAX_ENERGY_REGEN:
                    if self.Upgrade_Boosts(Boost['ID']):
                        self.Logging('Success', '⚡️', 'Буст `Восстановление энергии` улучшен!')
                        sleep(randint(3, 6)) # Промежуточное ожидание
        except:
            pass



    def _1win_Games(self) -> None:
        '''Пустые запросы для просмотра игр 1win'''

        self.Empty_Request('favicon_ico') # Пустой запрос
        self.Empty_Request('Games_1win') # Пустой запрос
        self.Empty_Request('wallet_list_options') # Пустой запрос
        self.Empty_Request('wallet_list_get') # Пустой запрос



    def AutoUpgradeProfile(self) -> None:
        '''Автоматические апгрейд всех карточек, получение ежедневной награды и апгрейд бустов'''

        self.AutoUpgradeCard() # Автоматический апгрейд всех карточек до максимально возможно уровня
        sleep(randint(2, 5)) # Промежуточное ожидание
        self.AutoDailyReward() # Автоматический апгрейд бустов
        sleep(randint(2, 5)) # Промежуточное ожидание
        self.AutoUpgradeBoosts() # Автоматический апгрейд бустов
        sleep(randint(2, 5)) # Промежуточное ожидание



    def Run(self) -> None:
        '''Активация бота'''

        while True:
            try:
                if self.Token: # Если аутентификация успешна

                    INFO = self.Get_Info()
                    Balance = INFO['Balance'] # Баланс
                    Hour_Profit = INFO['Hour_Profit'] # Прибыль в час
                    Click_Power = INFO['Click_Power'] # Сила клика
                    self.Logging('Success', '💰', f'Баланс: {Balance} /// Прибыль в час: {Hour_Profit} /// Сила клика: {Click_Power}')


                    self.Empty_Request('user_profit_options') # Пустой запрос
                    self.Empty_Request('user_profit_get') # Пустой запрос
                    self.Empty_Request('Balance_7') # Пустой запрос
                    self.Empty_Request('Balance_8') # Пустой запрос
                    self.Empty_Request('tokens_bonus_options') # Пустой запрос
                    self.Empty_Request('tokens_bonus_get') # Пустой запрос


                    # Рандомное выполнение действий: выполнение заданий, сбор монет за рефералов, 30 минут беспрерывного тапанья и пустые запросы для просмотра игр 1win, а также апгрейд карточек, бустов и получение получение ежедневной награды
                    Autos = [self.AutoTasks, self.AutoRefClaim, self.AutoClick, self._1win_Games, self.AutoUpgradeProfile]
                    shuffle(Autos) # Перемешивание списока функций
                    for Auto in Autos:
                        Auto()
                        sleep(randint(3, 6)) # Промежуточное ожидание


                    Waiting = randint(3*60*60, 5*60*60) # Значение времени в секундах для ожидания
                    Waiting_STR = (datetime.now() + timedelta(seconds=Waiting)).strftime('%Y-%m-%d %H:%M:%S') # Значение времени в читаемом виде


                    _INFO = self.Get_Info()
                    _Balance = _INFO['Balance'] # Баланс
                    _Hour_Profit = _INFO['Hour_Profit'] # Прибыль в час
                    _Click_Power = _INFO['Click_Power'] # Сила клика


                    self.Logging('Success', '💰', f'Баланс: {_Balance} /// Прибыль в час: {_Hour_Profit} /// Сила клика: {_Click_Power}')
                    self.Logging('Warning', '⏳', f'Следующий сбор: {Waiting_STR}!')


                    # Ожидание от 3 до 5 часов
                    Waiting_For_Upgrade = int(Waiting / (60*30))
                    for _ in range(Waiting_For_Upgrade):
                        if HPV_Upgrade_Alert(): # Проверка наличия обновления
                            return
                        sleep(60*30)
                    sleep(Waiting - (Waiting_For_Upgrade * 60 * 30))
                    self.ReAuthentication() # Повторная аутентификация аккаунта

                else: # Если аутентификация не успешна
                    if HPV_Upgrade_Alert(): # Проверка наличия обновления
                        return
                    sleep(randint(33, 66)) # Ожидание от 33 до 66 секунд
                    self.ReAuthentication() # Повторная аутентификация аккаунта

            except:
                if HPV_Upgrade_Alert(): # Проверка наличия обновления
                    return







if __name__ == '__main__':

    if s_name() == 'Windows':
        sys('cls'); sys('title HPV 1win - V2.08')
    else:
        sys('clear')

    while True:
        HPV_Banner() # Вывод баннера
        HPV_Config_Check() # Проверка конфига на валидность
        print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Проверка конфига окончена... Скрипт запустится через 5 секунд...\n'); sleep(5)

        Console_Lock = Lock()
        Threads = [] # Список потоков

        def Start_Thread(Name: str, URL: str, Proxy: dict, Headers: dict) -> None:
            _1win = HPV_1win(Name, URL, Proxy, Headers)
            _1win.Run()

        # Получение конфигурационных данных и запуск потоков
        for Account in HPV_Get_Config(_print=False):
            HPV = Thread(target=Start_Thread, args=(Account['Name'], Account['URL'], Account['Proxy'], Account['Headers'],))
            HPV.start()
            Threads.append(HPV)

        for thread in Threads:
            thread.join()


