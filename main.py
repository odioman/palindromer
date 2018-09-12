word = input('Enter a word to see if a palindrome')

if word[::-1] == word:
    print("Yay! A palindrome")

else:
    print("No palindrome here")