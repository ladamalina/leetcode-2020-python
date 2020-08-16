import logging
import sys
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        one_buy = two_buy = sys.maxsize
        one_profit = two_profit = 0
        for p in prices:
            one_buy = min(one_buy, p)
            one_profit = max(one_profit, p - one_buy)
            two_buy = min(two_buy, p - one_profit)
            two_profit = max(two_profit, p - two_buy)

        return two_profit


def main():
    assert Solution().maxProfit([3,3,5,0,0,3,1,4]) == 6
    assert Solution().maxProfit([1,2,3,4,5]) == 4
    assert Solution().maxProfit([7,6,4,3,1]) == 0


if __name__ == '__main__':
    main()
