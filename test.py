# Program to check if a number is prime or not

number = 407

# To take input from the user
#number = int(input("Enter a number: "))

# prime numbers are greater than 1
if number > 1:
   # check for factors
   for i in range(2,number):
       if (number % i) == 0:
           print(number,"is not a prime number")
           print(i,"times",number//i,"is",number)
           break
   else:
       print(number,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(number,"is not a prime number")