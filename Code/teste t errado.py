
from Essencials import getPercentage
def testet (mean, sd, how_many_samples, comparable):
    from math import sqrt
    test = ((comparable - mean) * sqrt(how_many_samples)) / sd
    return test


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


def lactose (fehlings_title, milk_solution_percentage, solution_spent):
    """
    This function return the percentage of lactose
    """
    inverted_sugar_in_the_expended_solution = getPercentage(fehlings_title, solution_spent)
    percentage_of_inverted_sugar = getPercentage(inverted_sugar_in_the_expended_solution, milk_solution_percentage)
    lactose_percentage =  percentage_of_inverted_sugar * 1.39 # 1.39 is a constant
    return lactose_percentage


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

def lactose (fehlings_title, milk_solution_percentage, solution_spent):
    """
    This function return the percentage of lactose
    """
    inverted_sugar = (fehlings_title * 100) / solution_spent
    grams_of_inverted_sugar_in_100ml = (inverted_sugar * 100) / milk_solution_percentage
    percentage_of_lactose = grams_of_inverted_sugar_in_100ml * 1.39
    return grams_of_inverted_sugar_in_100ml

def acidity (NaOH_molarity, NaOH_fc, NaOH_volume_spent, milk_volume):
    """
    This fuction calculates the milk acidity in ºDornic
    Function usage: x, y = acidity (0.1, 1.0233, 9.7, 50)
    x = 17.866818000000002 dornic degrees
    y = 0.17866818 percentage of latic acid (g/100ml)
    """
    mol_lactic_acid = (NaOH_molarity * NaOH_fc * NaOH_volume_spent) / 1000 # mmol to mol convertion
    grams_of_latic_acid = mol_lactic_acid * 90 # 90 is the molecular weight of the lactic acid
    percentage_of_latic_acid = getPercentage(grams_of_latic_acid, milk_volume)
    dornic_degree = ((percentage_of_latic_acid * 10) / 100) * 1000 # Dornic degree is mg/10ml
    return dornic_degree, percentage_of_latic_acid

def Lactosee (ml_titulacao, ml_amostra, ml_amostra_diluida):
    x = (ml_amostra_diluida * 0.068 * 100) / (ml_amostra * ml_titulacao)
    return x

data = []
for i in range(1, 6):
    y = float(input('volume spent: '))
    x = lactose(0.0515, 5, y)
    data.append(x)

dixonTest(data, 0.9)




