import numpy as np
import numpy.random as rand
import copy
#problem 1.1
'''Удалить в списке все числа, которые повторяются более двух раз.  '''
array=[]
list=[]
try:
	n=int(input("введите размер списка\n"))
except ValueError:
	print("Вы ввели не целое число")
for i in range(n):
	try:
		array.append(int(input("введите число\n")))
	except ValueError:
		print("Вы ввели не число")
for i in range(n):
	if array.count(array[i])>2:
		if array[i] not in list:
			list.append(array[i])
for i in range(len(list)):
	while list[i] in array:
		array.remove(list[i])	
for i in range( len(array)):
			print(array[i])

'''Найти подмножество данного множества чисел такое, что сумма его элементов равна заданному числу. '''
array=[]
try:
	n=int(input("введите размер списка\n"))
	s=int(input("введите сумму\n"))
except ValueError:
	print("Вы ввели не целое число")
for i in range(n):
	try:
		array.append(int(input("введите число\n")))
	except ValueError:
		print("Вы ввели не число")
subsets = [[]]
for n in array:
	prev = copy.deepcopy(subsets)
	[k.append(n) for k in subsets]
	subsets.extend(prev)
for i in range(len(subsets)):
	if sum(subsets[i])==s:
		print(subsets[i])
		break
	elif i==len( subsets):
		print("нет такого подмножества")

#problem 1.2
'''Введите одномерный целочисленный список. Найдите наибольший нечетный элемент. 
Найдите минимальный по модулю элемент списка. '''
try:
	n=int(input("введите размер списка\n"))
except ValueError:
	print("Вы ввели не целое число")
array=[]
array1=[]
for i in range(n):
	try:
		array.append(int(input("введите число\n")))
	except ValueError:
		print("Вы ввели не число")
	if array[i]%2==1:
		array1.append(array[i])
max=array1[0]
for i in range(1,len(array1)):
	if max<array1[i]:
		max=array1[i]
print("max="+str(max))
min=abs(array1[0])
i=0
for i in range(1,n):
	if min>abs(array[i]):
		min=abs(array[i])
		ind=i
min=array[ind]
print("min="+str(min))

#problem 1.3
'''Найдите сумму отрицательных элементов списка.
Найдите сумму элементов списка между двумя первыми нулями. Если двух нулей нет в списке, то выведите ноль.'''
try:
	n=int(input("введите размер списка\n"))
except ValueError:
	print("Вы ввели не целое число")
array=[]
sum=0
sum1=0
for i in range(n):
	try:
		array.append(int(input("введите число\n")))
	except ValueError:
		print("Вы ввели не число")
	if array[i]<0:
		sum+=array[i]
print("sum="+str(sum))
if array.count(0)>2:
	a=array.index(0)
	b=array.index(0,a+1)
	for i in range(a+1,b):
		sum1+=array[i]
	print("sum between zero="+str(sum1))
else:
	print("sum between zero= ноль")

#problem 1.4
'''Найдите произведение элементов списка с нечетными номерами. 
Найдите наибольший элемент списка, затем удалите его и выведите новый список.'''
try:
	n=int(input("введите размер списка\n"))
except ValueError:
	print("Вы ввели не целое число")
array=[]
mult=1
for i in range(n):
	try:
		array.append(int(input("введите число\n")))
	except ValueError:
		print("Вы ввели не число")
	if i%2==1:
		mult*=array[i]
print("multiplication="+str(mult))
max=array[0]
for i in range(n):
	if max<array[i]:
		max=array[i]
for i in range(n):
	while max in array:
		array.remove(max)
for i in range(len(array)):
	print(array[i])

#problem 1.5
'''Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент. 
Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные'''
try:
	n=int(input("введите размер списка\n"))
except ValueError:
	print("Вы ввели не целое число")
array=[]
mult=1
for i in range(n):
	try:
		array.append(int(input("введите число\n")))
	except ValueError:
		print("Вы ввели не число")
min=array[0]
for i in range(n):
	if min>array[i] and array[i]%2==0:
		min=array[i]
print("min="+str(min))
print(sorted(array, key=abs))

#problem 1.6
'''Найдите сумму номеров минимального и максимального элементов.'''
try:
	n=int(input("введите размер списка\n"))
except ValueError:
	print("Вы ввели не целое число")
array=[]
for i in range(n):
	try:
		array.append(int(input("введите число\n")))
	except ValueError:
		print("Вы ввели не число")
min=array[0]
max=array[0]
indmin=0
indmax=0
for i in range(n):
	if min>array[i]:
		min=array[i]
		indmin=i
for i in range(n):
	if max<array[i]:
		max=array[i]
		indmax=i
print(indmin+indmax)

'''По целому n и n положительным целым числам определите, можно ли из них образовать подмножество, сумма элементов которого делится на n без остатка. Если можно, то найти любое из таких подмножеств.'''
array=[]
try:
	n=int(input("введите размер списка\n"))
except ValueError:
	print("Вы ввели не целое число")
for i in range(n):
	try:
		a=(int(input("введите положительное число\n")))
		if a<0:
			print("Вы ввели отрицательное число")
			break
		else:
			array.append(a)
	except ValueError:
		print("Вы ввели не число")
subsets = [[]]
for i in array:
	prev = copy.deepcopy(subsets)
	[k.append(i) for k in subsets]
	subsets.extend(prev)
for i in range(len(subsets)):
	if sum(subsets[i])%n==0:
		print(subsets[i])
		break
	elif i==len( subsets):
		print("нет такого подмножества")

#problem 2.1
'''В матрице найти номер строки, сумма чисел в которой максимальна.'''
try:
	m=int(input("введите количество столбцов массива\n"))
	n=int(input("введите количество строк массива\n"))
except ValueError:
	print("Вы ввели не целое число")
Mas=np.random.randint(0,11,(n,m))
print(Mas)
sum=np.sum(Mas,axis=1)
max=sum[0]
i=0
for x in range (1,n):
	if max<sum[x]:
		max=sum[x]
		i=x
print("индекс max="+str(i+1))

#problem 2.2
'''Дана квадратная матрица. Проверить, является ли она симметричной относительно главной диагонали.'''
try:
	n=int(input("введите размерность матрицы\n"))
except ValueError:
	print("Вы ввели не целое число")
Mas=np.random.randint(0,11,(n,n))
print(Mas)
Mas1=Mas.transpose()
print(Mas1)
if np.array_equal(Mas,Mas1):
	print("симметричная")
else:
	print("не симметричная")

#problem 2.3
'''Даны две квадратных таблицы чисел. Требуется построить третью, каждый элемент которой равен сумме элементов, стоящих на том же месте в 1-й и 2-й таблицах.'''
try:
	n=int(input("введите размерность матрицы\n"))
except ValueError:
	print("Вы ввели не целое число")
Mas=np.random.randint(0,11,(n,n))
print(Mas)
Mas1=np.random.randint(0,11,(n,n))
print(Mas1)
Mas2=Mas+Mas1
print(Mas2)