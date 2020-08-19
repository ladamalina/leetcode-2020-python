import logging
import re
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        words = S.split(' ')
        for i, w in enumerate(words):
            # If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
            # For example, the word 'apple' becomes 'applema'.
            if w[0].lower() in vowels:
                words[i] = w + 'ma'

            # If a word begins with a consonant (i.e. not a vowel), remove the first letter and
            # append it to the end, then add "ma".
            # For example, the word "goat" becomes "oatgma".
            else:
                words[i] = w[1:] + w[0] + 'ma'

            words[i] = words[i] + 'a' * (i + 1)

        return " ".join(words)


def main():
    assert Solution().toGoatLatin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    assert Solution().toGoatLatin("The quick brown fox jumped over the lazy dog") == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"


if __name__ == '__main__':
    main()
