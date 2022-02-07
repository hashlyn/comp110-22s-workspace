"""EX03 - Wordle - A cute little guessing game!"""

__author__ = "730412456"


def contains_char(any_length: str, single_character: str) -> bool:
    """Returns bool after single_character is searched for in any_length."""
    assert len(single_character) == 1
    i: int = 0 
    while i < len(any_length):  
        if any_length[i] == single_character[0]: 
            return True
        else: 
            i += 1
    return False


def emojified(guess: str, secret_word: str) -> str: 
    """Returns a corresponding string of emojies."""
    assert len(guess) == len(secret_word)
    idx: int = 0
    GREEN_BOX: str = "\U0001F7E9"
    WHITE_BOX: str = "\U00002B1C"
    YELLOW_BOX: str = "\U0001F7E8"
    resulting_emoji: str = ""
    while idx < len(secret_word):
        if guess[idx] == secret_word[idx]:
            resulting_emoji = resulting_emoji + GREEN_BOX
            idx += 1
        elif contains_char(secret_word, guess[idx]) is True:
            resulting_emoji = resulting_emoji + YELLOW_BOX
            idx += 1
        else: 
            resulting_emoji = resulting_emoji + WHITE_BOX
            idx += 1
    return resulting_emoji 


def input_guess(expected_length_of_guess: int) -> str: 
    """Returns guess once it matches length of secret word."""
    guess: str = input(f"Enter a {expected_length_of_guess} character word: ")
    while len(guess) != expected_length_of_guess: 
        guess = input(f"That wasn't {expected_length_of_guess} chars! Try again: ")
    return guess 


def main() -> None: 
    """The entrypoint of the program and the main game loop."""
    secret_word: str = "codes"
    turns: int = 1
    won: bool = False
    while turns <= 6 and not won: 
        print(f"=== Turn {turns}/6 ===") 
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word: 
            won = True
            print(f"You won in {turns}/6 turns!")
        else: 
            turns += 1
        if turns == 7: 
            print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
