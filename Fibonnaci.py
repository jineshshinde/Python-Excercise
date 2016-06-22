Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Make sure to ask the user to enter the number of numbers in the sequence to generate.

def main():
	n = input("Enter fibonnaci numbers to generate: ")
	a = [1,1]
	for i in range(n-2):
		a.append(fibonacci(a))
	print a
 
def fibonacci(num):
	return (num[-1] + num [-2])

main()
