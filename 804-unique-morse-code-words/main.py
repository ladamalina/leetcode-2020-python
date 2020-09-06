import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        chars = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--.."
        }
        translations = set()
        for w in words:
            t = "".join([chars[ch] for ch in w])
            translations.add(t)

        return len(translations)


def main():
    assert Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]) == 2


if __name__ == '__main__':
    main()
