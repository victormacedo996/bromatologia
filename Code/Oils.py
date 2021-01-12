def acidityIndex (sample_weight, NaOH_molarity, NaOH_fc, NaOH_volume_spent):
    """
    Function to calculate the acidity index in mg of KOH in 1g of sample
    Function usage: x, y = acidityIndex(4.98, 0.01, 1.09987, 3.9)
    x (grams of acid in 100g of sample) = 0.2428990012048192
    y (acidity index grams of KOH in 1g) = 0.48235262650602395
    """
    acid_mols = NaOH_molarity * NaOH_fc * NaOH_volume_spent
    acid_mass = acid_mols * 282 # 282 is the molecular weight of oleic acid
    grams_of_acid_in_100g = (acid_mass * 100 / sample_weight)
    mg_of_acid_in_100g = grams_of_acid_in_100g / 1000
    KOH_mass = acid_mols * 56 # 56 is the molecular weight of KOH
    acidity_index = KOH_mass / sample_weight
    return mg_of_acid_in_100g, acidity_index

def saponificationIndex (sample_weight, HCl_molarity, HCl_fc, HCl_spent, blank_volume):
    """
    Function to calculate the saponification index in mg of KOH per grams
    """
    V_HCl = blank_volume - HCl_spent
    mols_KOH = HCl_molarity * HCl_fc * V_HCl
    KOH_mass = mols_KOH * 56 # 56 is the molecular weight of the KOH
    saponification_index = KOH_mass / sample_weight
    return saponification_index

def iodineIndex (Na2S2O3_molarity, Na2S2O3_fc, Na2S2O3_volume_spent, blank_volume, sample_weight):
    """
    Function to calculate the iodine index in grams of iodine per 100g
    """
    V_Na2S2O3 = blank_volume - Na2S2O3_volume_spent
    iodine_mols = (Na2S2O3_molarity * Na2S2O3_fc * V_Na2S2O3) / 2
    iodine_mg = iodine_mols * 254 # 254 is the molecular weight of iodine
    iodine_g = (iodine_mg / sample_weight) / 10
    return iodine_g

def peroxideIndex (Na2S2O3_molarity, Na2S2O3_fc, Na2S2O3_volume_spent, blank_volume, sample_weight):
    """
    Funtion to calculate the peroxide index in meq/Kg
    """
    V_Na2S2O3 = Na2S2O3_volume_spent - blank_volume
    mols_Na2S2O3 = Na2S2O3_molarity * Na2S2O3_fc * V_Na2S2O3
    peroxide_index = (mols_Na2S2O3 * 1000) / sample_weight # Mols of iodine = mols_Na2S2O3 / 2; meq of peroxide = mols of iodine * 2
    return peroxide_index



