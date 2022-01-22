"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730412456"

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5: 
    print("Error: Word must contain 5 characters")
    exit()
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character")
    exit()
instances: int = 0
print("Searching for " + single_character + " in " + five_character_word)

if single_character[0] == five_character_word[0]:
    instances = instances + 1
    print(single_character + " found at index 0")
if single_character[0] == five_character_word[1]:
    instances = instances + 1
    print(single_character + " found at index 1")
if single_character[0] == five_character_word[2]:
    instances = instances + 1 
    print(single_character + " found at index 2")
if single_character[0] == five_character_word[3]:
    instances = instances + 1
    print(single_character + " found at index 3")
if single_character[0] == five_character_word[4]:
    instances = instances + 1 
    print(single_character + " found at index 4")

if instances > 1: 
    print(str(instances) + " instances of " + single_character + " found in " + five_character_word)
if instances == 1:
    print(str(instances) + " instance of " + single_character + " found in " + five_character_word)
else:
    print("No instances of " + single_character + " found in " + five_character_word)