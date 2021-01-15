from Essentials import getPercentage
def invertedSugar (fehlings_title, expended_solution, solution_percentage):
    """
    Function to get the percentage of inverted sugar in honey
    """
    inverted_sugar_in_the_expended_solution = getPercentage(fehlings_title , expended_solution)
    percentage_of_inverted_sugar = getPercentage(inverted_sugar_in_the_expended_solution, solution_percentage)
    return percentage_of_inverted_sugar

def sucrose (inverted_sugar_pre_hidrolisys, inverted_sugar_post_hidrolisys):
    """
    Function to calculate the sucrose percentage in honey
    """
    inverted_sugar_from_sucrose = inverted_sugar_post_hidrolisys - inverted_sugar_pre_hidrolisys
    sucrose = inverted_sugar_from_sucrose * 0.95 ## 0.95 is the convertion factor for inverted sugar to sucrose
    return sucrose

def acidity (NaOH_volume, NaOH_molarity, NaOH_fc, honey_solution_concentration, honey_solution_volume):
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