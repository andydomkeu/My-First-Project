def palindrome(n):
    # Reverse the string and check if they match
    if str(n) == str(n)[::-1]:
        return "It is a palindrome"
    else:
        return "It is not a palindrome"

def prime_number(x):
    if x == 1:
        return "Number has to be greater than 1"
    else:
        # Floor Division
        for i in range(2, (x//2)+1):
            if x % i == 0:
                return "It is not a palindrome"
            else:
                return "It is a palindrome"

print(palindrome("racecar"))
print(palindrome("123321"))
print(palindrome("Sarah"))
print(prime_number(17))
print(prime_number(12))
print(prime_number(1))



