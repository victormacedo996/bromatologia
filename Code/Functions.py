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

def sucrose_polarimetry (alfa, volume, tube_length, solution_concentration):
    """
    Function to calculate the % of sucrose in the analysed sucrose via polarimetry
    """
    sample_sucrose_mass = (alfa * volume) / (66.5 * tube_length) ## 66.5 is a constant
    expected_sucrose_grams = (solution_concentration * volume) / 100
    %_sucrose = (sample_sucrose_mass * 100) / expected_sucrose_grams
    return %_sucrose












