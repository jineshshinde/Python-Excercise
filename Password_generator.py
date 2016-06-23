Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase 
letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time 
the user asks for a new password.

#Solutin 1
#User will enter the password length

import random
import string
def password(size):
	pw_str = ''.join(random.choice(char) for x in range(size))
	return pw_str
  
char = string.ascii_letters + string.digits + string.punctuation
  
def main():
	n = input('How many characters in your password? : ')
	pwd = password(n)
	print pwd
  
main()

#Solution 2
#Generate a password of length between 8 to 12

import random
import string

char = string.ascii_letters + string.digits + string.punctuation

def passwordGenerator():
	return "".join([string.printable[random.randint(0,len(char))] for i in range(random.randint(8,12))])

print passwordGenerator()
