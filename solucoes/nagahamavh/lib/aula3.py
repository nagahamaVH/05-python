from solucoes.nagahamavh.lib import utils


class NLP:
    def __init__(self, text):
        if not isinstance(text, str):
            raise TypeError
        self._text = str(text)
        self._stop_words = []

    def __str__(self):
        return self._text

    def list_words(self):
        return self._text.split()

    def unique(self):
        return list(set(self.list_words()))

    def count(self):
        counts = {}
        for word in self.list_words():
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return utils.sort_dict(counts)

    def top_n_words(self, n=10):
        if not isinstance(n, int):
            raise TypeError
        return utils.head_dict(self.count(), n)

    def summary(self):
        from numpy import mean, std

        values = list(self.count().values())
        return {"mean": mean(values), "std": std(values)}

    def insert_stop_words(self, stop_word):
        if not isinstance(stop_word, str):
            raise TypeError
        if stop_word not in self._stop_words:
            self._stop_words.append(stop_word)

    def clean_text(self):
        list_words = self.list_words().copy()

        if len(self._stop_words) == 0:
            return self._text
        else:
            for sw in self._stop_words:
                while True:
                    try:
                        list_words.remove(sw)
                    except ValueError:
                        break
            clean = " ".join(list_words)
            return clean

    def export_clean_text(self, file_path):
        form = open(file_path, "w")
        form.write(self.clean_text())
        form.close()
