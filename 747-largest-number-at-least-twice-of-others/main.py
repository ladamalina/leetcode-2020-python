import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        i1 = None  # largest
        i2 = None  # 2nd large
        for i, n in enumerate(nums):
            if i == 0:
                i1 = i
                continue

            # i > 0
            if nums[i] >= nums[i1]:
                i2 = i1
                i1 = i
            elif i2 is None or nums[i] >= nums[i2]:
                i2 = i

        if nums[i1] >= nums[i2] * 2:
            return i1

        return -1

def main():
    assert Solution().dominantIndex([1,0]) == 0
    assert Solution().dominantIndex([0,0,3,2]) == -1
    assert Solution().dominantIndex([0,0,0,1]) == 3
    assert Solution().dominantIndex([1, 2, 3, 4]) == -1
    assert Solution().dominantIndex([3, 6, 1, 0]) == 1
    assert Solution().dominantIndex([1]) == 0
    assert Solution().dominantIndex([1, 2]) == 1


if __name__ == '__main__':
    main()
