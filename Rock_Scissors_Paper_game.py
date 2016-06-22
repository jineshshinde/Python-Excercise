Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock


#Solution 1:

while True:
	print "r for Rock \ns for Scissors \np for Paper"
	p1 = raw_input("\nPlayer 1 please enter your sign: ")
	p2 = raw_input("Player 2 please enter your sign: ")
	w = ['r','s','p']
	l = ['s','p','r']
	if p1 not in w or p2 not in w:
		print"You enter the wrong character for sign. Please enter the correct sign."
	elif p2 == l[w.index(p1)]:
		print "\nCongratulation Player 1, you win the game."
 		
	elif p1 == l[w.index(p2)]:
		print "\nCongratulation Player 2, you win the game."
 	
	elif p1 == p2:
		print "Match Tie."
 	
	print "\nDo you want to continue?"
	if raw_input("Enter 'yes' to continue or 'no' to quit: ") == 'yes':
		continue
	else:
		break
	
#Solution 2:

while True:
	print "1 for Rock \n2 for Scissor \n3 for Paper"
	p1 = input("\nPlayer 1 please enter your sign: ")
	p2 = input("Player 2 please enter your sign: ")
	diff = p1-p2
 	
	if diff in [-1, 2]:
		print "\nCongratulation Player 1, you win the game."
	elif diff in [1, -2]:
		print "\nCongratulation Player 2, you win the game."
	elif diff == 0:
		print "\nMatch Tie."
 		
	print "\nDo you want to continue?"
	if raw_input("Enter 'yes' to continue or 'no' to quit: ") == 'yes':
		continue
	else:
		break

