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
resulting_emoji: str = " "

while index < len(secret_word): 
    if six_letter_guess[index] == secret_word[index]:
        resulting_emoji = resulting_emoji + GREEN_BOX
    else:
        letter_found_anywhere: bool = False
        alternate_indices: int = 0
        while letter_found_anywhere and alternate_indices < len(secret_word):
            if secret_word[alternate_indices] == six_letter_guess[index]: 
                letter_found_anywhere = not letter_found_anywhere
            else: 
                resulting_emoji = resulting_emoji + YELLOW_BOX
                alternate_indices = alternate_indices + 1
        if not letter_found_anywhere: 
            resulting_emoji = resulting_emoji + WHITE_BOX
    index = index + 1 
print(resulting_emoji)

if six_letter_guess == secret_word:
    print("Woo! You got it.")
else: 
    print("Not quite. Play again soon.")
