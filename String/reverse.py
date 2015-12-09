#-------------------------------------------------------------------------------------------
#Task: "Reverse a String – Enter a string and the program will reverse it and print it out."
#-------------------------------------------------------------------------------------------
def mtd1(string):
	new_string = ""
	for x in range(len(string)-1, -1, -1):
		new_string += string[x]
	return new_string

def mtd2(string):
	return string[::-1]

def mtd3(string):
	new_string = ""
	for x in reversed(string):
		new_string += x
	return new_string	

string = input("Input string to REVERSE: ")
print("Method #1: " + mtd1(string))
print("Method #2: " + mtd2(string))
print("Method #3: " + mtd3(string))