"""Tests for three utility functions!"""

__author__ = "730412456"


from utils import only_evens, sub, concat


def test_only_evens_empty() -> None: 
    """Tests for an empty list."""
    list_of_integers: list[int] = []
    assert only_evens(list_of_integers) == []


def test_only_evens_many_items() -> None: 
    """Tests for many positive items."""
    list_of_integers: list[int] = [2, 3, 4, 5, 6, 7]
    assert only_evens(list_of_integers) == [2, 4, 6]


def test_only_evens_many_items_again() -> None: 
    """Tests for many negative and positive items."""
    list_of_integers: list[int] = [-2, -1, 0, 1, 2]
    assert only_evens(list_of_integers) == [-2, 0, 2]


def test_sub_invalid_index() -> None:
    """Tests for starting index below 0."""
    a_list: list[int] = [1, 2, 3, 4]
    start_index: int = -1
    end_index: int = 3
    assert sub(a_list, start_index, end_index) == [1, 2, 3]


def test_sub_short_range() -> None: 
    """Tests for a range with one item between."""
    a_list: list[int] = [1, 2, 3, 4]
    start_index: int = 1
    end_index: int = 2
    assert sub(a_list, start_index, end_index) == [2]


def test_sub_long_range() -> None: 
    """Tests for a range with multiple items between."""
    a_list: list[int] = [1, 2, 3, 4]
    start_index: int = 0 
    end_index: int = 4
    assert sub(a_list, start_index, end_index) == [1, 2, 3, 4]


def test_concat_empty_list() -> None: 
    """Tests for one list that is empty concatenated with a nonempty list."""
    first_list: list[int] = []
    second_list: list[int] = [1, 2, 3]
    assert concat(first_list, second_list) == [1, 2, 3]


def test_concat_lists_same_length() -> None:
    """Tests for two lists of same length being concatenated."""
    first_list: list[int] = [1, 2, 3]
    second_list: list[int] = [4, 5, 6]
    assert concat(first_list, second_list) == [1, 2, 3, 4, 5, 6]


def test_concat_lists_different_length() -> None: 
    """Tests for two lists of different length being concatenated."""
    first_list: list[int] = [1, 2, 3]
    second_list: list[int] = [4, 5, 6, 7]
    assert concat(first_list, second_list) == [1, 2, 3, 4, 5, 6, 7]
