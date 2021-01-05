from Statistic import dixonTest, Ttest
from Essencials import getOption, getFloat, getAnswer, getInteger
from Essencials import getDixonConfidenceInterval, displayOptions, getOneSample, getTwoSamples
from os import system

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
    select_option = getInteger ('Enter 1: ')
    if select_option == False:
        mainMenu()

    ## Condition to calculate water alcalinity ##
    elif select_option == 1:
        from Water import alcalinity
        """
        Getting the constants
        """
        system('clear')
        print('Water alcalinity selected')
        print('\n')

        ## Getting constants ##
        H2SO4_concentration = getFloat ('Enter the H2SO4 concentration: ')
        H2SO4_fc = getFloat ('Enter the H2SO4 correction factor: ')
        water = getFloat('Enter the water volume used: ')
        

        volume_spent_with_phenolphthalein, volume_spent_with_methyl_orange = getTwoSamples ('phenolphthalein', 'methyl orange')

        data_set = [] ## List to store the results
        for phenolphthalein, methyl_orange in zip(volume_spent_with_phenolphthalein, volume_spent_with_methyl_orange):
            """
            For loop to run throught the list of samples and apply them in the alcalinity 
            function and append the result in the data_set list
            """
            result = alcalinity(H2SO4_concentration, H2SO4_fc, phenolphthalein, methyl_orange, water)
            data_set.append(result)

        system('clear')
        ## Statistical analysis
        print('Statistical analisys - Dixon test')
        print('Dixons confidence intervals:')
        confidence_interval = getDixonConfidenceInterval ()

        ## Executing dixon test with the data for each variable
        print('Dixon test result:')
        print('\n')
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
        ## Executing Students T test for each variable
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable_carbonate = getFloat('Enter the comparable for carbonate: ')
        comparable_bicarbonate = getFloat('Enter the comparable for bicarbonate: ')
        comparable_hydroxide = getFloat('Enter the comparable for hydroxide: ')
        print('Students T test results:')
        print('\n')
        print('Carbonate')
        Ttest(carbonate, comparable_carbonate, confidence_interval)
        print('\n')
        print('Bicarbonate')
        Ttest(bicarbonate, comparable_bicarbonate, confidence_interval)
        print('\n')
        print('Hydroxide')
        Ttest(hydroxide, comparable_hydroxide, confidence_interval)

    ## Condition to calculate water hardness ##
    elif select_option == 2:
        from Water import waterHardness
        system('clear')
        print('Water hardness selected')
        print('\n')

        ## Getting constants ##
        EDTA_standard = getFloat ('Enter the EDTA standard: ')
        quantity_of_CaCO3_neutralized_by_EDTA = getFloat ('Enter the quantity of CaCO3 nwutralized by the EDTA: ')
        EDTA_molatity = getFloat ('Enter the EDTA molarity: ')
        EDTA_fc = getFloat ('Enter the correction factor of the EDTA: ')
        sample_volume = getFloat ('Enter the sample volume: ')

        ## Getting variables ##
        EDTA_spent = getOneSample ('Enter the EDTA spent')

        ## Loop to execute the alcalinity function with every variable ##
        data_set = [] ## List to store the results
        for item in EDTA_spent:
            result = waterHardness (EDTA_standard, quantity_of_CaCO3_neutralized_by_EDTA, EDTA_molatity, EDTA_fc, item, sample_volume)
            data_set.append(result)
        
        system('clear')


        print('Statistical analisys - Dixon test')
        confidence_interval = getDixonConfidenceInterval ()
        ## Executing dixon test
        dixon_data_set = dixonTest (data_set, confidence_interval)
        print('\n')

        print('Statistical analisys - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)

    ## Condition to calculate total soluble solids ##
    elif select_option == 3:
