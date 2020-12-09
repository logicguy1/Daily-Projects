def is_valid_PIN(pin):
	if len(pin) in (4, 6) and pin.isnumeric():
		return True
	else:
		return False
	
print(is_valid_PIN("1943")
