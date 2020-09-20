import logging
import re
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        logger.debug('-' * 40)
        banned_set = set(banned)
        lower_paragraph = paragraph.lower()
        dirty_words = re.split(r'[\W]\s*', lower_paragraph)
        dirty_words = [re.sub(r'([\W])', '', _) for _ in dirty_words if _ > ""]
        clean_words = [_ for _ in dirty_words if _ not in banned_set]
        logger.debug(f'clean_words={clean_words}, banned_set={banned_set}')

        most_freq_word = None
        freq = dict()
        for w in clean_words:
            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1

            if most_freq_word:
                if freq[w] > freq[most_freq_word]:
                    most_freq_word = w
            else:
                most_freq_word = w
        logger.debug(f'freq={freq}')

        return most_freq_word


def main():
    assert Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]) == "ball"
    assert Solution().mostCommonWord("Bob. hIt, baLl", ["bob", "hit"]) == "ball"
    assert Solution().mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]) == "b"


if __name__ == '__main__':
    main()
