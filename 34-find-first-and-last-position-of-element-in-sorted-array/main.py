import logging
from bisect import bisect_left, bisect_right
from typing import List, Tuple

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        logger.debug('-' * 40)
        if not nums:
            return [-1, -1]

        left_index = bisect_left(nums, target)
        logger.debug(f'nums={nums}, target={target}, left_index={left_index}')
        if left_index >= len(nums) or nums[left_index] != target:
            return [-1, -1]

        right_index = bisect_right(nums, target)
        logger.debug(f'nums={nums}, target={target}, right_index={right_index}')
        return [left_index, right_index-1]


def main():
    assert Solution().searchRange([5,7,7,8,8,10], 8) == [3,4]
    assert Solution().searchRange([5,7,7,8,8,10], 6) == [-1,-1]
    assert Solution().searchRange([1], 1) == [0,0]
    assert Solution().searchRange([1], 2) == [-1,-1]
    assert Solution().searchRange([1,1], 1) == [0,1]
    assert Solution().searchRange([], 1) == [-1,-1]


if __name__ == '__main__':
    main()
