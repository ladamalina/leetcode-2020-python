import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        min_n = min(nums)
        max_n = max(nums)

        if min_n > 0:
            return 0
        if max_n == len(nums) - 1:
            return max_n + 1

        real_sum = sum(nums)
        arithm_sum = (len(nums) + 1)*(min_n + max_n)/2
        missing = int(arithm_sum - real_sum)

        return missing


def main():
    assert Solution().missingNumber([3,0,1]) == 2
    assert Solution().missingNumber([9,6,4,2,3,5,7,0,1]) == 8
    assert Solution().missingNumber([0,2]) == 1
    assert Solution().missingNumber([0]) == 1
    assert Solution().missingNumber([1]) == 0


if __name__ == '__main__':
    main()
