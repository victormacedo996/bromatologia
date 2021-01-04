from Essencials import getOption, getFloat
def displayOptions(option_list):
    """
    Function to print the options for the menus contained in a list
    """
    for item in option_list:
        if item == 'Exit' or item == 'Back to main menu':
            print(f"  0. {item}")
        else:
            print(f"  {option_list.index(item) + 1}. {item}")

def mainMenu ():
    """
    Function to print the main menu of the program
    """
    system('clear')
    print('Welcome to the FOOD ANALYSIS CALCULATOR!')
    print('Foods that can be analysed:')
    options = ['Wheat flour', 'Honey', 'Sucrose', 'Water', 'Exit']
    displayOptions(options)

def wheatFlourMenu ():
    """
    Function to print the menu for the menu for the wheat flour analysis
    """
    system('clear')
    print('Wheat flour selected')
    print('Wich parameter do you want to analyse?')
    options = ['Fixed mineral waste', 'Acidity', 'Protein', 'Back to main menu']
    displayOptions(options)

def honeyMenu ():
    """
    Function to print the menu for the menu for the honey analysis
    """
    system('clear')
    print('Honey selected')
    print('Wich parameter do you want to analyse?')
    options = ['Inverted sugar', 'Sucrose', 'Acidity', 'Formol index', 'Back to main menu']
    displayOptions(options)
    

def sucroseMenu ():
    """
    Function to print the menu for the menu for the sucrose analysis
    """
    system('clear')
    print('Sucrose selected')
    print('Wich parameter do you want to analyse?')
    options = ['Sucrose by polarimetry', 'Sucrose by Fehlings method', 'ICUMSA colour', 'Back to main menu']
    displayOptions(options)

def waterMenu ():
    """
    Function to print the menu for the menu for the water analysis
    """
    system('clear')
    print('water selected')
    print('Wich parameter do you want to analyse?')
    options = ['Alcalinity', 'Water hardness', 'Total soluble solids', 'Residual chlorine', 
                'Chloride', 'Oxigen consumed', 'Back to main menu']
    displayOptions(options)
    select_option = getOption (options)
    if select_option == False:
        mainMenu()
    elif select_option == 1:
        from Water import alcalinity
        H2SO4_concentration = getFloat ('Enter the H2SO4 concentration: ')
        H2SO4_fc = getFloat ('Enter the H2SO4 correction factor: ')
        water_volume_used = ('Enter the water volume used: ')
        volume_spent_with_phenolphthalein = []
        volume_spent_with_methyl_orange = []
        data_set = []
        i = 1
        while True:
            if i == 1:
                r = f"{i}st"
            elif i == 2:
                r = f"{i}nd"
            elif i == 3:
                r = f"{i}rd"
            else:
                r = f"{i}th"
            phenolphthalein = getFloat(f"Enter {r} volume of phenolphthalein: ")
            methyl_orange = getFloat(f"Enter {r} volume of methyl orange: ")
            volume_spent_with_phenolphthalein.append(phenolphthalein)
            volume_spent_with_methyl_orange.append(methyl_orange)
            if 
        
        for phenolphthalein, methyl_orange in zip(volume_spent_with_phenolphthalein, volume_spent_with_methyl_orange):
            alcalinity = alcalinity(H2SO4_concentration, H2SO4_fc, phenolphthalein, methyl_orange, water_volume_used)
            data_set.append(alcalinity)

