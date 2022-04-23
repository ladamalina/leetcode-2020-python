import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        logger.debug('-' * 40)
        logger.debug(f'{prices=}')
        if len(prices) <= 1:
            return 0

        max_sell_price = 0
        buy_idx = None
        sell_idx = None
        for i in range(0, len(prices)):
            logger.debug(f'{i=}, {prices[i]=}, {buy_idx=}, {sell_idx=}')
            if buy_idx is None:
                if i + 1 < len(prices):
                    if prices[i] < prices[i + 1]:
                        buy_idx = i
                        logger.debug(f'{buy_idx=}, {prices[buy_idx]=}')
                continue

            if buy_idx is not None and sell_idx is None:
                if i + 1 < len(prices):
                    if prices[i] > prices[i + 1]:
                        sell_idx = i
                    else:
                        continue
                else:
                    sell_idx = i
                max_sell_price += prices[sell_idx] - prices[buy_idx]
                buy_idx = None
                sell_idx = None

        return max_sell_price


def main():
    assert Solution().maxProfit([7,1,5,3,6,4]) == 7
    assert Solution().maxProfit([1,2,3,4,5]) == 4
    assert Solution().maxProfit([7,6,4,3,1]) == 0
    assert Solution().maxProfit([7]) == 0
    assert Solution().maxProfit([7,6]) == 0
    assert Solution().maxProfit([2,6]) == 4
    assert Solution().maxProfit([2,2]) == 0
    assert Solution().maxProfit([2,2,2,2,2]) == 0
    assert Solution().maxProfit([2,2,2,0,2,2,2]) == 2


if __name__ == '__main__':
    main()
