from Essencials import getFloat
i = 1 ## Counting variable
answer = 'y' 
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
    phenolphthalein = getFloat(f"Enter {r} volume of phenolphthalein: ")
    i += 1