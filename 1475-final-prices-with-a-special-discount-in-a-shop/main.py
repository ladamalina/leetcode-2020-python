import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break

        return prices


def main():
    assert Solution().finalPrices([8,4,6,2,3]) == [4,2,4,2,3]
    assert Solution().finalPrices([10,1,1,6]) == [9,0,1,6]
    assert Solution().finalPrices([1,2,3,4,5]) == [1,2,3,4,5]


if __name__ == '__main__':
    main()
