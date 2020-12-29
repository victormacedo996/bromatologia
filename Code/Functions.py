def getFloat (Float):
    """
    Float input verification
    """
    while True:
        try:
            user_input = float(input(Float))
            return user_input
        except ValueError:
            print('Use only numbers and separete decimals with point')

def getInteger (Interger):
    """
    Integer input verification
    """
    while True:
        try:
            user_input = int(input(Interger))
            return user_input
        except ValueError:
            print('you must enter e interger')

def getPercentage (times100, divisor):
    """
    Function to get percentages
    """
    percentage = (times100 * 100) / divisor
    return percentage

def dixonTest (data_set, confidence_interval):
    """
    Function to execute dixon test and automacally change the samples data
    """
    dixon_table = {0.9: {3: 0.941, 
                    4: 0.765,
                    5: 0.642,
                    6: 0.560,
                    7: 0.507,
                    8: 0.468,
                    9: 0.437,
                    10: 0.412},

                0.95: {3: 0.970, 
                    4: 0.829,
                    5: 0.710,
                    6: 0.625,
                    7: 0.568,
                    8: 0.526,
                    9: 0.493,
                    10: 0.466},

                0.99: {3: 0.994, 
                    4: 0.926,
                    5: 0.821,
                    6: 0.740,
                    7: 0.680,
                    8: 0.634,
                    9: 0.598,
                    10: 0.568}
            
            }
    data_set.sort()

    ## Dixon's test equation
    Qmax = abs((data_set[-1] - data_set[-2]) / (data_set[-1] - data_set[0]))
    Qmin = abs((data_set[0] - data_set[1]) / (data_set[-1] - data_set[0]))

    ## Modifying the data
    if Qmax > dixon_table[confidence_interval][len(data_set)]:
        print('Reject máx value')
        del data_set[-1]
    elif Qmin > dixon_table[confidence_interval][len(data_set)]:
        print('Reject min value')
        del data_set[0]
    else:
        pass
    
    ## Print the new data set for the user
    print("New data set: ", *data_set, sep = ", ")
    
    return data_set

def Ttest (data_set, comparable, confidence_interval):
    """
    Function to calculate the p-value of the students t test for one sample using
    scipy library
    """
    from scipy import stats
    t_stat, p_value = scipy.stats.ttest_1samp(data_set, comparable, axis = 0)
    print(f"P-Value: {p_value}  T-Statistic: {t_stat}")
    if p_value < confidence_interval:
        print('Equal numbers')
    else:
        print('Different numbers')

def sucrosePolarimetry (alfa, volume, tube_length, solution_concentration):
    """
    Function to calculate the % of sucrose in the analysed sucrose via polarimetry
    """
    sample_sucrose_mass = (alfa * volume) / (66.5 * tube_length) ## 66.5 is a constant
    expected_sucrose_grams = (solution_concentration * volume) / 100
    sucrose_percentage = getPercentage (sample_sucrose_mass, expected_sucrose_grams)
    return sucrose_percentage

def icumsaClour (solution_concentration, absorbance_420nm, optical_length):
    """
    Function to calculate the ICUMSA colour of the sucrose
    """
    ICUMSA_colour = (absorbance_420nm * 1000) / ((solution_concentration / 100) * optical_length)
    return ICUMSA_colour

def sucroseInSucrose (fehlings_title, expended_solution, solution_percentage):
    """
    Function to calculate inverted sugar in the expended solution
    """
    inverted_sugar_in_the_expended_solution = getPercentage(fehlings_title , expended_solution)
    percentage_of_inverted_sugar = getPercentage(inverted_sugar_in_the_expended_solution, solution_percentage)
    sucrose_percentage = (342 * percentage_of_inverted_sugar) / 360 ## 342 and 360 are constants
    return sucrose_percentage
    
def InvertedSugarInHoney (fehlings_title, expended_solution, solution_percentage):
    """
    Function to get the percentage of inverted sugar in honey
    """
    inverted_sugar_in_the_expended_solution = getPercentage(fehlings_title , expended_solution)
    percentage_of_inverted_sugar = getPercentage(inverted_sugar_in_the_expended_solution, solution_percentage)
    return percentage_of_inverted_sugar

def sucroseInHoney (inverted_sugar_pre_hidrolisys, inverted_sugar_post_hidrolisys):
    """
    Function to calculate the sucrose percentage in honey
    """
    inverted_sugar_from_sucrose = inverted_sugar_post_hidrolisys - inverted_sugar_pre_hidrolisys
    sucrose = inverted_sugar_from_sucrose * 0.95 ## 0.95 is a constant
    return sucrose

def honeyAcidity (NaOH_volume, NaOH_molarity, NaOH_fc, honey_solution_concentration, honey_solution_volume):
    """
    Function to get acidity in honey - meq/kg
    """
    mili_eq_NaOH = NaOH_volume * NaOH_molarity * NaOH_fc
    grams_of_honey = (honey_solution_concentration * honey_solution_volume) / 100
    acidity = (mili_eq_NaOH * 1000) / grams_of_honey
    return acidity

def formolIndex (NaOH_volume, NaOH_molarity, NaOH_fc, grams_of_honey):
    """
    Function to calculate the formol index in honey
    """
    number_of_NaOH_mols = NaOH_volume * NaOH_molarity * NaOH_fc
    volume = number_of_NaOH_mols / NaOH_molarity
    formol_index = (volume * 1000) / grams_of_honey
    return formol_index



    