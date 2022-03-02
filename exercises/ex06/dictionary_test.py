"""Tests for dictionary functions!"""

__author__ = "730412456"


from exercises.ex06.dictionary import invert, favorite_colors, count
import pytest 


def test_invert_single_letters() -> None: 
    """Tests for inverting keys and values that are single letters."""
    dictionary = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(dictionary) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_words() -> None:
    """Tests for inverting key and values that are words."""
    dictionary = {'apple': 'cat', 'banana': 'dog'}
    assert invert(dictionary) == {'cat': 'apple', 'dog': 'banana'}


def test_invert_keyerror() -> None:
    with pytest.raises(KeyError): 
        dictionary = {'chapel': 'hill', 'dirt': 'hill'}
        invert(dictionary)


def test_favorite_colors_one_color() -> None: 
    """Tests for only one color."""
    personal_favs = {'hannah': 'yellow', 'matthew': 'yellow', 'brianna': 'yellow'}
    assert favorite_colors(personal_favs) == 'yellow'


def test_favorite_colors_tie() -> None: 
    """Tests for colors that will tie."""
    personal_favs = {'hannah': 'yellow', 'matthew': 'purple', 'brianna': 'orange'} 
    assert favorite_colors(personal_favs) == 'yellow'


def test_favorite_colors_many() -> None:
    """Tests for many colors."""
    personal_favs = {'hannah': 'yellow', 'matthew': 'purple', 'brianna': 'purple'}
    assert favorite_colors(personal_favs) == 'purple'


def test_count_empty_list() -> None:
    """Tests for an empty list."""
    input_list = []
    assert count(input_list) == {}


def test_count_repeating() -> None:
    """Tests for repeatings str values in a list."""
    input_list = ['a', 'a', 'b', 'c', 'c', 'c']
    assert count(input_list) == {'a': 2, 'b': 1, 'c': 3}


def test_count_non_repeating() -> None:
    """Tests for non-repeating str values in a list."""
    input_list = ['a', 'b', 'c', 'd', 'e']
    assert count(input_list) == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
