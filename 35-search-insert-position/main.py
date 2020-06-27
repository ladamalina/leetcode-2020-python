import logging
from bisect import bisect_left
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)


def main():
    assert Solution().searchInsert([1,3,5,6], 5) == 2
    assert Solution().searchInsert([1,3,5,6], 2) == 1
    assert Solution().searchInsert([1,3,5,6], 7) == 4
    assert Solution().searchInsert([1,3,5,6], 0) == 0


if __name__ == '__main__':
    main()
