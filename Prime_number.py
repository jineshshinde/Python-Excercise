Ask the user for a number and determine whether the number is prime or not. 

def prime(num):
  divisor = []
  if num == 1:
    print "Number is not prime number."
    return
    
  for i in range(2,num):
    if num%i == 0:
      divisor.append(i)
  if divisor:
    print "Number is not prime number."
  else:
    print "Number is prime number."

n = input("Enter the number: ")
prime(n)
