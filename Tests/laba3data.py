from lab3 import *
a=int(input("введите число\n"))
b=int(input("введите число\n"))
c=int(input("введите число\n"))
if a==0 or b==0 or c==0:
	y=arithmetic_mean(a,b,c)
	print(f'среднее арифметическое {y}')
else:
	y=geometric_mean(a,b,c)
	print(f'среднее геометрическое {y}')

#problems of digits numbers
'''Дано натуральное трехзначное число n. Верно ли, что среди его цифр есть 0 или 9?'''
n=int(input("введите трехзначное число\n"))
y=digits_numbers(n)
print(y)
if y[0]==0 or y[1]==0 or y[2]==0 or y[0]==9 or y[1]==9 or y[2]==9:
   print('yes')
else:
   print('no')
'''Дано натуральное четырехзначное число n. Верно ли, что все его цифры различны?'''
n=int(input("введите четырехзначное число\n"))
y=digits_numbers(n)
print(y)
if y[0]!=y[1] or y[0]!=y[2] or y[0]!=y[3] or y[1]!=y[2] or y[1]!=y[3] or y[2]!=y[3]:
   print('yes')
else:
   print('no')
'''Число делится на 3 тогда, когда сумма его цифр делится на 3. Проверить этот признак на примере заданного трехзначного числа. '''
n=int(input("введите трехзначное число\n"))
y=digits_numbers(n)
if ((y[0]+y[1]+y[2])%3)==0:
   print('yes')
else:
   print('no')
'''Есть натуральное двузначное число n. Верно ли, что среди его цифр есть 1 или 9?'''
n=int(input("введите двузначное число\n"))
y=digits_numbers(n)
if y[0]==0 or y[1]==0 or y[0]==9 or y[1]==9:
   print('yes')
else:
   print('no')