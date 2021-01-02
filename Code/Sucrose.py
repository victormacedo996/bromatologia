from Essencials import getPercentage
def sucroseByPolarimetry (alfa, volume, tube_length, solution_concentration):
    """
    Function to calculate the % of sucrose in the analysed sucrose via polarimetry
    """
    sample_sucrose_mass = (alfa * volume) / (66.5 * tube_length) ## 66.5 is a constant
    expected_sucrose_grams = (solution_concentration * volume) / 100
    sucrose_percentage = getPercentage (sample_sucrose_mass, expected_sucrose_grams)
    return sucrose_percentage

def icumsaColour (solution_concentration, absorbance_420nm, optical_length):
    """
    Function to calculate the ICUMSA colour of the sucrose
    """
    ICUMSA_colour = (absorbance_420nm * 1000) / ((solution_concentration / 100) * optical_length)
    return ICUMSA_colour

def sucrosePercentage (fehlings_title, expended_solution, solution_percentage):
    """
    Function to calculate inverted sugar in the expended solution
    """
    inverted_sugar_in_the_expended_solution = getPercentage(fehlings_title , expended_solution)
    percentage_of_inverted_sugar = getPercentage(inverted_sugar_in_the_expended_solution, solution_percentage)
    sucrose_percentage = (342 * percentage_of_inverted_sugar) / 360 ## 342 and 360 are constants
    return sucrose_percentage