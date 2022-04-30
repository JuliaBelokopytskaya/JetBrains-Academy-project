
#problem 1
'''Скопировать в файл F2 только четные строки из F1. Подсчитать размер файлов F1 и F2 (в байтах).'''
import os
import re
file2=open('f2.txt','w')
file1=open('f1.txt', 'r')
s=file1.readlines()
file1.close()	
for i in range(len(s)):
	if i%2==0:
		file2.write(s[i])
file2.close()
with open('f2.txt','r') as file:
	print(file.read())
print(os.path.getsize("f1.txt"))
print(os.path.getsize("f2.txt"))

#problem2
'''Скопировать в файл F2 только те строки из F1,  которые начинаются с буквы «А». Подсчитать количество слов в F2.'''
file2=open('f2.2.txt','w')
with open('f1.txt', 'r') as file1:
	s=file1.readlines()
c=0
for i in range(len(s)):
	if s[i][0]=='А':
		file2.write(s[i])
		c+=s[i].count(' ')
file2.close()
with open('f2.2.txt','r') as file:
	print(file.read())
print(f'Количество слов: {c}')
		
#problem3
'''Скопировать из файла F1 в файл F2 строки, начиная с К до К+5. Подсчитать количество гласных букв в F2.'''
file2=open('f2.3.txt','w')
with open('f1.txt', 'r') as file1:
	s=file1.readlines()
k=int(input("Input k \n"))
c=0
for i in range(k,k+5):
		file2.write(s[i])
file2.close()
with open('f2.3.txt', 'r') as file1:
	p=file1.readlines()
print(p)
for j in range(len(p)):
	c+=sum(1 for x in p[j] if x in 'уУеЕыЫаАоОэЭяЯиИюЮ')
print(f'Количество гласных {c}')
	
#problem4
'''Скопировать из файла F1 в файл F2 все строки, которые не содержат цифры. Подсчитать количество строк, которые начинаются на букву «А» в файле F2.'''
file2=open('f2.4.txt','w')
with open('f1.txt', 'r') as file1:
	Lines=file1.readlines()
c=0
for i in range(len(Lines)):
	if(len(re.findall(r'\d+', Lines[i])))==0:
		file2.write(Lines[i])
file2.close()
file=open('f2.4.txt','r')
s=file.readlines()		
for i in range(len(s)):
	if s[i][0]=='А':
		c+=1
file.close()
print(f'Количество строк: {c}')

#problem5
'''Скопировать из файла F1 в файл F2 строки, начиная с четвертой по порядку. Подсчитать количество символов в последнем слове F2.'''
file2=open('f2.5.txt','w')
with open('f1.txt', 'r') as file1:
	s=file1.readlines()
for i in range(3, len(s)):
		file2.write(s[i])
file2.close()
p=s[len(s)-1].rsplit()
print(f'количество символов в последнем слове {len(p[len(p)-1])}')

#problem6
'''Скопировать из файла F1 в файл F2 строки, начиная с N до K. Подсчитать количество согласных букв в файле F2.'''
file2=open('f2.6.txt','w')
with open('f1.txt', 'r') as file1:
	s=file1.readlines()
k=int(input("Input k \n"))
n=int(input("Input n \n"))
c=0
for i in range(n,k):
		file2.write(s[i])
file2.close()
with open('f2.6.txt', 'r') as file1:
	p=file1.readlines()
print(p)
for j in range(len(p)):
	c+=sum(1 for x in p[j] if x  not in 'уУеЕыЫаАоОэЭяЯиИюЮ' and x.isalpha() )
print(f'Количество согласных {c}')

#problem7
'''Скопировать из файла F1 в файл F2 все строки, которые содержат только одно слово. Найти самое длинное слово в  файле F2.'''
file2=open('f2.7.txt','w')
with open('f.txt', 'r') as file1:
	s=file1.readlines()
p=[]
for i in range(len(s)):
	p.append(s[i].split())
for j in range(len(p)):
	if len(p[j])==1:
		for x in s[j]:
			if x in ':!?,.':
				d=s[j].replace(x, ' ')
		file2.write(d)
file2.close()
with open('f2.7.txt', 'r') as file:
	g=file.readlines()
max=0
ind=0
for i in range(len(g)):
	if max<len(g[i]):
		max=len(g[i])
		ind=i
print(f'самое длинное слово {g[ind]}')