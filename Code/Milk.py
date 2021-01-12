from Essencials import getPercentage

def lactose (fehlings_title, milk_solution_percentage, solution_spent):
    """
    This function return the percentage of lactose
    """
    inverted_sugar_in_the_expended_solution = getPercentage(fehlings_title, solution_spent)
    percentage_of_inverted_sugar = getPercentage(inverted_sugar_in_the_expended_solution, milk_solution_percentage)
    lactose_percentage =  percentage_of_inverted_sugar * 1.39 # 1.39 is a constant
    return lactose_percentage

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


def fatpercentage (tactobutirometer_reading, sample_weight):
    """
    Determination of the fat content by the Gerber tactobutirometer
    This function returns the percentage of lipids
    """
    lipids_percentage = (tactobutirometer_reading * 11.3) / sample_weight # 11.3 is a constant
    return lipids_percentage

def totalSolubleSolids (percentage_of_fat, density):
    """
    This function return the total soluble solids using the Fleishmann formula
    """
    total_soluble_solids = (1.2 * percentage_of_fat) + 2.665 * ((100 * density) - 100)
    return total_soluble_solids


def nonFatSolids (percentage_of_total_soluble_solids, fat_percentage):
    """
    This function return the percentage of non fat solids
    """
    percentage_of_non_fat_solids = percentage_of_total_soluble_solids - fat_percentage
    return percentage_of_non_fat_solids

