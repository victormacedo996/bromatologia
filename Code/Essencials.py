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

def getAnswer (answer):
    """
    Function to get YES or NO answer from the user
    """
    while True:
        user_input = input(answer).lower()
        if user_input != "y" and user_input != "n":
            print('Use Y for yes and N for no')
        else:
            return user_input

def getSample ():
    """
    Function to get the users input and create a data set
    """
    data_set = []
    while True:
        sample = getFloat ('Enter sample: ')
        data_set.append(sample)
        answer = getAnswer ('Do you want to add another sample? (Y/N): ')
        if answer == 'y':
            pass
        else:
            break
        if len(data) == 10:
            break

    return data_set

def getOption (list_of_options):
    """
    Function to verify the option input of the user to navigate throught the menus
    """
    while True:
        try:
            user_input = getInteger('Enter option: ')
            if user_input == 0:
                return False
            elif user_input > len(list_of_options) or user_input < len(list_of_options):
                print('Invalid option')
            else:
                return user_input
        except ValueError:
            print('You must enter a integer number')
