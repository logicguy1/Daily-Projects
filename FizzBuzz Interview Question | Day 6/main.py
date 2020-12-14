def fizz_buzz(num): # Initialise the function
    out = "" # Used to store the output
    if num % 3 == 0: # Check if it is devisabel by 3
        out += "Fizz" # Add Fizz to the output
    if num % 5 == 0: # Check if it is devisabel by 5
        out += "Buzz" # Add buzz to the output
    if out == "": # If neather of the above conditions were met run this
        out += num # Add just the num to the output

    return out # Return out
