import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = globabl_max = None
        for i in range(0, len(nums)):
            current_max = max(nums[i], nums[i] + current_max) if current_max is not None else nums[i]
            if globabl_max is None or current_max > globabl_max:
                globabl_max = current_max

        return globabl_max

def main():
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert Solution().maxSubArray([4]) == 4
    assert Solution().maxSubArray([-1]) == -1


if __name__ == '__main__':
    main()
