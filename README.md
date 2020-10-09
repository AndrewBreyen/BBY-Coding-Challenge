#How It Works
Code starts executing at the main method. 

Opens the 100,000 digits of pi from the pi.txt as a file with read-only access. Saves to pifile variable.
reads pifile into digits. 

Curr_chunk is set to -1 so that if -1 is printed, there is an error. 

While len(digits) >=7, use Python slicing to split into 7 digit chunks. 
For every 7 digit chunk, check if its both a prime and palindrome. If yes, break out of loop. Curr_chunk will not be reassigned to anything, since it broke out of loop, so curr_chunk is the answer. 


Check_prime() method:
I first had it checking prime using something like this method: 
if num > 1: 
      
   # Iterate from 2 to n / 2  
   for i in range(2, num): 
         
       # If num is divisible by any number between  
       # 2 and n / 2, it is not prime  
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
   else: 
       print(num, "is a prime number") 
  
else: 
   print(num, "is not a prime number") 

(https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/)

However, after researching ways to optimize, I found this optimized method. 

Description of optimized method:

Instead of checking till n, we can check till √n because a larger factor of n must be a multiple of smaller factor that has been already checked.

The algorithm can be improved further by observing that all primes are of the form 6k ± 1, with the exception of 2 and 3. This is because all integers can be expressed as (6k + i) for some integer k and for i = ?1, 0, 1, 2, 3, or 4; 2 divides (6k + 0), (6k + 2), (6k + 4); and 3 divides (6k + 3). So a more efficient method is to test if n is divisible by 2 or 3, then to check through all the numbers of form 6k ± 1.

Check_palindrome() method: 
Check palindrome first converts the parameter number into a string, and uses python slicing of strings to start from the back and go 1 character back every time to set reverse_num to the reverse of number. Then, a Boolean is returned, TRUE if reverse_num = number, FALSE if not. 

