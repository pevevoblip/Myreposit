
import colorama #Встановлення
dir(colorama) #Інтроспекція

from colorama import Fore
print(Fore.RED + "Червоний текст") #Зміна коліру на червоний

from colorama import init, Fore
init(autoreset=True)
print(Fore.RED + "Цей текст червоний, але наступний буде стандартним!") #Фарбування одного рядка

print('Hi')


