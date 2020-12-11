def uncensor(txt, vowels): # Initialise the function
  out = "" # Out is used to store the final message
  indx = 0 # Index is to keep track of what vowel we are on
  
  for i in txt: # Loop over the message
    if i == "*": # If the letter we are at is a star
      out += vowels[indx] # give out the vowel 
      indx += 1 # Increase index by one to get the next vowel next time
      
    else: # If the letter is a normal letter and not a "*"
      out += i # Just give out the letter

  return out # Return the result

print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
