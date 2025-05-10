# This program finds common letters between two user-provided words.

word1 = input("Enter first word: ").lower()
word2 = input("Enter second word: ").lower()
common_letters = set(word1) & set(word2)
print("Common letters:", common_letters)