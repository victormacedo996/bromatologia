from Essentials import getPercentage

def alcalinity (H2SO4_concentration, H2SO4_fc, volume_spent_with_phenolphthalein, volume_spent_with_methyl_orange, water_volume_used):
    """
    Function to calculate the water alcalinity in mg of CaCO3/L. The result is a list with
    the alcalinity of carbonate in the 0 position, bicarbonate in the 1 position and 
    hydroxide in position 3
    """
    total_spent = volume_spent_with_phenolphthalein + volume_spent_with_methyl_orange
    if volume_spent_with_phenolphthalein == 0:
        hydroxide = 0
        carbonate = 0
        bicarbonate = total_spent

    elif volume_spent_with_phenolphthalein < (total_spent / 2):
        hydroxide = 0
        carbonate = 2 * volume_spent_with_phenolphthalein
        bicarbonate = total_spent - (2 * volume_spent_with_phenolphthalein)

    elif volume_spent_with_phenolphthalein == (total_spent / 2):
        hydroxide = 0
        carbonate = 2 * volume_spent_with_phenolphthalein
        bicarbonate = 0

    elif volume_spent_with_phenolphthalein > (total_spent / 2):
        hydroxide = (2 * volume_spent_with_phenolphthalein) - total_spent
        carbonate = 2 * (total_spent - volume_spent_with_phenolphthalein)
        bicarbonate = 0

    elif volume_spent_with_phenolphthalein == total_spent:
        hydroxide = total_spent
        carbonate = 0
        bicarbonate = 0


    water_alcalinity = []
    carbonate_alcalinity = ((H2SO4_concentration * H2SO4_fc * carbonate * 100) * 1000) / water_volume_used
    bicarbonate_alcalinity = ((H2SO4_concentration * H2SO4_fc * bicarbonate * 100) * 1000) / water_volume_used
    hydroxide_alcalinity = ((H2SO4_concentration * H2SO4_fc * hydroxide * 100) * 1000) / water_volume_used
    water_alcalinity.append(carbonate_alcalinity)
    water_alcalinity.append(bicarbonate_alcalinity)
    water_alcalinity.append(hydroxide_alcalinity)

    return water_alcalinity


def waterHardness (EDTA_standard, quantity_of_CaCO3_neutralized_by_EDTA, EDTA_molatity, EDTA_fc, volume_of_EDTA_used, sample_volume):
    """
    Function to calculate water hardness in mg CaCO3/L of water.
    EDTA_standard = EDTA volume required to complex standard 1g / L CaCO3 solution
    """
    sample_CaCO3 = ((volume_of_EDTA_used * EDTA_fc) * quantity_of_CaCO3_neutralized_by_EDTA) / (EDTA_standard * EDTA_fc)
    CaCO3_per_liter = getPercentage (sample_CaCO3 * 10, sample_volume)
    return CaCO3_per_liter

def totalSolubleSolids (capsule_tare, sample_volume, total_weight_after_dry):
    sample_soluble_solids = total_weight_after_dry - capsule_tare
    soluble_solids_per_liter = getPercentage (sample_soluble_solids * 10, sample_volume)
    return soluble_solids_per_liter

def residualChlorine (Na2S2O3_molarity, Na2S2O3_fc, Na2S2O3_volume_used, sample_volume):
    """
    Function to calculate the residual chlorine in chlorine grams per liter
    """
    Na2S2O3_mols = Na2S2O3_molarity * Na2S2O3_fc * Na2S2O3_volume_used
    chlorine_mols = Na2S2O3_mols / 2
    sample_chlorine_grams = chlorine_mols * 70
    chlorine_grams_per_liter = getPercentage(sample_chlorine_grams * 10, sample_volume)
    return chlorine_grams_per_liter

def chloride (AgNO3_molarity, AgNO3_fc, AgNO3_volume_used, sample_volume):
    """
    Function to calculate the chloride mili grams per liter
    """
    mols_of_AgNO3 = AgNO3_molarity * AgNO3_fc * AgNO3_volume_used
    chloride_mili_grams = mols_of_AgNO3 * 35.5 # 35.5 is a constant
    chloride_mili_grams_per_liter = getPercentage (chloride_mili_grams * 10, sample_volume)
    return chloride_mili_grams_per_liter

def consumedOxigen (sample_volume, KMnO4_molarity, KMnO4_fc, KMnO4_volume_used, Na2C2O4_molarity, Na2C2O4_fc, Na2C2O4_volume_used, second_KMnO4_molarity, second_KMnO4_fc, second_KMnO4_volume_used):
    """
    Function to calculate the O2 consume in water in mg/L
    """
    mols_KMnO4 = KMnO4_molarity * KMnO4_fc * KMnO4_volume_used
    mols_Na2C2O4 = Na2C2O4_molarity * Na2C2O4_fc * Na2C2O4_volume_used
    second_mols_KMnO4 = second_KMnO4_molarity * second_KMnO4_fc * second_KMnO4_volume_used
    mols_of_Na2C2O4_neutralized = (5 * second_mols_KMnO4) / 2
    mols_of_Na2C2O4_avalible = mols_Na2C2O4 - mols_of_Na2C2O4_neutralized
    mols_of_KMnO4_that_reacted_with_avalible_Na2C2O4 = (2 * mols_of_Na2C2O4_avalible) / 5
    mols_KMnO4_avalible = mols_KMnO4 - mols_of_KMnO4_that_reacted_with_avalible_Na2C2O4
    mols_of_O2_producted = (mols_KMnO4_avalible * 5) / 4
    O2_miligrams = mols_of_O2_producted * 32
    O2_mili_grams_per_liter = getPercentage (O2_miligrams * 10, sample_volume)
    return O2_mili_grams_per_liter