from Essencials import getOption, getInteger
from time import sleep
from os import system
from Menus import mainMenu, waterMenu, wheatFlourMenu

mainMenu()

while True:
    food_choice = getInteger ('Choose the food for analisys: ')

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
        sleep(1.5)
        exit()



