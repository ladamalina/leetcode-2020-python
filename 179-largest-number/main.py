import logging
from functools import cmp_to_key
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0:
            return "0"

        def cmp_func(x, y):
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1

        strs = [str(_) for _ in nums]
        strs.sort(key=cmp_to_key(cmp_func), reverse=True)

        return ''.join(strs).lstrip('0') or '0'


def main():
    assert Solution().largestNumber([10, 2]) == "210"
    assert Solution().largestNumber([3, 30, 34, 5, 9]) == "9534330"


if __name__ == '__main__':
    main()
