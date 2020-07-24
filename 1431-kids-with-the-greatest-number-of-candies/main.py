import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies_num = 0
        for c in candies:
            if c >= max_candies_num:
                max_candies_num = c

        return [c + extraCandies >= max_candies_num for c in candies]


def main():
    assert Solution().kidsWithCandies([2,3,5,1,3], 3) == [True,True,True,False,True]


if __name__ == '__main__':
    main()
