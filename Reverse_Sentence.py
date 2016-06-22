Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.

def reverse_sentence(sen):
	a = sen.split(' ')
	return ' '.join(a[::-1])
 
 
n = raw_input("Enter a sentence: ")
rev_sen = reverse_sentence(n)
print rev_sen
