#-------------------------------------------------------------------------------------------
#Task: "Check password for lenght, using of upper and lower cases, numbers"
#-------------------------------------------------------------------------------------------
import re

def password_check(password):
	score = 0
	if len(password) > 6: # checks password length
		score += len(password)
		print("Score from length: " + str(len(password)))
	if not password.isupper() and not password.islower(): # checks for both Up and Low presents in string
		score += 5
		print("Score from upper/lower cases: 5")
	if not password.isalpha(): # check that password is not alphabetical only
		score += 5
		print("Score from not only alphabetical chars use: 5")
	if re.match(r'\W*', password):
		score += 5
		print("Score from special char use: 5")
	return score

print("!!!PASSWORD CHECKER!!!")
password = input("Enter password: ")
print("Your score: " + str(password_check(password)) + " dead raccons")