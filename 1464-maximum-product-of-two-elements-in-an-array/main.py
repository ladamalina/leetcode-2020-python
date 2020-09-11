import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()

        return max((nums[0]-1)*(nums[1]-1), (nums[-2]-1)*(nums[-1]-1))


def main():
    assert Solution().maxProduct([3,4,5,2]) == 12
    assert Solution().maxProduct([1,5,4,5]) == 16
    assert Solution().maxProduct([3,7]) == 12


if __name__ == '__main__':
    main()
