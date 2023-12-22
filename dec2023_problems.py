""" PROBLEM 1 - Break Palindrome """


def breakPalindrome(palindromeStr):
    # If the length of the palindrome is 1, it's impossible to make a non-palindrome
    if len(palindromeStr) == 1:
        return "IMPOSSIBLE"

    # Convert the string to a list to manipulate it
    palindrome_list = list(palindromeStr)

    # Loop through the first half of the palindrome
    for i in range(len(palindrome_list) // 2):
        # If the character is not 'a', it can be changed to 'a' to make the string
        # lexicographically smaller and not a palindrome
        if palindrome_list[i] != 'a':
            palindrome_list[i] = 'a'
            return ''.join(palindrome_list)

    # If all characters are 'a', change the last character to 'b' to make the string
    # lexicographically larger and not a palindrome
    palindrome_list[-1] = 'b'
    return ''.join(palindrome_list)

# # Example usage:
# palindromeStr = 'aaabaaa'
# print(breakPalindrome(palindromeStr))

palindromeStr = 'mom'
print(breakPalindrome(palindromeStr))