import datetime

def check_prime(number):
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5

    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i = i + 6

    return True


def check_palindrome(number):
    reverse_num = int(str(number)[::-1])

    return reverse_num == number


def main():
    digits = open("./pi.txt", "r").read()
    curr_chunk = -1

    while len(digits) >= 7:
        curr_chunk, digits = int(digits[0:7]), digits[1:]
        if check_prime(curr_chunk) and check_palindrome(curr_chunk):
            break

    print(f"First 7 digits in PI that is primary and a palindrome: {curr_chunk}")


#################################
# PROGRAM EXECUTION STARTS HERE #
#################################
if __name__ == "__main__":
    main()

