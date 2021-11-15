# Fibonacci Series
num = int(input("Enter the Range Number: "))
num1 = 0
num2 = 1
for n in range(0, num):
  if(n <= 1):
    next = n
  else:
    next = num1 + num2
    num1 = num2
    num2 = next
  print(next)
