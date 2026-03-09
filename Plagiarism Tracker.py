from difflib import SequenceMatcher

text1 = input("Enter first text: ")
text2 = input("Enter second text: ")

similarity = SequenceMatcher(None, text1, text2).ratio()

print("Similarity:", similarity * 100, "%")
