import logging
from typing import List, Tuple

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        logger.debug('-' * 40)
        logger.debug(f'{prices=}')
        if len(prices) <= 1:
            return 0

        max_profit = 0

        buy_indexes = []
        for i in range(0, len(prices) - 1):
            if i == 0 and prices[i] < prices[i + 1]:
                buy_indexes.append(i)
            elif i > 0 and prices[i - 1] >= prices[i] < prices[i + 1]:
                buy_indexes.append(i)
        logger.debug(f'{buy_indexes=}, buy_prices={[prices[_] for _ in buy_indexes]}')

        for buy_idx in buy_indexes:
            best_sell_idx, best_sell_price = self.getBestSellPrice(prices[buy_idx + 1:])
            profit = best_sell_price - prices[buy_idx]
            logger.debug(f'{buy_idx=}, buy_price={prices[buy_idx]}, {best_sell_idx=}, {best_sell_price=}, {profit=}')
            if profit > max_profit:
                max_profit = profit

        return max_profit

    def getBestSellPrice(self, prices: List[int]) -> Tuple[int, int]:
        max_idx = None
        max_price = None
        for i in range(0, len(prices)):
            if max_idx is None or prices[i] > max_price:
                max_idx = i
                max_price = prices[i]

        return max_idx, max_price


def main():
    assert Solution().maxProfit([7,1,5,3,6,4]) == 5
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
