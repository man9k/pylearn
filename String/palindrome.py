#-------------------------------------------------------------------------------------------
#Task: "Checks if the string entered by the user is a palindrome. 
#		That is that it reads the same forwards as backwards like “racecar”"
#-------------------------------------------------------------------------------------------
from time import sleep
from random import uniform
import sys

def cool_print(string):
	for x in string:
	    print(x, end='')
	    sys.stdout.flush()
	    sleep(uniform(0, 0.3))

def pal_check1(string):
	count = 0
	for i in range(len(string), 0, -1):
		cool_print(string[i-1] + " " + string[-i] + "\n")
		if string[i-1].lower() == string[-i].lower():
			count += 1
	if count == len(string):
		return "ALL YOUR BASES ARE PALINDROME\n"
	else:
		return "IT'S NOT PALINDROME, BRO\n"

string = input("ENTER SOME PALINDROME STRING, BRO: ")
cool_print(pal_check1(string))