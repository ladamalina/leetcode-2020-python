import logging
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def diffArrays(self, l1: List[int], l2: List[int]) -> List[int]:
        l1 = l1[:]
        for el in l2:
            l1.remove(el)
        return l1

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]

        results = []
        nums_set = list(set(nums))
        for n in nums_set:
            results.append([n])

        for i in range(1, len(nums)):
            new_results = []
            for j in range(0, len(results)):
                curr_res = results[j]
                left_nums = self.diffArrays(nums, curr_res)
                for left_num in left_nums:
                    new_result = curr_res + [left_num]
                    try:
                        exists_idx = new_results.index(new_result)
                    except ValueError:
                        new_results.append(curr_res + [left_num])
            results = new_results

        return results


def main():
    assert Solution().permuteUnique([1]) == [[1]]
    assert Solution().permuteUnique([1,1]) == [[1,1]]
    assert Solution().permuteUnique([1,2]) == [[1,2], [2,1]]
    assert Solution().permuteUnique([1,1,2]) == [
        [1,1,2],
        [1,2,1],
        [2,1,1]
    ]


if __name__ == '__main__':
    main()
