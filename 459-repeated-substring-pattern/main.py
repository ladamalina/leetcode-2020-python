import logging
from typing import Generator

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        sub_len_gen = self.getNextIndex(s)
        sub_len = next(sub_len_gen, None)
        while sub_len is not None:
            if self.checkPattern(s, sub_len):
                return True
            sub_len = next(sub_len_gen, None)

        return False

    def getNextIndex(self, s: str) -> Generator[int, None, None]:
        for i in range(1, len(s)):
            if s[i] == s[0]:
                yield i

        return None

    def checkPattern(self, s: str, sub_len: int) -> bool:
        if len(s) % sub_len != 0:
            return False
        for i in range(sub_len, len(s)):
            if s[i] != s[i % sub_len]:
                return False

        return True


def main():
    assert Solution().repeatedSubstringPattern("abab") is True
    assert Solution().repeatedSubstringPattern("aba") is False
    assert Solution().repeatedSubstringPattern("abcabcabcabc") is True


if __name__ == '__main__':
    main()
