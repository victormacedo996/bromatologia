def getFloat (Float):
    """
    Float input verification
    usage: x = getFloat ('mensage to display ')
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
    usage: x = getInterger ('mensage to display ')
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
    usage: x = getPercentage(5, 10)
    x = 50
    """
    percentage = (times100 * 100) / divisor
    return percentage

def getAnswer (answer):
    """
    Function to get YES or NO answer from the user
    usage: x = getAnswer('mensage to display ')
    """
    while True:
        user_input = input(answer).lower()
        if user_input != "y" and user_input != "n":
            print('Use Y for yes and N for no')
        else:
            return user_input

def getOption (list_of_options):
    """
    Function to verify the option input of the user to navigate throught the menus
    usage: x = getOption (list)
    user's input must be in range of list
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

def getDixonConfidenceInterval ():
    """
    Usage: getDixonConfidenceInterval()
    """
    print('Dixons confidence intervals:')
    print("""
            1. 90%
            2. 95%
            3. 99%
            """)
    confidence_interval = 0
    while True:
        confidence_interval = getInteger ('Enter the confidence interval: ')
        if confidence_interval < 1 or confidence_interval > 3:
            print('You must enter a valid confidence interval')
        else:
            if confidence_interval == 1:
                confidence_interval = 0.9
                break
            elif confidence_interval == 2:
                confidence_interval = 0.95
                break
            else:
                confidence_interval = 0.99
                break
    return confidence_interval

def displayOptions(option_list):
    """
    Function to print the options for the menus contained in a list
    usage: displayOptions(list)
    """
    for item in option_list:
        if item == 'Exit' or item == 'Back to main menu':
            print(f"  0. {item}")
        else:
            print(f"  {option_list.index(item) + 1}. {item}")

def getOneSample (question_to_ask):
    """
    This function return a lists with the users input
    usage: x  = getOneSamples ('question')
    """
    i = 1 ## Counting variable
    answer = 'y'
    data_set = []
    while True:
    # Loop while to get the variables of the samples

        if i == 1: ## Condition to print the right ordinal number
            r = f"{i}st"
        elif i == 2:
            r = f"{i}nd"
        elif i == 3:
            r = f"{i}rd"
        else:
            r = f"{i}th"

        sample = getFloat (f"{r} {question_to_ask}: ")
        data_set.append(sample)
        answer = getAnswer ('Add another sample? (Y/N): ')
        if len(data_set) < 3 and answer != 'y':
            answer = 'y'
            print('You must enter at least 3 samples')
        elif answer != 'y':
            break
        else:
            if len(data_set) == 10:
                break
            else:
                pass
        i += 1
    return data_set

def getTwoSamples (first_question_to_ask, second_question_to_ask):
    """
    This function return two lists with the users input for each question
    usage: x, y = getTwoSamples = ('question1', 'question2')
    """
    i = 1 ## Counting variable
    answer = 'y'
    question1_set = []
    question2_set = []
    while True:
    # Loop while to get the variables of the samples
    
        if i == 1: ## Condition to print the right ordinal number
            r = f"{i}st"
        elif i == 2:
            r = f"{i}nd"
        elif i == 3:
            r = f"{i}rd"
        else:
            r = f"{i}th"

        question1 = getFloat(f"Enter {r} volume of {first_question_to_ask}: ")
        question2 = getFloat(f"Enter {r} volume of {second_question_to_ask}: ")
        question1_set.append(question1)
        question2_set.append(question2)
        answer = getAnswer ('Add another sample? (Y/N): ')

        if len(question1_set) < 3 and answer != 'y':
            answer = 'y'
            print('You must enter at least 3 samples')
        elif answer != 'y':
            break
        else:
            if len(question1_set) == 10:
                break
            else:
                pass
        i += 1
    return question1_set, question2_set