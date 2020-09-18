# digits of pi after 3.
pidigits = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337"

# a method to check if a given number is prime
def checkPrime(number):
    # Corner cases 
    if (number <= 1) : 
        return False
    if (number <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (number % 2 == 0 or number % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= number) : 
        if (number % i == 0 or number % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

# a method to check if a given number is a palindrome
def checkPalindrome(number):
    print(number)

# takes a string of numbers (pi digits), splits them into chunks of 7, then converts the list of strings and converts it to a list of strings
def chunksOf7(number):
    chunksStrings = [number[i:i+7] for i in range(0, len(number), 1)]
    chunksInt = [int(i) for i in chunksStrings]
    return chunksInt


chunks = chunksOf7(pidigits)
for chunk in chunks:
    print(checkPrime(chunk))
