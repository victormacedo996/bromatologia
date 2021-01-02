def getFloat (Float):
    """
    Float input verification
    """
    while True:
        try:
            user_input = float(input(Float))
            return user_input
        except ValueError:
            print('Use only numbers and separete decimals with point')

def getInteger (Interger):
    """
    Integer input verification
    """
    while True:
        try:
            user_input = int(input(Interger))
            return user_input
        except ValueError:
            print('you must enter e interger')

def getPercentage (times100, divisor):
    """
    Function to get percentages
    """
    percentage = (times100 * 100) / divisor
    return percentage
