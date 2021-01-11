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
    data_set_aux = []
    data_set_aux = data_set
    data_set_aux.sort()

    ## Dixon's test equation
    if (data_set_aux[-1] - data_set_aux[0]) == 0:
        print('Cannot divide by zero, passing trought')
        pass
    else:
        Qmax = abs((data_set_aux[-1] - data_set_aux[-2]) / (data_set_aux[-1] - data_set_aux[0]))
        Qmin = abs((data_set_aux[0] - data_set_aux[1]) / (data_set_aux[-1] - data_set_aux[0]))

        ## Modifying the data
        if Qmax > dixon_table[confidence_interval][len(data_set_aux)] and Qmin > dixon_table[confidence_interval][len(data_set_aux)]:
            ## Print the new data set for the user
            print(f"Reject min and máx value: {data_set_aux[0]} and {data_set_aux[-1]}")
            del data_set_aux[-1]
            del data_set_aux[0]
            print(f"Data set: {data_set_aux}")
        elif Qmax > dixon_table[confidence_interval][len(data_set_aux)]:
            print(f"Reject máx value: {data_set_aux[-1]}")
            del data_set_aux[-1]
            print(f"Data set: {data_set_aux}")
        elif Qmin > dixon_table[confidence_interval][len(data_set_aux)]:
            print(f"Reject min value: {data_set_aux[0]}")
            del data_set[0]
            print(f"Data set: {data_set_aux}")

    print('\n')
    
    from statistics import mean, stdev
    mean = mean(data_set_aux)
    standard_derivation = stdev(data_set_aux)

    print(f"Mean: {mean}")
    print(f"Standard derivation +/- {standard_derivation}")
    
    
    return data_set_aux

def Ttest (data_set, comparable, confidence_interval):
    """
    Function to calculate the p-value of the students t test for one sample using
    scipy library
    """
    from scipy import stats
    t_stat, p_value = stats.ttest_1samp(data_set, comparable, axis = 0)
    print(f"P-Value: {p_value}  T-Statistic: {t_stat}")
    if p_value < (1 - confidence_interval):
        print('Reject H0')
    else:
        print('Do not reject H0')