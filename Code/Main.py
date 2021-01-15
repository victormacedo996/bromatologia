from Essentials import getOption, getInteger
from time import sleep
from os import system
from Menus import mainMenu, waterMenu, wheatFlourMenu, honeyMenu, sucroseMenu

while True:
    mainMenu()
    food_choice = getInteger ('Choose the food for analisys: ')
    if food_choice > 4 or food_choice < 0:
        print('Invalid option')
        sleep(1)
    else:
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



