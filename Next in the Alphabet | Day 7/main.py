import string

letters = string.ascii_uppercase # Get all the letters in the english alphabeth

def next_letters(s): # Initialise the function

    out = "" # Save variable out for returning later
    for i in s: # Loop over the input
        if i == "Z": # Check if the letter is a 'Z' then output 'AA'
            out += "AA" # Add that to the output
        else: # If it is not a 'Z'
            out += letters[letters.index(i) + 1] # Add the correct letter to the output

    return out # Return the output

print(next_letters("ABC"))

