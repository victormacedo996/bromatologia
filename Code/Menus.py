def mainMenu ():
    from Statistic import dixonTest, Ttest
    from Essencials import getOption, getFloat, getAnswer, getInteger
    from Essencials import getDixonConfidenceInterval, displayOptions, getOneSample, getTwoSamples
    from os import system
    """
    Function to print the main menu of the program
    """
    system('clear')
    print('Welcome to the FOOD ANALYSIS CALCULATOR!')
    print('Foods that can be analysed:')
    options = ['Wheat flour', 'Honey', 'Sucrose', 'Water', 'Exit']
    displayOptions(options)
    
def wheatFlourMenu ():
    from Statistic import dixonTest, Ttest
    from Essencials import getOption, getFloat, getAnswer, getInteger
    from Essencials import getDixonConfidenceInterval, displayOptions, getOneSample, getTwoSamples
    from os import system
    """
    Function to print the menu for the menu for the wheat flour analysis
    """
    system('clear')
    print('Wheat flour selected')
    print('Wich parameter do you want to analyse?')
    options = ['Fixed mineral waste', 'Acidity', 'Protein', 'Back to main menu']
    displayOptions(options)
    select_option = getInteger ('Choose the analysis: ')
    if select_option == False:
        mainMenu()

    ## Condition to calculate fixed mineral waste ##
    elif select_option == 1:
        system('clear')
        print('Fixed mineral waste selected')
        ## Getting constants ## 
        crucible_tare = getFloat ('Enter the crucible tare: ')
        sample_weight = getFloat ('Enter the sample weight: ')
        sample_humidity = getFloat ('Enter the sample humidity (ex: 20% = 20): ')

        ## Getting variable ##
        weight_after_calcination = getOneSample ('weight after calcination')

        data_set = []
        for item in weight_after_calcination:
            result = fixedMineralWaste (crucible_tare, sample_weight, item, sample_humidity)
            data_set.append(result)

        system('clear')
        ## Executing dixon test ##
        print('Statistical analisys - Dixon test')
        print('\n')

        conidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest(data_set, confidence_interval)
        print('\n')

        ## Executing Students T test ##
        print('Statistical analisys - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)

    ## Condition to calculate acidity ##
    elif select_option == 2:
        system('clear')
        print('Acidity selected')

        ## Getting constants ##
        flour_solution_percentage = getFloat ('Enter the percentage of the flour solution (ex: 10% = 10): ')
        volume_of_flour_solution_used =  getFloat ('Enter the volume of flour solution used: ')
        NaOH_molarity = getFloat ('Enter the NaOH molarity: ')
        NaOH_fc = ('Enter the correction factor of the NaOH: ')
        sample_humidity = ('Enter the sample humidity: ')

        ## Getting variable ##
        volume_of_NaOH_spent = getOneSample ('volume of NaOH spent')

        data_set = []
        for item in volume_of_NaOH_spent:
            result = acidity(flour_solution_percentage, volume_of_flour_solution_used, item, NaOH_molarity, NaOH_fc, sample_humidity)
            data_set.append(result)

        system('clear')
        ## Executing dixon test ##
        print('Statistical analisys - Dixon test')
        print('\n')

        conidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest(data_set, confidence_interval)
        print('\n')

        ## Executing Students T test ##
        print('Statistical analisys - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)

    elif select_option == 3:
        




def honeyMenu ():
    from Statistic import dixonTest, Ttest
    from Essencials import getOption, getFloat, getAnswer, getInteger
    from Essencials import getDixonConfidenceInterval, displayOptions, getOneSample, getTwoSamples
    from os import system
    """
    Function to print the menu for the menu for the honey analysis
    """
    system('clear')
    print('Honey selected')
    print('Wich parameter do you want to analyse?')
    options = ['Inverted sugar', 'Sucrose', 'Acidity', 'Formol index', 'Back to main menu']
    displayOptions(options)
    

def sucroseMenu ():
    from Statistic import dixonTest, Ttest
    from Essencials import getOption, getFloat, getAnswer, getInteger
    from Essencials import getDixonConfidenceInterval, displayOptions, getOneSample, getTwoSamples
    from os import system
    """
    Function to print the menu for the menu for the sucrose analysis
    """
    system('clear')
    print('Sucrose selected')
    print('Wich parameter do you want to analyse?')
    options = ['Sucrose by polarimetry', 'Sucrose by Fehlings method', 'ICUMSA colour', 'Back to main menu']
    displayOptions(options)

def waterMenu ():
    from Statistic import dixonTest, Ttest
    from Essencials import getOption, getFloat, getAnswer, getInteger
    from Essencials import getDixonConfidenceInterval, displayOptions, getOneSample, getTwoSamples
    from os import system
    """
    Function to print the menu for the menu for the water analysis
    """
    system('clear')
    print('water selected')
    print('Wich parameter do you want to analyse?')
    options = ['Alcalinity', 'Water hardness', 'Total soluble solids', 'Residual chlorine', 
                'Chloride', 'Oxigen consumed', 'Back to main menu']

    displayOptions(options)
    select_option = getInteger ('Choose the analysis: ')
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
        from Essencials import getFloat
        H2SO4_concentration = getFloat ('Enter the H2SO4 molarity: ')
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

    ## Condition to calculate the total soluble solids ##
    elif select_option == 3:
        from Water import totalSolubleSolids
        system ('clear')
        print('Total soluble solids selected')
        print('\n')

        capsule_weight = getOneSample ('capsule weight')
        total_weight_after_dry = getOneSample ('weight after dryed (capsule + sample)')
        sample_volume = getOneSample ('sample volume')

        data_set = []
        for capsule_weight, total_weight_after_dry, sample_volume in zip(capsule_weight, total_weight_after_dry, sample_volume):
            result = totalSolubleSolids (capsule_weight, total_weight_after_dry, sample_volume)
            data_set.append(result)

        system ('clear')

        ## Executing dixon test ##
        print('Statistical analisys - Dixon test')
        print('\n')

        conidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest(data_set, confidence_interval)
        print('\n')

        ## Executing Students T test ##
        print('Statistical analisys - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)

    ## Condition to calculate total residual chlorine ##
    elif select_option == 4:
        from Water import residualChlorine
        system ('clear')
        print('Residual chlorine selected')
        print('\n')

        ## Getting constants ##
        Na2S2O3_molarity = getFloat ('Enter the Na2S2O3 molarity: ')
        Na2S2O3_fc = getFloat = ('Enter the correction factor of the Na2SO3: ')
        sample_volume = getFloat('Enter the sample volume: ')

        ## Getting variables ##
        Na2S2O3_volume_used = getOneSample ('volume of Na2SO3 used')

        ## Applying the function to all variables ##
        data_set = []
        for item in Na2S2O3_volume_used:
            result = residualChlorine (Na2S2O3_molarity, Na2S2O3_fc, item, sample_volume)
            data_set.append(result)
        
        ## Executing Dixon test ##
        print('Statistical analysis - Dixon test')
        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest (data_set, confidence_interval)

        ## Executing Students T test ##
        print('Statistical analysis - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)

    ## Condition to calculate chloride ##
    elif select_option == 5:
        from Water import chloride
        system ('clear')
        print('Chloride selected')
        print('\n')

        ## Getting constants ##
        AgNO3_molarity = getFloat ('Enter AgNO3 molarity: ')
        AgNO3_fc = getFloat ('Enter the correction factor of the AgNO3: ')
        sample_volume = getFloat('Enter the sample volume: ')
        AgNO3_volume_used = getOneSample ('volume of AgNO3 spent')

        data_set = []
        for item in AgNO3_volume_used:
            result = chloride (AgNO3_molarity, AgNO3_fc, item, sample_volume)
            data_set.append(result)

        ## Executing Dixon test ##
        system('clear')
        print('Statistical analysis - Dixon test')
        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest (data_set, confidence_interval)

        ## Executing Students T test ##
        print('Statistical analysis - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)

    ## Condition to calculate the consumed oxigen ##
    elif select_option == 6:
        from Water import consumedOxigen
        ## Getting constants ##
        sample_volume = getFloat('Enter the sample volume: ')
        KMnO4_molarity = getFloat ('Enter the KMnO4 molarity: ')
        KMnO4_fc = getFloat ('Enter the correction factor for the KMnO4: ')
        Na2C2O4_molarity = getFloat ('Enter the Na2C2O4 molarity: ')
        Na2C2O4_fc = getFloat ('Enter the correction factor for the Na2C2O4: ')
        second_KMnO4_molarity = getFloat ('Enter the second KMnO4 used molarity: ')
        second_KMnO4_fc = getFloat ('Enter the second correction factor for the second KMnO4: ')

        ## Getting variables ##
        KMnO4_volume_used = getOneSample ('fist KMnO4 volume used')
        Na2C2O4_volume_used = getOneSample ('Na2C2O4 volume used')
        second_KMnO4_volume_used = getOneSample ('second KMnO4 volume used')

        data_set = []

        for item1, item2, item3 in zip(KMnO4_volume_used, Na2C2O4_volume_used, second_KMnO4_volume_used):
            result = consumedOxigen (sample_volume, KMnO4_molarity, KMnO4_fc, item1, Na2C2O4_molarity, Na2C2O4_fc, item2, second_KMnO4_molarity, second_KMnO4_fc, item3)
            data_set.append(result)

        ## Executing Dixon test ##
        print('Statistical analysis - Dixon test')
        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest (data_set, confidence_interval)

        ## Executing Students T test ##
        print('Statistical analysis - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)