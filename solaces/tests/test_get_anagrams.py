import pytest
from solaces.lib.aula2 import find_base_words, group_anagrams


@pytest.fixture
def multiple_base_multiple_words():
    words = ["eat", "ate", "done", "tea", "soup", "node"]
    base = ["aet", "aet", "deno", "aet", "opsu", "deno"]
    group = [["eat", "ate", "tea"], ["done", "node"], ["soup"]]
    return [words, base, group]


@pytest.fixture
def one_word_in_list():
    words = ["bac"]
    base = ["abc"]
    group = [["bac"]]
    return [words, base, group]


@pytest.fixture
def multiple_base_single_words():
    words = ["dbc", "abc", "cde"]
    base = ["bcd", "abc", "cde"]
    group = [["abc"], ["dbc"], ["cde"]]
    return [words, base, group]


class TestFindBaseWords:
    def test_multiple_base_repeated_words(self, multiple_base_multiple_words):
        assert find_base_words(
            multiple_base_multiple_words[0]) == multiple_base_multiple_words[1]

    def test_empty_list(self):
        assert find_base_words([]) == []

    def test_one_word_in_list(self, one_word_in_list):
        assert find_base_words(one_word_in_list[0]) == one_word_in_list[1]

    def test_multiple_base_single_words(self, multiple_base_single_words):
        assert find_base_words(
            multiple_base_single_words[0]) == multiple_base_single_words[1]

    def test_incorrect_type_of_input(self):
        with pytest.raises(TypeError):
            find_base_words({"w1": "abc", "w2": "bcd"})

    def test_list_of_lists_is_not_valid(self):
        with pytest.raises(ValueError):
            find_base_words(["eat", ["ate", "done"], "tea", "soup", "node"])

    def test_numbers(self):
        with pytest.raises(TypeError):
            find_base_words([1, 325, 95, 35, 59])


class TestGroupAnagrams:
    def test_multiple_base_repeated_words(self, multiple_base_multiple_words):
        assert group_anagrams(
            multiple_base_multiple_words[0], multiple_base_multiple_words[1]) == multiple_base_multiple_words[2]

    def test_empty_list(self):
        assert group_anagrams([], []) == [[]]

    def test_one_word_in_list(self, one_word_in_list):
        assert group_anagrams(
            one_word_in_list[0], one_word_in_list[1]) == one_word_in_list[2]

    def test_multiple_base_single_words(self, multiple_base_single_words):
        assert group_anagrams(
            multiple_base_single_words[0], multiple_base_single_words[1]) == multiple_base_single_words[2]

    def test_mismatch_input_lengths(self):
        with pytest.raises(ValueError):
            group_anagrams(["eat", "done"], ["aet"])
