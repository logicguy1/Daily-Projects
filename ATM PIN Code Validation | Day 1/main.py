def is_valid_PIN(pin): # Initalise the function
  if len(pin) in (4, 6) and pin.isnumeric(): # Check the lenght of the pin and if it is a number
    return True # Return true / false depending on the if statement
  return False
	
print(is_valid_PIN("1943") # Run the function
