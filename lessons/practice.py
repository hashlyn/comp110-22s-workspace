
secret_word: str = "python"
six_letter_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

index: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
resulting_emoji: str = " "

while index < len(secret_word): 
    while six_letter_guess[index] == secret_word[index]:
        resulting_emoji + GREEN_BOX
    resulting_emoji + WHITE_BOX 
    index: int = index + 1 
print(resulting_emoji)