from shutil import get_terminal_size as gts
from colorama import Fore
from time import sleep



HPV_TEAM = f'''
 _  _ _____   __   ___      _____ _  _ 
| || | _ \ \ / /__/ \ \    / /_ _| \| |
| __ |  _/\ V /___| |\ \/\/ / | || .` |
|_||_|_|   \_/    |_| \_/\_/ |___|_|\_|
+-----------------------------------------+
| Контент: t.me/HPV_TEAM /// t.me/HPV_PRO |
+-----------------------------------------+
| Сотрудничество: t.me/HPV_BASE |
+-------------------------------+
| Автор: t.me/A_KTO_Tbl |
+-----------------------+
| V2.08 |
+-------+
'''



def HPV_Banner():
    '''Вывод баннера'''

    for HPV in HPV_TEAM.split('\n'): # Вывод баннера
        print(Fore.MAGENTA + HPV.center(gts()[0], ' '))
        sleep(0.026)


