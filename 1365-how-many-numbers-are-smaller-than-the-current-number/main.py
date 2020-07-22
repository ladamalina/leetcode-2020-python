import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        nums_dict = dict()
        for i, n in enumerate(sorted_nums):
            if i == 0:
                nums_dict[n] = 0
                continue
            if sorted_nums[i - 1] == sorted_nums[i]:
                continue
            nums_dict[n] = i

        res = [nums_dict[n] for n in nums]

        return res


def main():
    assert Solution().smallerNumbersThanCurrent([8,1,2,2,3]) == [4,0,1,1,3]


if __name__ == '__main__':
    main()
