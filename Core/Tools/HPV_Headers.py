from random import choice, randint

from Core.Tools.Headers_Tools.HPV_Chrome_Version import HPV_CHROME_VERSION
from Core.Tools.Headers_Tools.HPV_Phone_Model import HPV_PHONE_MODEL
from Core.Tools.Headers_Tools.HPV_Telegram_Client import HPV_TELEGRAM_CLIENT



def HPV_Headers() -> dict:
    '''Генератор уникальных параметров для Headers'''

    HPV_Chrome_Version = choice(HPV_CHROME_VERSION) # Версия Google Chrome
    HPV_Android_Version = randint(11, 14) # Версия Android
    HPV_Phone_Model = choice(HPV_PHONE_MODEL) # Модель телефона
    HPV_Telegram_Client = choice(HPV_TELEGRAM_CLIENT) # Клиент Telegram

    USER_AGENT = f'Mozilla/5.0 (Linux; Android {HPV_Android_Version}; {HPV_Phone_Model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{HPV_Chrome_Version} Mobile Safari/537.36'
    SEC_CH_UA = f'"Chromium";v="{HPV_Chrome_Version.split(".")[0]}", "Not(A:Brand";v="99", "Google Chrome";v="{HPV_Chrome_Version.split(".")[0]}"'
    SEC_CH_UA_MOBILE = '?1'
    SEC_CH_UA_PLATFORM = '"Android"'
    X_REQUESTED_WITH = HPV_Telegram_Client

    return {'USER_AGENT': USER_AGENT, 'SEC_CH_UA': SEC_CH_UA, 'SEC_CH_UA_MOBILE': SEC_CH_UA_MOBILE, 'SEC_CH_UA_PLATFORM': SEC_CH_UA_PLATFORM, 'X_REQUESTED_WITH': X_REQUESTED_WITH}


