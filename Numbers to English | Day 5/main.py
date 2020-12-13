englishNumbers = {
    "0" : "zero","1" : "one","2" : "two","3" : "three","4" : "four","5" : "five","6" : "six","7" : "seven","8" : "eight","9" : "nine",
    "11" : "eleven","12" : "twelve","13" : "thirteen","14" : "fourteen","15" : "fifteen","16" : "sixteen","17" : "seventeen","18" : "eighteen","19" : "nineteen",
    "10" : "ten","20" : "twenty","30" : "thirty","40" : "forty","50" : "fifty","60" : "sixty","70" : "seventy","80" : "eighty","90" : "ninety",
    "100" : "hundred"
}

def num_split(num): # Used to split numbers up to their components
    strNum = str(num) # Get the number as a string

    isNeg = True if num < 0 else False # Check if num is negative

    numbers = [] # To keep track of all the numbers that we need to return at last
    indx = 0 # The amount of zeros to add at the end of the current number
    for i in strNum[::-1]: # Loop over the number backwords
        if i.isnumeric(): # Run the code if i is a number
            number = "" # Create our number here termerealy

            number += i # Add i ( The base number )
            number += "0" * indx # Add the zeros after the base number

            indx += 1 # Add an extra zero to the next number

            numbers.append(number) # Add the number to the final list

    return numbers[::-1] # Return the result and flip the list to get it in the right order

def num_to_eng(n):
    numbers = num_split(n) # Split up the numbers so 343 becomes [300, 40, 3]
    number = "" # Use this to store our english number
    for i in numbers: # Loop over the splitted up numbers
        # i = str(i) # Convert i to a string
        if len(i) == 3: # If the number is in hundreds
            number += englishNumbers[i[0]] # Get the first number as a word like 'nine' or 'one'
            number += " " + englishNumbers["100"] # Add the 'hundred'
        elif len(i) == 2: # Check if the number has two digets
            if i == "00": # If then number is equels zero
                pass # Do nothing
            elif str(n)[-2:] in englishNumbers: # Check the last 2 numbers if they are something special in the dict
                number += " " + englishNumbers[str(n)[-2:]] # Write what they ment
                break # Stop the loop to avoid the last number being added
            else:
                number += " " + englishNumbers[i] # Otherwise just do the normal
        elif len(i) == 1: # Check if the number has one diget
            number += " " + englishNumbers[i] # If there is one number left just add it

    return number.strip() # Return the result

print(num_to_eng(154))
