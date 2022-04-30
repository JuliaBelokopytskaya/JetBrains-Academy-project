import copy
from functools import reduce

#problem 1
'''Ввести три числа m, n, p. Подсчитать  количество отрицательных чисел'''
k=[]
for i in range(3):
    k.append(int(input( "введите число\n")))
count_negativ=len(list(filter(lambda x: x<0,k )))
print (f"{count_negativ} отрицательных чисел")

#problem 3
'''Даны три числа a, b и c. Найти среднее геометрическое этих чисел, если все они отличны от нуля, и среднее арифметическое в противном случае.'''
def geometric_mean(a,b,c):
    y=(a*b*c)/3
    print ('среднее геометрическое-' +str(y))
def arithmetic_mean(a,b,c):
    y=(a+b+c)/3
    print ('среднее арифметическое-'+str(y))
a=int(input("введите число\n"))
b=int(input("введите число\n"))
c=int(input("введите число\n"))
if a==0 or b==0 or c==0:
    arithmetic_mean(a,b,c)
else:
    geometric_mean(a,b,c)

#problems of digits numbers
def digits_numbers(a):
    if a//10==0:
        x.append(a)
        return x
    else:
        x.append(a%10)
        digits_numbers(a//10)
        return x
'''Дано натуральное трехзначное число n. Верно ли, что среди его цифр есть 0 или 9?'''
n=int(input("введите трехзначное число\n"))
x=[]
y=digits_numbers(n)
if y[0]==0 or y[1]==0 or y[2]==0 or y[0]==9 or y[1]==9 or y[3]==9:
    print('yes')
else:
    print('no')
'''Дано натуральное четырехзначное число n. Верно ли, что все его цифры различны?'''
n=int(input("введите четырехзначное число\n"))
y=digits_numbers(n)
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

#problem 1.1, 1.6 subsets
'''Найти подмножество данного множества чисел такое, что сумма его элементов равна заданному числу. '''
def fun_subsets(array):
    subsets = [[]]
    for n in array:
        prev = copy.deepcopy(subsets)
        [k.append(n) for k in subsets]
        subsets.extend(prev)
    prev.clear()
    return subsets
s=int(input("введите сумму\n"))
array=[]
def input_data():
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
    return array
array=input_data()
sub=fun_subsets(array)
for i in range(len(sub)):
    if sum(sub[i])==s:
        print(sub[i])
        break
    elif i==len( sub):
        print("нет такого подмножества")
'''По целому n и n положительным целым числам определите, можно ли из них образовать подмножество, сумма элементов которого делится на n без остатка. Если можно, то найти любое из таких подмножеств.'''
array.clear()
array=input_data()
subset=fun_subsets(array)
for i in range(len(subset)):
    if sum(subset[i])%len(array)==0:
        print(subset[i])
        break
    elif i==len( subset):
        print("нет такого подмножества")

#problems lists
def input_data():
    array=[]
    for i in range(int(input("введите размер списка\n"))):
        array.append(int(input("введите число\n")))
    return array
def fun_min(arr):
    min=arr[0]
    ind=0
    for i in range(1,len(arr)):
        if min>arr[i]:
            min=arr[i]
            ind=i
    return [min,ind]
def fun_max(arr):
    max=arr[0]
    ind=0
    for i in range(1,len(arr)):
        if max<arr[i]:
            max=arr[i]
            ind=i
    return [max,ind]
'''Введите одномерный целочисленный список. Найдите наибольший нечетный элемент. 
Найдите минимальный по модулю элемент списка. '''
array=input_data()
array1=list(filter(lambda x: x%2==1, array))
max_odd=fun_max(array1)
print(f"наибольший нечетный элемент {max_odd[0]}")
array2=list(map(lambda x: abs(x),array))
min_abs=fun_min(array2)
print(f"минимальный по модулю элемент {array[min_abs[1]]}")
'''Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент. 
Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные'''
array.clear()
array1.clear()
array=input_data()
array1=list(filter(lambda x: x%2==0, array))
if len(array1)==0:
    print(array[0])
else:
    min=fun_min(array1)
    print(f"наименьший четный элемент списка {min[0]}")
print(sorted(array, key=abs))
'''Найдите сумму номеров минимального и максимального элементов.'''
array.clear()
array=input_data()
max=fun_max(array)
min=fun_min(array)
print(f"сумма номеров минимального и максимального элементов {max[1]+min[1]}")
'''Найдите произведение элементов списка с нечетными номерами. 
Найдите наибольший элемент списка, затем удалите его и выведите новый список.'''
array.clear()
array1.clear()
array=input_data()
for i in range(len(array)):
    if i%2==1:
        array1.append(array[i])
mult=reduce(lambda x,y: x*y,array1)
print (f"{mult} - произведение элементов списка с нечетными номерами")
max=fun_max(array)
for i in range(len(array)):
    while max in array:
        array.remove(max)
print(array)