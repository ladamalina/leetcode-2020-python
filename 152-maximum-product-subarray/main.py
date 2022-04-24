import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mini, maxi, res = 1, 1, -math.inf
        for n in nums:
            a = mini * n
            b = maxi * n
            mini = min(a, b, n)
            maxi = max(a, b, n)
            res = max(res, maxi)

        return res


def main():
    assert Solution().maxProduct([2,3,-2,4]) == 6
    assert Solution().maxProduct([-2,0,-1]) == 0


if __name__ == '__main__':
    main()
