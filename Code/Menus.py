def mainMenu ():
    from Essentials import displayOptions, clearScreen
    from time import sleep
    """
    Function to print the main menu of the program
    """
    clearScreen()
    print('Welcome to the FOOD ANALITYCS!')
    print('Foods that can be analysed:')
    options = ['Wheat flour', 'Honey', 'Sucrose', 'Water', 'Oils', 'Check license' ,'Exit']
    displayOptions(options)
    
def wheatFlourMenu ():
    from Statistic import dixonTest, Ttest
    from Essentials import getFloat, getAnswer, getInteger
    from Essentials import getDixonConfidenceInterval, displayOptions, getOneSample, getTwoSamples, clearScreen
    from time import sleep
    """
    Function to print the menu for the menu for the wheat flour analysis
    """
    clearScreen()
    print('Wheat flour selected')
    print('Wich parameter do you want to analyse?')
    options = ['Fixed mineral waste', 'Acidity', 'Protein', 'Back to main menu']
    displayOptions(options)
    select_option = getInteger ('Choose the analysis: ')
    if select_option == False:
        mainMenu()

    ## Condition to calculate fixed mineral waste ##
    elif select_option == 1:
        from Flour import fixedMineralWaste
        from Essentials import getThreeSamples
        clearScreen()
        print('Fixed mineral waste selected')
        print('\n')
        ## Getting constants ## 
        sample_humidity = getFloat ('Enter the sample humidity (ex: 20% = 20): ')

        ## Getting variable ##
        weight_after_calcination, crucible_tare, sample_weight = getThreeSamples('weight_after_calcination', 'crucible_tare', 'sample_weight')

        data_set = []
        for item1, item2, item3 in zip(weight_after_calcination, crucible_tare, sample_weight):
            result = fixedMineralWaste (item2, item3, item1, sample_humidity)
            data_set.append(result)

        clearScreen()
        ## Executing dixon test ##
        print('Statistical analisys - Dixon test')
        print('\n')

        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest(data_set, confidence_interval)
        print('\n')

        ## Executing Students T test ##
        print('Statistical analisys - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)
        input('Press any key to back to main menu')

    ## Condition to calculate acidity ##
    elif select_option == 2:
        from Flour import acidity
        clearScreen()
        print('Acidity selected')
        print('\n')

        ## Getting constants ##
        flour_solution_percentage = getFloat ('Enter the percentage of the flour solution (ex: 10% = 10): ')
        volume_of_flour_solution_used =  getFloat ('Enter the volume of flour solution used: ')
        NaOH_molarity = getFloat ('Enter the NaOH molarity: ')
        NaOH_fc = getFloat('Enter the correction factor of the NaOH: ')
        sample_humidity = ('Enter the sample humidity: ')

        ## Getting variable ##
        volume_of_NaOH_spent = getOneSample ('volume of NaOH spent')

        data_set = []
        for item in volume_of_NaOH_spent:
            result = acidity(flour_solution_percentage, volume_of_flour_solution_used, item, NaOH_molarity, NaOH_fc)
            data_set.append(result)

        clearScreen()
        ## Executing dixon test ##
        print('Statistical analisys - Dixon test')
        print('\n')

        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest(data_set, confidence_interval)
        print('\n')

        ## Executing Students T test ##
        print('Statistical analisys - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)
        input('Press any key to back to main menu')

    elif select_option == 3:
        from Flour import protein
        ## Codition to calculate protein ##
        clearScreen()
        print('Protein selected')
        print('\n')

        ## Getting constants ##
        convertion_factor = getFloat ('Enter the convertion factor of the food source: ')
        sample_humidity = getFloat ('Enter the sample humidity: ') 
        volume_of_HCl_in_erlenmayer = getFloat ('Enter the volume of HCl in the erlenmayer: ')
        HCl_molarity = getFloat ('Enter the HCl molarity: ')
        HCl_fc = getFloat ('Enter the correction factor of the HCl: ')
        NaOH_molarity = getFloat ('Enter the NaOH molarity: ')
        NaOH_fc = getFloat ('Enter the correction factor of the NaOH: ')

        ## Getting variable ##
        volume_of_NaOH_spent, sample_weight = getTwoSamples('Volume of NaOH', 'Sample weight')

        data_set = []
        for item1, item2 in zip(volume_of_NaOH_spent, sample_weight):
            result = protein(convertion_factor, sample_humidity, item2, volume_of_HCl_in_erlenmayer, HCl_molarity, HCl_fc, item1, NaOH_molarity, NaOH_fc)
            data_set.append(result)

        clearScreen()
        ## Executing dixon test ##
        print('Statistical analisys - Dixon test')
        print('\n')

        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest(data_set, confidence_interval)
        print('\n')

        ## Executing Students T test ##
        print('Statistical analisys - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)
        input('Press any key to back to main menu')

    elif select_option < 0 or select_option > 3:
        print('Invalid option')
        sleep(1)
        mainMenu()

def honeyMenu ():
    from Statistic import dixonTest, Ttest
    from Essentials import getFloat, getAnswer, getInteger
    from Essentials import getDixonConfidenceInterval, displayOptions, getOneSample, getTwoSamples, clearScreen
    from time import sleep
    """
    Function to print the menu for the menu for the honey analysis
    """
    clearScreen()
    print('Honey selected')
    print('Wich parameter do you want to analyse?')
    options = ['Inverted sugar', 'Sucrose', 'Acidity', 'Formol index', 'Back to main menu']
    displayOptions(options)
    select_option = getInteger ('Choose the analysis: ')

    if select_option == False:
        mainMenu()

    ## Condition to calculate inverted sugar in honey ##
    elif select_option == 1:
        from Honey import invertedSugar
        clearScreen()
        print('Inverted sugar selected')
        print('\n')

        ## Getting constants ##
        fehlings_title = getFloat ('Enter the fehlings title: ')
        solution_percentage = getFloat ('Enter the solution percentage: ')

        ## Getting variable ##
        expended_solution = getOneSample ('Volume of the expended solution')

        data_set = []
        for item in expended_solution:
            result = invertedSugar (fehlings_title, item, solution_percentage)
            data_set.append(result)

        clearScreen()
        ## Executing dixon test ##
        print('Statistical analisys - Dixon test')
        print('\n')

        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest(data_set, confidence_interval)
        print('\n')

        ## Executing Students T test ##
        print('Statistical analisys - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)
        input('Press any key to back to main menu')

    ## Condition to calculate sucrose in honey ##
    elif select_option == 2:
        from Honey import sucrose
        clearScreen()
        print('Sucrose in honey selected')
        print('\n')

        ## Getting variables ##
        inverted_sugar_pre_hidrolisys, inverted_sugar_post_hidrolisys = getTwoSamples ('amount of inverted sugar pre hidrolisys', 'amount of inverted sugar post hidrolisys')
        data_set = []
        for item1, item2 in zip(inverted_sugar_pre_hidrolisys, inverted_sugar_post_hidrolisys):
            result = sucrose (item1, item2)
            data_set.append(result)

        clearScreen()
        ## Executing dixon test ##
        print('Statistical analisys - Dixon test')
        print('\n')

        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest(data_set, confidence_interval)
        print('\n')

        ## Executing Students T test ##
        print('Statistical analisys - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)
        input('Press any key to back to main menu')

    ## Condition to calculate acidity in Honey ##
    elif select_option == 3:
        from Honey import acidity
        clearScreen()
        print('Acidity in honey selected')
        print('\n')

        ## Getting constants ##
        NaOH_molarity = getFloat ('Enter the NaOH molaroty: ')
        NaOH_fc = getFloat ('Enter the correction factor of the NaOH: ')
        honey_solution_concentration = getFloat ('Enter the honey solution concentration (%p/v): ')
        honey_solution_volume = getFloat ('Enter the honey solution volume: ')

        ## Getting variables ##
        NaOH_volume = getOneSample ('volume of NaOH used')

        data_set = []
        for item in NaOH_volume:
            result = acidity (item, NaOH_molarity, NaOH_fc, honey_solution_concentration, honey_solution_volume)
            data_set.appen(result)

        clearScreen()
        ## Executing dixon test ##
        print('Statistical analisys - Dixon test')
        print('\n')

        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest(data_set, confidence_interval)
        print('\n')

        ## Executing Students T test ##
        print('Statistical analisys - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)
        input('Press any key to back to main menu')

    ## Condition to calculate the formol index ##
    elif select_option == 4:
        from Honey import formolIndex
        clearScreen()
        print('Formol index selected')
        print('\n')

        ## Getting constants ##
        NaOH_molarity = getFloat('Enter the NaOH molarity: ')
        NaOH_fc = getFloat('Enter the correction factor for the NaOH: ')
        grams_of_honey = getFloat('Enter the grams of honey used: ')

        ## Getting variable ##
        NaOH_volume = getOneSample ('volume of NaOH used')

        data_set = []
        for item in NaOH_volume:
            result = formolIndex (item, NaOH_molarity, NaOH_fc, grams_of_honey)
            data_set.append(result)

        clearScreen()
        ## Executing dixon test ##
        print('Statistical analisys - Dixon test')
        print('\n')

        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest(data_set, confidence_interval)
        print('\n')

        ## Executing Students T test ##
        print('Statistical analisys - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)
        input('Press any key to back to main menu')
        
    elif select_option < 0 or select_option > 4:
        print('Invalid option')
        sleep(1)
        mainMenu()

def sucroseMenu ():
    from Statistic import dixonTest, Ttest
    from Essentials import getFloat, getAnswer, getInteger
    from Essentials import getDixonConfidenceInterval, displayOptions, getOneSample, getTwoSamples, clearScreen
    from time import sleep
    """
    Function to print the menu for the menu for the sucrose analysis
    """
    clearScreen()
    print('Sucrose selected')
    print('Wich parameter do you want to analyse?')
    options = ['Sucrose by polarimetry', 'ICUMSA colour', 'Sucrose by Fehlings method', 'Back to main menu']
    displayOptions(options)
    select_option = getInteger ('Choose the analysis: ')
    if select_option == False:
        mainMenu()

    ## Condition to calculate sucrose via polarimetry ##
    elif select_option == 1:
        from Sucrose import sucroseByPolarimetry
        clearScreen()
        print('Sucrose via polarimetry selected')
        ## Getting constants ##
        volume = getFloat('Enter the sample volume: ')
        tube_length = getFloat ('Enter the tube lenght: ')
        solution_concentration = getFloat ('Enter the solution concentration:')

        ## Getting varaibles ##
        alfa = getOneSample ('alfa')
        data_set = []
        for item in data_set:
            result = sucroseByPolarimetry (item, volume, tube_length, solution_concentration)
            data_set.append(result)

        clearScreen()
        ## Executing dixon test ##
        print('Statistical analisys - Dixon test')
        print('\n')

        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest(data_set, confidence_interval)
        print('\n')

        ## Executing Students T test ##
        print('Statistical analisys - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)
        input('Press any key to back to main menu')
        
    elif select_option == 2:
        from Sucrose import icumsaColour
        clearScreen()
        print('ICUMSA colour selected')

        ## Getting constants ##
        solution_concentration = getFloat('Enter the solution concentration: ')
        optical_length = getFloat('Enter the optical lenght: ')

        ## Getting variables ##
        absorbance_420nm = getOneSample ('absorbance in 420nm')

        data_set = []
        for item in absorbance_420nm:
            result = icumsaColour (solution_concentration, item, optical_length)
            data_set.append(result)

        clearScreen()
        ## Executing dixon test ##
        print('Statistical analisys - Dixon test')
        print('\n')

        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest(data_set, confidence_interval)
        print('\n')

        ## Executing Students T test ##
        print('Statistical analisys - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)
        input('Press any key to back to main menu')

    ## Condition to calculate the sucrose by Fehlings methos ##
    elif select_option == 3:
        from Sucrose import sucrosePercentage
        clearScreen()
        print('Sucrose by fehlings method selected')

        ## Getting constants ##
        fehlings_title = getFloat('Enter Fehings title: ')
        solution_percentage = getFloat ('Enter the solution percentage: ')

        ## Getting variables ##
        expended_solution = getOneSample ('volume expent')

        data_set = []
        for item in expended_solution:
            result = sucrosePercentage (fehlings_title, item, solution_percentage)
            data_set.append(result)

        clearScreen()
        ## Executing dixon test ##
        print('Statistical analisys - Dixon test')
        print('\n')

        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest(data_set, confidence_interval)
        print('\n')

        ## Executing Students T test ##
        print('Statistical analisys - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)
        input('Press any key to back to main menu')

    elif select_option < 0 or select_option > 3:
        print('Invalid option')
        sleep(1)
        mainMenu()

def waterMenu ():
    from Statistic import dixonTest, Ttest
    from Essentials import getFloat, getAnswer, getInteger
    from Essentials import getDixonConfidenceInterval, displayOptions, getOneSample, getTwoSamples, clearScreen
    from time import sleep
    """
    Function to print the menu for the menu for the water analysis
    """
    clearScreen()
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
        clearScreen()
        print('Water alcalinity selected')
        print('\n')

        ## Getting constants ##
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
        
        
        clearScreen()
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
        input('Press any key to back to main menu')

    ## Condition to calculate water hardness ##
    elif select_option == 2:
        from Water import waterHardness
        clearScreen()
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
        
        clearScreen()

        print('Statistical analisys - Dixon test')
        confidence_interval = getDixonConfidenceInterval ()
        ## Executing dixon test
        dixon_data_set = dixonTest (data_set, confidence_interval)
        print('\n')

        print('Statistical analisys - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)
        input('Press any key to back to main menu')

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

        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest(data_set, confidence_interval)
        print('\n')

        ## Executing Students T test ##
        print('Statistical analisys - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)
        input('Press any key to back to main menu')

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
        input('Press any key to back to main menu')

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
        clearScreen()
        print('Statistical analysis - Dixon test')
        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest (data_set, confidence_interval)

        ## Executing Students T test ##
        print('Statistical analysis - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)
        input('Press any key to back to main menu')

    ## Condition to calculate the consumed oxigen ##
    elif select_option == 6:
        clearScreen()
        print('Oxigen consumed selected')
        print('\n')
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
        clearScreen()
        print('Statistical analysis - Dixon test')
        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest (data_set, confidence_interval)

        ## Executing Students T test ##
        print('Statistical analysis - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)
        input('Press any key to back to main menu')
    elif select_option < 0 or select_option > 6:
        print('Invalid option')
        sleep(1)
        mainMenu()

def OilsMenu ():
    from Statistic import dixonTest, Ttest
    from Essentials import getFloat, getAnswer, getInteger
    from Essentials import getDixonConfidenceInterval, displayOptions, getOneSample, getTwoSamples, clearScreen
    from time import sleep
    """
    Function to print the oils menu option
    """
    clearScreen()
    print('Fat and oils selected')
    print('Wich parameter do you want to analyse?')
    options = ['Acidity index', 'Saponification index', 'Iodine index', 'Peroxide index',
    'Back to main menu']

    displayOptions(options)
    select_option = getInteger ('Choose the analysis: ')
    if select_option == False:
        mainMenu()
    elif select_option == 1:
        clearScreen()
        print('Acidity selected')
        print('\n')
        from Oils import acidityIndex
        ## Getting constants
        NaOH_molarity = getFloat('Enter the NaOH molarity: ')
        NaOH_fc = getFloat('Enter the correction factor for the NaOH:')
        ## Getting variables
        NaOH_spent, sample_weight = getTwoSamples('volume of NaOH spent', 'mass of the sample')
        data_set = []
        for NaOH, mass in zip(NaOH_spent, sample_weight):
            acidity_index = acidityIndex(mass, NaOH_molarity, NaOH_fc, NaOH)
            data_set.append(acidity_index)

        ## Executing Dixon test ##
        clearScreen()
        print('Statistical analysis - Dixon test')
        confidence_interval = getDixonConfidenceInterval ()
        print('\n')
        print('mg of acid in 100g of sample')
        mg_of_acid = dixonTest (list(item[0] for item in data_set), confidence_interval)
        print('\n')
        print('Acidity index (mg of KOH in 1g of sample)')
        acidity = dixonTest(list(item[1] for item in data_set), confidence_interval)

        ## Executing Students T test ##
        print('\n')
        print('Statistical analysis - Students T test')
        confidence_interval_mg_of_acid = getFloat('Enter the confidence interval for mg of acid in 100g of sample (ex: 95% = 0.95): ')
        comparable_mg_of_acid = getFloat('Enter the comparable for mg of acid in 100g of sample: ')
        print('\n')
        confidence_interval_acidity_index = getFloat('Enter the confidence interval for acidity index (ex: 95% = 0.95): ')
        comparable_acidity_index = getFloat('Enter the comparable for acidity index: ')
        print('\n')
        print('T test for mg of acid in 100g of sample')
        Ttest(mg_of_acid, comparable_mg_of_acid, confidence_interval_mg_of_acid)
        print('\n')
        print('T test for acidity index')
        Ttest(acidity, comparable_acidity_index, confidence_interval_acidity_index)


        input('Press any key to back to main menu')

    elif select_option == 2:
        clearScreen()
        print('Saponification index selected')
        print('\n')
        from Oils import saponificationIndex
        ## Getting constants
        HCl_molarity = getFloat('Enter the HCl molarity: ')
        HCl_fc = getFloat('Enter the correction factor for the HCl: ')
        blank_volume = getFloat('Enter the blank volume: ')
        ## Getting variables
        HCl_spent, sample_weight = getTwoSamples('HCl spent', 'Sample weight')
        data_set = []
        for HCl, mass in zip(HCl_spent, sample_weight):
            saponification_index = saponificationIndex(mass, HCl_molarity, HCl_fc, HCl, blank_volume)
            data_set.append(saponification_index)

        ## Executing Dixon test ##
        clearScreen()
        print('Statistical analysis - Dixon test')
        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest (data_set, confidence_interval)

        ## Executing Students T test ##
        print('Statistical analysis - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)
        input('Press any key to back to main menu')

    elif select_option == 3:
        clearScreen()
        print('Iodine index selected')
        print('\n')
        from Oils import iodineIndex
        ## Getting constants
        Na2S2O3_molarity = getFloat('Enter Na2S2O3 molarity: ')
        Na2S2O3_fc = getFloat('Enter Na2S2O3 correction factor: ')
        blank_volume = getFloat('Enter the blank volume: ')
        ## Getting variables
        sample_weight, Na2S2O3_volume_spent = getTwoSamples('Sample weight', 'Na2S2O3 volume spent')
        data_set = []
        for mass, Na2S2O3 in zip(sample_weight, Na2S2O3_volume_spent):
            iodine_index = iodineIndex (Na2S2O3_molarity, Na2S2O3_fc, Na2S2O3, blank_volume, mass)
            data_set.append(iodine_index)
        
        ## Executing Dixon test ##
        clearScreen()
        print('Statistical analysis - Dixon test')
        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest (data_set, confidence_interval)

        ## Executing Students T test ##
        print('Statistical analysis - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)
        input('Press any key to back to main menu')

    elif select_option == 4:
        clearScreen()
        print('Peroxide index selected')
        print('\n')
        from Oils import peroxideIndex
        ## Geting constants
        Na2S2O3_molarity = getFloat('Enter the Na2S2O3 molarity: ')
        Na2S2O3_fc = getFloat('Enter the correction factor for the Na2S2O3: ')
        blank_volume = getFloat('Enter the blank volume: ')
        ## Getting variables
        sample_weight, Na2S2O3_volume_spent = getTwoSamples('Sample weight', 'Na2S2O3 volume spent')
        data_set = []
        for mass, Na2S2O3 in zip(sample_weight, Na2S2O3_volume_spent):
            peroxide_index = peroxideIndex(Na2S2O3_molarity, Na2S2O3_fc, Na2S2O3, blank_volume, mass)
            data_set.append(peroxide_index)

        ## Executing Dixon test ##
        clearScreen()
        print('Statistical analysis - Dixon test')
        confidence_interval = getDixonConfidenceInterval ()
        dixon_data_set = dixonTest (data_set, confidence_interval)

        ## Executing Students T test ##
        print('Statistical analysis - Students T test')
        confidence_interval = getFloat('Enter the confidence interval (ex: 95% = 0.95): ')
        comparable = getFloat('Enter the comparable: ')
        Ttest(dixon_data_set, comparable, confidence_interval)
        input('Press any key to back to main menu')
        
    elif select_option < 0 or select_option > 4:
        print('Invalid option')
        sleep(1)
        mainMenu()

def licenseMenu():
    
    from Essentials import clearScreen
    clearScreen()
    print("""
        Copyright (c) 2020 Victor Macedo

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense and to permit 
    persons to whom the Software is furnished to do so, subject to the following 
    conditions:
    \n
    """)
    input('Press any key to proceed')
    print("""
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    If the software is used in any kind of scientific or academic work it has to be 
    cited properly.

    This program must under no circumstances be sold or marketed. 

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """)
    input('Press any key to back to main menu')
