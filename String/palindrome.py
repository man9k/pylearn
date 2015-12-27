#-------------------------------------------------------------------------------------------
#Task: "Checks if the string entered by the user is a palindrome. 
#		That is that it reads the same forwards as backwards like “racecar”"
#-------------------------------------------------------------------------------------------
from time import sleep
from random import uniform
import sys

#just cool output
def cool_print(string):
	for x in string:
	    print(x, end='')
	    sys.stdout.flush()
	    sleep(uniform(0, 0.25))

def result(value):
	if value:
		cool_print("ALL YOUR BASES ARE PALINDROME\n")
	else:
		cool_print("IT'S NOT PALINDROME, BRO\n")

#1-st method
def pal_check1(string):
	cool_print("INIT METHOD #1\n")
	count = 0
	for i in range(len(string), 0, -1):
		cool_print(string[i-1] + " " + string[-i])
		if string[i-1].lower() == string[-i].lower():
			count += 1
			cool_print(" +")
		cool_print("\n")
	if count == len(string):
		return True
	else:
		return False

#2-nd simplier method
def pal_check2(string):
	cool_print("INIT METHOD #2\n")
	cool_print(string + "   " + string[::-1]+"\n")
	return string.lower() == string[::-1].lower()

string = input("ENTER SOME PALINDROME STRING, BRO: ")

result(pal_check1(string))
result(pal_check2(string))

#"ALL YOUR BASES ARE PALINDROME\n"
#"IT'S NOT PALINDROME, BRO\n"