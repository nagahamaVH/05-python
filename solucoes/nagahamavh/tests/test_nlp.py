import pytest
from solucoes.nagahamavh.lib import utils
from solucoes.nagahamavh.lib.aula3 import NLP


@pytest.fixture
def fixture_single_stop_word():
    return "a letra 'a' deve ser removida. olha a letra aqui: a"


@pytest.fixture
def fixture_top_words():
    from collections import Counter

    text = "Poop on grasses scream for no reason at 4 am and annoy kitten brother with poking, for sit in box paw at your fat belly, and meow meow mama. Cats making all the muffins if it fits, i sits. Cereal boxes make for five star accommodation pushed the mug off the table but mewl for food at 4am sniff all the things yet swat turds around the house human give me attention meow but meow meow mama. Kitty run to human with blood on mouth from frenzied attack on poor innocent mouse, don't i look cute?. Peer out window, chatter at birds, lure them to mouth all of a sudden cat goes crazy knock dish off table head butt cant eat out of my own dish cats are cute"
    top_words = utils.sort_dict(dict(Counter(text.split())))

    return [text, top_words]


class TestConstructor:
    def test_int(self):
        with pytest.raises(TypeError):
            NLP(1)

    def test_dict(self):
        with pytest.raises(TypeError):
            NLP({"key": "value"})

    def test_list(self):
        with pytest.raises(TypeError):
            NLP(["This is a list"])


class TestCountWords:
    def test_sort_decreasing(self):
        text = "a c a a a b c b b"
        expected = {"a": 4, "b": 3, "c": 2}
        assert NLP(text).count() == expected

    def test_word_as_part_of_another_word(self):
        from collections import Counter

        text = "When a micro brew is stupid, a Red Stripe caricatures a Pilsner Urquell over an Octoberfest"
        assert NLP(text).count() == utils.sort_dict(dict(Counter(text.split())))

    def test_sort_alphabetic_when_words_have_same_frequency(self):
        text = "a c b 23 *"
        expected = {"*": 1, "23": 1, "a": 1, "b": 1, "c": 1}
        assert NLP(text).count() == expected


class TestSummary:
    def test_summary(self, fixture_top_words):
        from numpy import mean, std

        nlp = NLP(fixture_top_words[0])
        values = list(fixture_top_words[1].values())
        expected = {"mean": mean(values), "std": std(values)}
        assert nlp.summary() == expected


class TestInsertStopWords:
    def test_insert_should_be_string(self, fixture_single_stop_word):
        nlp = NLP(fixture_single_stop_word)
        with pytest.raises(TypeError):
            nlp.insert_stop_words(["a", "ser"])

    def test_insert_registred_stop_word(self):
        nlp = NLP("teste")
        nlp.insert_stop_words("the")
        nlp.insert_stop_words("second")
        nlp.insert_stop_words("the")
        expected = ["the", "second"]
        assert nlp._stop_words == expected


class TestCleanText:
    def test_empty_stop_word(self, fixture_single_stop_word):
        NLP(fixture_single_stop_word).clean_text() == NLP(
            fixture_single_stop_word)

    def test_single_stop_word(self, fixture_single_stop_word):
        nlp = NLP(fixture_single_stop_word)
        nlp.insert_stop_words("a")
        assert nlp.clean_text() == "letra 'a' deve ser removida. olha letra aqui:"

    def test_multiple_stop_words(self):
        text = "a palavra 'a' e 'ser' devem ser removidas. olha a letra aqui: a"
        nlp = NLP(text)
        nlp.insert_stop_words("a")
        nlp.insert_stop_words("ser")
        expected = "palavra 'a' e 'ser' devem removidas. olha letra aqui:"
        assert nlp.clean_text() == expected

    def test_text_has_only_stop_words(self):
        text = "stop word has to stop"
        nlp = NLP(text)
        nlp.insert_stop_words("stop")
        nlp.insert_stop_words("word")
        nlp.insert_stop_words("has")
        nlp.insert_stop_words("to")
        expected = ""
        assert nlp.clean_text() == expected


class TestTopNWords:
    def test_default_n_parameter(self, fixture_top_words):
        nlp = NLP(fixture_top_words[0])
        expected = utils.head_dict(fixture_top_words[1], 10)
        assert nlp.top_n_words() == expected

    def test_n_parameter_should_be_int(self, fixture_top_words):
        nlp = NLP(fixture_top_words[0])
        with pytest.raises(TypeError):
            nlp.top_n_words("23")
