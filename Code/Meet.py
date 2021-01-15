from Essentials import getPercentage

def fatPercentage (tactobutirometer_reading, sample_weight):
    """
    Determination of the fat content by the Gerber tactobutirometer
    This function returns the percentage of lipids
    """
    lipids_percentage = (tactobutirometer_reading * 11.3) / sample_weight # 11.3 is a constant
    return lipids_percentage



