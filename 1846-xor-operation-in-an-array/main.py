import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        pairs = 0
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    pairs += 1

        return pairs


def main():
    assert Solution().numIdenticalPairs([1,2,3,1,1,3]) == 4
    assert Solution().numIdenticalPairs([1,1,1,1]) == 6
    assert Solution().numIdenticalPairs([1,2,3]) == 0
    assert Solution().numIdenticalPairs([1]) == 0


if __name__ == '__main__':
    main()
