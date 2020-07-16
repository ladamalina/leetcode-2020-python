import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0

        first_char_i = None
        last_char_i = None
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if last_char_i is not None:
                    first_char_i = i + 1
                    break
            else:
                if last_char_i is None:
                    last_char_i = i
                else:
                    first_char_i = i
        if last_char_i is None:
            return 0
        else:
            return last_char_i - first_char_i + 1 if first_char_i is not None else 1


def main():
    assert Solution().lengthOfLastWord("Hello World") == 5
    assert Solution().lengthOfLastWord("Hello World ") == 5
    assert Solution().lengthOfLastWord(" World ") == 5
    assert Solution().lengthOfLastWord("World ") == 5
    assert Solution().lengthOfLastWord("W") == 1
    assert Solution().lengthOfLastWord(" ") == 0
    assert Solution().lengthOfLastWord("") == 0


if __name__ == '__main__':
    main()
