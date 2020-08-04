import logging
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        int_mask = int("1" * len(nums), 2)
        while int_mask >= 0:
            bin_mask = "{0:b}".format(int_mask)
            if len(bin_mask) < len(nums):
                bin_mask = "0" * (len(nums) - len(bin_mask)) + bin_mask
            set_item = []
            for i, bin_pos in enumerate(bin_mask):
                if bin_pos == "1":
                    set_item.append(nums[i])
            sets.append(set_item)
            int_mask -= 1

        return sets


def main():
    assert Solution().subsets([1,2,3]) == [[1,2,3],[1,2],[1,3],[1],[2,3],[2],[3],[]]


if __name__ == '__main__':
    main()
