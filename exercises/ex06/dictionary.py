"""Dictionary functions!"""

__author__ = "730412456"


def invert(dictionary: dict[str, str]) -> dict[str, str]: 
    """Inverting a given dictionary."""
    invert_dictionary: dict[str, str] = {}
    for key_dictionary in dictionary:
        if dictionary[key_dictionary] in invert_dictionary:
            raise KeyError("KeyError")
        else: 
            invert_dictionary[dictionary[key_dictionary]] = key_dictionary
    return invert_dictionary


def favorite_colors(personal_favs: dict[str, str]) -> str: 
    """Returns what color appears most frequently."""
    color_list: list[str] = []
    for key in personal_favs: 
        color_list.append(personal_favs[key])
    frequency: dict[str, int] = count(color_list)
    biggest: int = 0 
    popular_color: str = ""
    for key in frequency: 
        if frequency[key] > biggest: 
            biggest = frequency[key]
            popular_color = key
    return popular_color
        
            
def count(input_list: list[str]) -> dict[str, int]: 
    """Counting each item in an input list."""
    count_dictionary: dict[str, int] = {}
    for key in input_list:
        if key in count_dictionary: 
            count_dictionary[key] += 1 
        else: 
            count_dictionary[key] = 1
    return count_dictionary