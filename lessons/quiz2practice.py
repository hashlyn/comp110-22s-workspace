"""Quiz 2 Practice!"""


def vowels_and_threes(given: str) -> str: 
    """Return a string containing letters at an index that is a multiple of three or is a vowel."""
    index: int = 0
    v_and_three: str = ""
    vowel_list: list[str] = ['a', 'e', 'i', 'o', 'u']
    while index < len(given): 
        if index % 3 == 0 and index != 0: 
            v_and_three += given[index]
            index += 1
        if given[index] in vowel_list:
            v_and_three += given[index]
        index += 1 
    return v_and_three
        
