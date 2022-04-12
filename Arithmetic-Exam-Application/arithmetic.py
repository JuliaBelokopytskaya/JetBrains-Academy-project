import random
def out_res_expr(s):
	if (s.find('+') != -1):
		p = s.split('+')
		return (int(p[0]) + int(p[1]))
	if (s.find('-') != -1):
		p = s.split('-')
		return (int(p[0]) - int(p[1]))
	if (s.find('*') != -1):
		p = s.split('*')
		return (int(p[0]) * int(p[1]))
def rand_simple():
	a=random.randint(2,9)
	b=random.randint(2,9)
	z=random.choice('+-*')
	s=str(a)+z+str(b)
	print(s)
	return(s)
def inp():
	while True:
		try:
			var = int(input())
			message = "Incorrect format"
			assert (var==1 or var==2), message
			break
		except ValueError:
			print("Incorrect format")
		except AssertionError as err:
			print(err)
	return var
def input_user():
	while True:
		try:
			user = int(input())
			break
		except ValueError:
			print("Incorrect format")
	return user
def exam(var, i):
	if var == 1:
		s = rand_simple()
		user = input_user()
		res = out_res_expr(s)
	else:
		s = random.randint(11, 29)
		print(s)
		user = input_user()
		res = s * s
	if user == res:
		print("Right!")
		i += 1
	else:
		print("Wrong!")
	return i
def write_res(name,i,var,level):
	file=open("results.txt",'a')
	file.write(name+": "+str(i)+"/5 in level "+str(var)+" ("+level+").\n")

print("Which level do you want? Enter a number:")
print("1 - simple operations with numbers 2-9")
print("2 - integral squares of 11-29")
var=inp()
if var==1:
	level="simple operations with numbers 2-9"
else:
	level="integral squares of 11-29"
i=0
for _ in range(5):
	i=exam(var, i)
print(f"Your mark is {i}/5. Would you like to save the result? Enter yes or no.")
ans=input()
if ans.lower() in "yes":
	print("What is your name?")
	name=input()
	write_res(name,i,var,level)
	print('The results are saved in "results.txt"')


