import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 1
        found = [None] * len(nums)
        for n in nums:
            if 0 <= n - 1 < len(nums):
                found[n - 1] = True
        num = None
        for i in range(len(found)):
            if found[i] is None:
                num = i + 1
                break
        if num is None:
            num = max(nums) + 1

        return num


def main():
    assert Solution().firstMissingPositive([1,2,0]) == 3
    assert Solution().firstMissingPositive([3,4,-1,1]) == 2
    assert Solution().firstMissingPositive([7,8,9,11,12]) == 1
    assert Solution().firstMissingPositive([]) == 1
    assert Solution().firstMissingPositive([1]) == 2


if __name__ == '__main__':
    main()
