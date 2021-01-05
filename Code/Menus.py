from Statistic import dixonTest, Ttest
from Essencials import getOption, getFloat, getAnswer, getInteger
from os import system
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
    select_option = getInteger ('Enter 1: ')#getOption (options)
    if select_option == False:
        mainMenu()
    elif select_option == 1:
        from Water import alcalinity
        """
        Getting the constants
        """
        H2SO4_concentration = getFloat ('Enter the H2SO4 concentration: ')
        H2SO4_fc = getFloat ('Enter the H2SO4 correction factor: ')
        water = getFloat('Enter the water volume used: ')
        volume_spent_with_phenolphthalein = [] ## List to store the users input
        volume_spent_with_methyl_orange = [] ## List to store the users input
        data_set = [] ## List to store the results
        i = 1 ## Counting variable
        answer = 'y' 
        while True:
        # Loop while to get the variables of the samples
        
            if i == 1: ## Condition to print the right ordinal number
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
            answer = getAnswer ('Add another sample? (Y/N): ')
            if len(volume_spent_with_phenolphthalein) < 3 and answer != 'y':
                answer = 'y'
                print('You must enter at least 3 samples')
            elif answer != 'y':
                break
            else:
                if len(volume_spent_with_phenolphthalein) == 10:
                    break
                else:
                    pass
            i += 1
        for phenolphthalein, methyl_orange in zip(volume_spent_with_phenolphthalein, volume_spent_with_methyl_orange):
            """
            For loop to run throught the list of samples and apply them in the alcalinity 
            function and append the result in the data_set list
            """
            result = alcalinity(H2SO4_concentration, H2SO4_fc, phenolphthalein, methyl_orange, water)
            data_set.append(result)

        system('clear')
        print('Statistical analisys - Dixon test')
        print('Dixons confidence intervals:')
        print("""
                1. 90%
                2. 95%
                3. 99%
                """)
        confidence_interval = 0
        while True:
            confidence_interval = getInteger ('Enter the confidence interval: ')
            if confidence_interval < 1 or confidence_interval > 3:
                print('You must enter a valid confidence interval')
            else:
                if confidence_interval == 1:
                    confidence_interval = 0.9
                    break
                elif confidence_interval == 2:
                    confidence_interval = 0.95
                    break
                else:
                    confidence_interval = 0.99
                    break

        ## Executing dixon test with the data for each variable
        print('Dixon test result:')
        print('Carbonate')
        carbonate = dixonTest (list(item[0] for item in data_set), confidence_interval)
        print('\n')
        print('Bicarbonate')
        bicarbonate = dixonTest (list(item[1] for item in data_set), confidence_interval)
        print('\n')
        print('Hydroxide')
        hydroxide = dixonTest (list(item[2] for item in data_set), confidence_interval)
        print('\n')

        print('Statistical analisys - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        print('Students T test results:')
        print('Carbonate')
        Ttest(carbonate, comparable, confidence_interval)
        print('\n')
        print('Bicarbonate')
        Ttest(bicarbonate, comparable, confidence_interval)
        print('\n')
        print('Hydroxide')
        Ttest(hydroxide, comparable, confidence_interval)




