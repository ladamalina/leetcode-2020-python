import logging
import heapq
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half_len = len(nums) / 2
        freq = dict()
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
            if freq[n] > half_len:
                return n


def main():
    assert Solution().majorityElement([3, 2, 3]) == 3
    assert Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2


if __name__ == '__main__':
    main()
