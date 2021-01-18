from Essentials import getInteger
from time import sleep
from os import system
from Menus import mainMenu, waterMenu, wheatFlourMenu, honeyMenu, sucroseMenu, licenseMenu, OilsMenu

while True:
    mainMenu()
    food_choice = getInteger ('Choose the food for analisys: ')
    if food_choice > 5 or food_choice < 0:
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

        elif food_choice == 5:
            OilsMenu()
            
        elif food_choice == 6:
            licenseMenu()
            
        else:
            print("""
            Thank you for using Food Analitycs!!
            Don't forget to check the repository and support the project
            https://github.com/victormacedo996/food-analytics
            """)
            sleep(1.5)
            exit()



