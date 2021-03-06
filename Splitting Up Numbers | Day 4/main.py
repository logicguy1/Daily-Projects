def num_split(num):
    strNum = str(num) # Get the number as a string

    isNeg = True if num < 0 else False # Check if num is negative

    numbers = [] # To keep track of all the numbers that we need to return at last
    indx = 0 # The amount of zeros to add at the end of the current number
    for i in strNum[::-1]: # Loop over the number backwords
        if i.isnumeric(): # Run the code if i is a number
            number = "" # Create our number here termerealy

            number += "-" if isNeg else "" # Add a - If the number is negative
            number += i # Add i ( The base number )
            number += "0" * indx # Add the zeros after the base number

            indx += 1 # Add an extra zero to the next number

            numbers.append(int(number)) # Add the number to the final list

    return numbers[::-1] # Return the result and flip the list to get it in the right order

print(num_split(-325))

