import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))


def main():
    assert Solution().heightChecker([1,1,4,2,1,3]) == 3
    assert Solution().heightChecker([5,1,2,3,4]) == 5
    assert Solution().heightChecker([1,2,3,4,5]) == 0


if __name__ == '__main__':
    main()
