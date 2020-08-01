import logging
from typing import Dict

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

mem: Dict[int, int] = dict()


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        for i, ch in enumerate(word):
            if i == 0:
                continue
            if ch.islower() and word[i - 1].islower():
                continue
            if ch.isupper() and word[i - 1].isupper():
                continue
            if ch.islower() and word[i - 1].isupper() and i == 1:
                continue
            return False
        return True


def main():
    assert Solution().detectCapitalUse("USA") is True
    assert Solution().detectCapitalUse("Google") is True
    assert Solution().detectCapitalUse("leetcode") is True
    assert Solution().detectCapitalUse("FlaG") is False


if __name__ == '__main__':
    main()
