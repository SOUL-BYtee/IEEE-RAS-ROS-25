word = input("Enter a word: ").lower()
if word == word[::-1]:
    print(f"The word '{word}' is a palindrome.")
else:
    print(f"The word '{word}' is not a palindrome.")