from Essencials import getPercentage

def alcalinity (H2SO4_concentration, H2SO4_fc, volume_spent_with_phenolphthalein, volume_spent_with_methyl_orange, water_volume_used):
    """
    Function to calculate the water alcalinity in mg of CaCO3/L. The result is a list with
    the alcalinity of carbonate in the 0 position and bicarbonate in the 1 position
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
    

    if hydroxide != 0:
        print('Water must not be consumed')

    else:
        water_alcalinity = []
        carbonate_alcalinity = ((H2SO4_concentration * H2SO4_fc * carbonate * 100) * 1000) / water_volume_used
        bicarbonate_alcalinity = ((H2SO4_concentration * H2SO4_fc * bicarbonate * 100) * 1000) / water_volume_used
        water_alcalinity.append(carbonate_alcalinity, bicarbonate_alcalinity)

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

def consumedOxigen ()

    