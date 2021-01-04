from Essencials import getPercentage
def fixedMineralWaste (crucible_tare, sample_weight, weight_after_calcination, sample_humidity):
    """
    Function to calculate the fixed mineral waste
    """
    FMW = (crucible_tare + sample_weight) - weight_after_calcination
    FMW_in_100g = getPercentage(FMW, sample_weight)
    FMW_percentage_in_dry_sample = getPercentage(FMW_in_100g, 100 - sample_humidity)
    return FMW_percentage_in_dry_sample

def acidity (flour_solution_percentage, volume_of_flour_solution_used, volume_of_NaOH_spent, NaOH_molarity, NaOH_fc, sample_humidity):
    """
    Function to calculate the flour acidity in KOH/100g
    """
    quantity_of_sample = flour_solution_percentage / volume_of_flour_solution_used
    NaOH_mols_spent = volume_of_NaOH_spent * NaOH_molarity * NaOH_fc
    mass_of_KOH_mg = NaOH_mols_spent * 56 ## 56 is a constant
    KOH_in_100g_of_sample = getPercentage (mass_of_KOH_mg, quantity_of_sample)
    return KOH_in_100g_of_sample


def protein (convertion_factor, sample_humidity, sample_weight, volume_of_HCl_in_erlenmayer, HCl_molarity, HCl_fc, volume_of_NaOH_spent, NaOH_molarity, NaOH_fc):
    """
    Function to calculate protein in dry base using kjedahl method
    """
    number_of_mols_of_HCl = volume_of_HCl_in_erlenmayer * HCl_molarity * HCl_fc
    number_of_mols_of_NaOH = volume_of_NaOH_spent * NaOH_molarity * NaOH_fc
    number_of_mols_of_nitrogen = number_of_mols_of_HCl - number_of_mols_of_NaOH
    protein_mass = number_of_mols_of_nitrogen * 14 * convertion_factor
    percentage_of_protein = getPercentage(protein_mass, sample_weight)/ 1000
    protein_percentage_in_dry_sample = getPercentage(percentage_of_protein, (100 - sample_humidity)
    return protein_percentage_in_dry_sample