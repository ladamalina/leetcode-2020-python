import logging
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for n in nums:
            if 10 <= n <= 99 or 1000 <= n <= 9999 or n == 100000:
                cnt += 1

        return cnt


def main():
    assert Solution().findNumbers([555,901,482,1771]) == 1
    assert Solution().findNumbers([12,345,2,6,7896]) == 2
    assert Solution().findNumbers([100000]) == 1


if __name__ == '__main__':
    main()
