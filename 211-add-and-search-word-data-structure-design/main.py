import logging
from typing import Dict

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._words_list_by_len: Dict[int, list] = dict()
        self._words_set_by_len: Dict[int, set] = dict()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if len(word) in self._words_set_by_len:
            if word not in self._words_set_by_len[len(word)]:
                self._words_list_by_len[len(word)].append(word)
                self._words_set_by_len[len(word)].add(word)
        else:
            self._words_list_by_len[len(word)] = [word]
            self._words_set_by_len[len(word)] = set([word])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if len(word) not in self._words_set_by_len:
            return False

        if "." in word:
            reg = word.replace(".", "[a-z]")
            reg = f"^{reg}$"
            return self._search_regex(word, reg)
        else:
            return self._search_exact(word)

    def _search_regex(self, word: str, reg: str) -> bool:
        import re
        for w in self._words_list_by_len[len(word)]:
            if re.match(reg, w):
                return True

        return False

    def _search_exact(self, word: str) -> bool:
        return word in self._words_set_by_len[len(word)]


def main():
    pass


if __name__ == '__main__':
    main()
