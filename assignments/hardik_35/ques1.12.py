def pallin(string):
	length = len(string)
	for i in range(0,length/2):
		if(string[i] != string[length-i-1]):
			return False
	return True

string = raw_input('Enter a string: ')
print(pallin(string)) 