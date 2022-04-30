#problem 3 
'''Даны три числа a, b и c. Найти среднее геометрическое этих чисел, если все они отличны от нуля, и среднее арифметическое в противном случае.'''
def geometric_mean(a,b,c):
	y=(a*b*c)/3
	return y
def arithmetic_mean(a,b,c):
	y=(a+b+c)/3
	return y
def digits_numbers(a,x=[]):
	if a//10!=0:
		x.append(a % 10)
		a = a // 10
		digits_numbers(a)
	else:
		x.append(a)
	return x
