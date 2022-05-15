import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        half = len(s) // 2
        for i in range(0, half):
            left_ch = s[i]
            right_ch = s[i*-1 - 1]
            s[i] = right_ch
            s[i * -1 - 1] = left_ch


def main():
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    assert s == ["o", "l", "l", "e", "h"]

    s = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(s)
    assert s == ["h", "a", "n", "n", "a", "H"]


if __name__ == '__main__':
    main()
