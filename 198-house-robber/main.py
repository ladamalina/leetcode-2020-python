import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(*nums)

        best_deal = [0] * len(nums)
        best_deal[0] = nums[0]
        best_deal[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            best_deal[i] = max(best_deal[i - 2] + nums[i], best_deal[i - 1])

        return best_deal[-1]


def main():
    assert Solution().rob([1,2,3,1]) == 4
    assert Solution().rob([2,7,9,3,1]) == 12
    assert Solution().rob([7,1,1,7]) == 14
    assert Solution().rob([7]) == 7
    assert Solution().rob([7,1]) == 7
    assert Solution().rob([]) == 0


if __name__ == '__main__':
    main()
