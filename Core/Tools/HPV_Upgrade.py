from subprocess import run as terminal, Popen
from os import path
from sys import exit, executable
from platform import system as s_name
from colorama import Fore

from Core.Config.HPV_Config import AUTO_UPDATE



PATH = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) # Путь к главной директории



def HPV_Upgrade_Alert() -> bool:
    '''Проверка наличия обновления'''

    try:
        if AUTO_UPDATE:
            terminal(['git', 'fetch'], cwd=PATH, check=True) # Загрузка последних изменений
            CHECK = terminal(['git', 'status', '-uno'], cwd=PATH, capture_output=True, text=True).stdout # Проверка состояния файлов
            return True if 'Your branch is behind' in CHECK else False
        else:
            return False
    except:
        return False



def HPV_Upgrade() -> None:
    '''Автоматическая проверка и установка обновления'''

    print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Проверка наличия обновления... Подождите немного!')
    PIP = 'pip' if s_name() == 'Windows' else 'pip3' # Определение ОС, для установки зависимостей
    HPV_Requirements = path.join(path.dirname(path.abspath(__file__)), 'HPV_Requirements.txt') # Путь к файлу с зависимостями

    try:
        if HPV_Upgrade_Alert():
            print(Fore.MAGENTA + '[HPV]' + Fore.YELLOW + ' — Обнаружено обновление!')

            if AUTO_UPDATE:
                print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Идёт процесс обновления... Подождите немного!')
                terminal(['git', 'pull'], cwd=PATH, check=True) # Обновление локального репозитория

                print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Установка зависимостей...')
                terminal([PIP, 'install', '-r', HPV_Requirements], check=True) # Установка зависимостей

                print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Перезапуск программы...')
                Popen([executable, path.join(PATH, 'HPV_1win.py')]); exit() # Перезапуск программы

            else:
                print(Fore.MAGENTA + '[HPV]' + Fore.YELLOW + ' — Автообновления отключены! Обновление не установлено!')

        else:
            print(Fore.MAGENTA + '[HPV]' + Fore.GREEN + ' — Обновлений не обнаружено!')

    except Exception as ERROR:
        print(Fore.MAGENTA + '[HPV]' + Fore.RED + f' — Что-то пошло не так!\n\tОшибка: {ERROR}')


