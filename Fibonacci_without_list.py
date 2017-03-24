# Fibonacci series without using list.

a = 1
b = 1

print a
for i in range(5):
  print b
  c = a + b
  a = b
  b = c

##Output will be
1
1
2
3
5
8
