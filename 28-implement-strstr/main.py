import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(0, len(haystack)):
            if len(haystack) - i < len(needle):
                return -1
            if haystack[i] != needle[0]:
                continue
            # haystack[i] == needle[0]
            equals = True
            for j in range(0, len(needle)):
                if haystack[i + j] != needle[j]:
                    equals = False
                    break
            if equals:
                return i

        return -1

def main():
    assert Solution().strStr(haystack="hello", needle="ll") == 2
    assert Solution().strStr(haystack="aaaaa", needle="bba") == -1


if __name__ == '__main__':
    main()
