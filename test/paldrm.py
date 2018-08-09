def isPalindrome(number):
    orgNumber = number
    reverseNumber = 0
    while number > 0:
        remainder = number % 10
        reverseNumber = reverseNumber * 10 + remainder
        number = number / 10

    if reverseNumber == orgNumber:
        return True
    else:
        return False


number = int(input("Enter Number : "))
if isPalindrome(number) is True:
    print("It is Palindrome...")
else:
    print("Not Palindrome...")
