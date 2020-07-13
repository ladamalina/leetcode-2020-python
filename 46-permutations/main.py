import logging
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]

        results = []
        nums_set = set(nums)
        for n in nums:
            results.append([n])

        for i in range(1, len(nums)):
            new_results = []
            for j in range(0, len(results)):
                curr_res = results[j]
                left_nums = list(nums_set - set(curr_res))
                for left_num in left_nums:
                    new_results.append(curr_res + [left_num])
            results = new_results

        return results


def main():
    assert Solution().permute([1]) == [[1]]
    assert Solution().permute([1,2]) == [[1,2], [2,1]]
    assert Solution().permute([1,2,3]) == [
        [1,2,3],
        [1,3,2],
        [2,1,3],
        [2,3,1],
        [3,1,2],
        [3,2,1]
    ]


if __name__ == '__main__':
    main()
