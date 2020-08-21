from collections import defaultdict

words = ['eat', 'ate', 'done', 'tea', 'soup', 'node']
def printAnagrams(words):
    groupedWords = defaultdict(list)
    for word in words:
        groupedWords["".join(sorted(word))].append(word)

    for group in groupedWords.values():
        print (" ".join(group))

printAnagrams(words)
