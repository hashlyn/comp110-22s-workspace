"""EX02 - One Shot Wordle - An even cuter step towards Wordle."""

__author__ = "730412456"

secret_word: str = "python"
six_letter_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

while len(six_letter_guess) != len(secret_word):
    six_letter_guess = input(f"That was not {len(secret_word)} letters! Try again: ")

index: int = 0 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
resulting_emoji: str = ""

while index < len(secret_word): 
    if six_letter_guess[index] == secret_word[index]:
        resulting_emoji = resulting_emoji + GREEN_BOX
    else:
        character_anywhere_in_word: bool = False
        alternate_index: int = 0 
        while not character_anywhere_in_word and alternate_index < len(secret_word):
            if secret_word[alternate_index] == six_letter_guess[index]:
                character_anywhere_in_word = True
            else: 
                alternate_index = alternate_index + 1 
        if character_anywhere_in_word: 
            resulting_emoji = resulting_emoji + YELLOW_BOX
        else: 
            resulting_emoji = resulting_emoji + WHITE_BOX 
    index = index + 1 
print(resulting_emoji)

if six_letter_guess == secret_word:
    print("Woo! You got it.")
else: 
    print("Not quite. Play again soon.")
