# write your code here
import sys
import math
import re
var = {}
while True:
    input_user = input()
    if input_user == "/exit":
        print("Bye!")
        break
    elif input_user == "/help":
        print("The program calculates addition and subtraction of numbers with using variables")
    elif len(input_user) == 0:
        pass
    elif input_user[0] == "/":
        print("Unknown command")
    else:
        input_user = input_user.replace(" ", "")
        if "=" in input_user:
            p = input_user.split("=")
            if len(p) > 2:
                print("Invalid assignment")
            if not p[0].isalpha():
                print("Invalid identifier")
            else:
                var.fromkeys(p[0])
                if not p[1].isdigit():
                    if not p[1].isalpha():
                        print("Invalid assignment")
                    else:
                        if p[1] not in var.keys():
                            print("Unknown variable")
                        else:
                            var[p[0]] = int(var[p[1]])
                else:
                    var[p[0]] = int(p[1])
        else:
            if ("+" in input_user) or ("-" in input_user) or ("*" in input_user) or ("/" in input_user):
                try:
                    if "//" in input_user:
                        print("Invalid expression")
                    else:
                        print(int(eval(input_user, var)))
                except (SyntaxError, NameError):
                    print("Invalid expression")
            else:
                if not input_user.isalpha():
                    print("Invalid identifier")
                else:
                    if input_user not in var.keys():
                        print("Unknown variable")
                    else:
                        print(var[input_user])

