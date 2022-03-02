"""Some utility functions!"""

__author__ = "730412456"


def only_evens(list_of_integers: list[int]) -> list[int]: 
    """Return the even elements within a given list."""
    i: int = 0
    evens: list[int] = list()
    while i < len(list_of_integers): 
        if list_of_integers[i] % 2 == 0:
            evens.append(list_of_integers[i])
            i += 1
        else:
            i += 1
    return evens 


def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]: 
    """Return a subset of a given list."""
    sublist: list[int] = list()
    if start_index < 0: 
        start_index = 0 
    if start_index == len(a_list): 
        return sublist
    if end_index > len(a_list): 
        end_index = len(a_list)
    if len(a_list) == 0 or start_index > len(a_list) or end_index <= 0: 
        return sublist 
    sublist.append(a_list[start_index])
    while start_index < (end_index - 1): 
        start_index = start_index + 1
        sublist.append(a_list[start_index])
    return sublist


def concat(first_list: list[int], second_list: list[int]) -> list[int]: 
    """Return a list that is the concatenated values of the first and second lists."""
    concat_list: list[int] = list()
    counter: int = 0 
    while counter < len(first_list):
        concat_list.append(first_list[counter])
        counter += 1
    counter = 0 
    while counter < len(second_list): 
        concat_list.append(second_list[counter])
        counter += 1
    return concat_list 
    