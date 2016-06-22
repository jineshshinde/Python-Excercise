Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random
n = random.randint(1,9)
count = 0
while True:
	inp = raw_input("\nGuess a number between 1 to 9: ")
	if inp == 'exit':
		break
	else:
		inp = int(inp)
		count += 1
	if inp > n:
		print "\nToo high"
	elif inp < n:
		print "\nToo low"
	elif inp == n:
		print "\nYou Got it!!!"
		print "And It takes %s tries!!!"%count
		break
