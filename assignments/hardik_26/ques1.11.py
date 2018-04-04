def sum(list_num):
	length = len(list_num)
	sum_num = 0
	for i in list_num:
		sum_num += i
	return sum_num;

def multiply(list_num):
	length = len(list_num)
	prod = 1
	for i in list_num:
		prod *= i
	return prod 

number = input('Enter number of elements: ')
list_num = []
print('Enter elements')
for i in range(0,number):
	ele = input()
	list_num.append(ele)
print(sum(list_num))
print(multiply(list_num))