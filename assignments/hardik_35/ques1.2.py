number = input("enter a number:")
if number <= 0:
	print("enter a number greater than zero")
else:
	while number > 0:
		print(number);
		number -= 1;