def length(string):
	len = 0;
	for x in string:
		len += 1
	return len


string = raw_input('Enter a string: ')
print(length(string))