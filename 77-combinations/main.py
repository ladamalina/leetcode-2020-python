import logging
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def combine_digits(self, nums: List[int], k: int) -> List[List[int]]:
        # logger.debug(f'{nums=}, {k=}')
        if len(nums) == k:
            return [nums]
        elif len(nums) < k:
            return []
        # len(nums) > k

        if k == 1:
            return [[_] for _ in nums]
        # k > 1

        results_w_1 = self.combine_digits(nums[1:], k-1)
        # logger.debug(f'{nums=}, {k=}, {nums[0]=}, {results_w_1=}')
        results_wo_1 = self.combine_digits(nums[1:], k)
        # logger.debug(f'{nums=}, {k=}, {nums[0]=}, {results_wo_1=}')

        # logger.debug(f'{nums=}, {k=}, {nums[0]=}, sum of {nums[0]=} + {results_w_1=}')
        results = [[nums[0]] + _ for _ in results_w_1]
        results.extend(results_wo_1)
        # logger.debug(f'{nums=}, {k=}, {results=}')

        return results

    def combine(self, n: int, k: int) -> List[List[int]]:
        logger.debug('-' * 40)
        logger.debug(f'{n=}, {k=}')
        return self.combine_digits([_ for _ in range(1, n + 1)], k)


def main():
    assert Solution().combine(4, 2) == [
        [1,2],
        [1,3],
        [1,4],
        [2,3],
        [2,4],
        [3,4],
    ]
    Solution().combine(20, 16)


if __name__ == '__main__':
    main()
