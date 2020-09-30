# a method to check if a number is prime
# returns False if number is not prime, returns True if number is prime
# https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
#
# Instead of checking till n, we can check till sqrt(n) because a larger factor of n must be a multiple of smaller factor that has been already checked.
# The algorithm can be improved further by observing that all primes are of the form 6k +- 1, with the exception of 2 and 3.
# This is because all integers can be expressed as (6k + i) for some integer k and for i = ?1, 0, 1, 2, 3, or 4; 2 divides (6k + 0), (6k + 2), (6k + 4); and 3 divides (6k + 3).
# So a more efficient method is to test if n is divisible by 2 or 3, then to check through all the numbers of form 6k +- 1.
def check_prime(number):
    # This is checked so that we can skip middle five numbers in below loop 
    if (number % 2 == 0 or number % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= number) : 
        if (number % i == 0 or number % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

# a method to check if a given number is a palindrome
# Converts number into a string, then uses Python slicing method to reverse
# If reverse_number == number, it is a palindrome, and returns true
def check_palindrome(number):
    reverse_num = int(str(number)[::-1])
    return reverse_num == number

# main method
def main():
    # opens the pi.txt file for reading access into the digits variable
    digits = open("./pi.txt", "r").read()
    
    #sets curr_chunk = -1, so if the output is -1, we know there is an error
    curr_chunk = -1

    # while len(digits) >= 7, go through and use Python slicing to split into 7 digit chunks
    while len(digits) >= 7:
        curr_chunk, digits = int(digits[0:7]), digits[1:]
        # if curr_chunk is both prime and palindrome, break out of while loop
        if check_prime(curr_chunk) and check_palindrome(curr_chunk):
            break

    # print result
    print(f"First 7 digits in Pi that is prime and palindrome: {curr_chunk}")


#################################
# PROGRAM EXECUTION STARTS HERE #
#################################
if __name__ == "__main__":
    main()