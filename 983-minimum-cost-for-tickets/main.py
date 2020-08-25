import logging
from typing import List, Optional

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        for i in range(1, len(dp)):
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(i - 1, 0)] + costs[0], dp[max(i - 7, 0)] + costs[1], dp[max(i - 30, 0)] + costs[2])

        return dp[-1]


def main():
    assert Solution().mincostTickets([1,4,6,7,8,20], [2,7,15]) == 11
    assert Solution().mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]) == 17


if __name__ == '__main__':
    main()
