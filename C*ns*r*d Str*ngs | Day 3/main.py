def uncensor(txt, vowels):
  txtPack = txt.split("*")
  
  out = ""
  indx = 0
  for i in txtPack:
    out += f"{i}{vowels[indx]}"
    indx += 1
    
  return out
