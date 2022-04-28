import logging
from collections import defaultdict
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_sums: Dict[int, int] = defaultdict(int)
        prefix_sums[0] = 1
        cnt = 0

        for i, n in enumerate(nums):
            prefix_sum += n
            cnt += prefix_sums.get(prefix_sum - k, 0)
            prefix_sums[prefix_sum] += 1

        return cnt


def main():
    assert Solution().subarraySum([1,1,1], 2) == 2
    assert Solution().subarraySum([2,0,0,0], 2) == 4
    assert Solution().subarraySum([1], 0) == 0


if __name__ == '__main__':
    main()
