import logging
import re
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sets = set()
        result_sets = []
        int_mask = int("1" * len(nums), 2)
        while int_mask >= 0:
            bin_mask = "{0:b}".format(int_mask)
            if len(bin_mask) < len(nums):
                bin_mask = "0" * (len(nums) - len(bin_mask)) + bin_mask
            set_item = []
            for i, bin_pos in enumerate(bin_mask):
                if bin_pos == "1":
                    set_item.append(nums[i])
            set_item.sort()
            tuple_item = tuple(set_item)
            if tuple_item not in sets:
                sets.add(tuple_item)
                result_sets.append(set_item)
            int_mask -= 1

        return result_sets


def main():
    assert Solution().subsetsWithDup([1,2,2]) == [[1,2,2],[1,2],[1],[2,2],[2],[]]


if __name__ == '__main__':
    main()
