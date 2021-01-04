from Essencials import getOption
from time import sleep
from os import system
import Menus

mainMenu()


food_choice = getFood('Wich food do you want to analyse? ')

if food_choice == 1:
    wheatFlourMenu ()
elif food_choice == 2:
    honeyMenu ()
elif food_choice == 3:
    sucroseMenu ()
elif food_choice == 4:
    waterMenu ()
else:
    print('Thank you for using the program')
    sleep(2)
    exit()



