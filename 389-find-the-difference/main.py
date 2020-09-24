import logging
from collections import defaultdict

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = defaultdict(lambda: 0)
        for ch in s:
            diff[ch] += 1

        for ch in t:
            diff[ch] -= 1
            if diff[ch] < 0:
                return ch


def main():
    assert Solution().findTheDifference(s="abcd", t="abcde") == "e"


if __name__ == '__main__':
    main()
