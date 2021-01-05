from Essencials import getFloat, getAnswer

def getTwoSamples (first_question_to_ask, second_question_to_ask):
    i = 1 ## Counting variable
    answer = 'y'
    volume_spent_with_phenolphthalein = []
    volume_spent_with_methyl_orange = []
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

        phenolphthalein = getFloat(f"Enter {r} volume of {first_question_to_ask}: ")
        methyl_orange = getFloat(f"Enter {r} volume of {second_question_to_ask}: ")
        volume_spent_with_phenolphthalein.append(phenolphthalein)
        volume_spent_with_methyl_orange.append(methyl_orange)
        answer = getAnswer ('Add another sample? (Y/N): ')

        if len(volume_spent_with_phenolphthalein) < 3 and answer != 'y':
            answer = 'y'
            print('You must enter at least 3 samples')
        elif answer != 'y':
            break
        else:
            if len(volume_spent_with_phenolphthalein) == 10:
                break
            else:
                pass
        i += 1
    return volume_spent_with_phenolphthalein, volume_spent_with_methyl_orange

phenol, metil = getTwoSamples ('phenolphtalein', 'metil orange')

print(phenol)
print(metil)