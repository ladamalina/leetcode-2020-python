import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run_sum = []
        for i in range(0, len(nums)):
            if i == 0:
                run_sum.append(nums[i])
                continue
            # i > 0
            run_sum.append(run_sum[i - 1] + nums[i])

        return run_sum


def main():
    assert Solution().runningSum([1,2,3,4]) == [1,3,6,10]


if __name__ == '__main__':
    main()
