import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)


def main():
    l = [0,1,0,3,12]
    Solution().moveZeroes(l)
    assert l == [1,3,12,0,0]

    l = []
    Solution().moveZeroes(l)
    assert l == []

    l = [0,0]
    Solution().moveZeroes(l)
    assert l == [0,0]

    l = [1,2,3]
    Solution().moveZeroes(l)
    assert l == [1,2,3]

    l = [1,0]
    Solution().moveZeroes(l)
    assert l == [1,0]

    l = [0]
    Solution().moveZeroes(l)
    assert l == [0]


if __name__ == '__main__':
    main()
