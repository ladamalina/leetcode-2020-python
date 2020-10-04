import logging
from typing import List, Tuple

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res: Set[Tuple] = set()
        n = sorted(nums)
        for i in range(len(n)-1):
            for j in range(i+1, len(n)):
                if n[j] - n[i] == k:
                    res.add((n[i], n[j]))
                elif n[j] - n[i] > k:
                    break
        return len(res)


def main():
    assert Solution().findPairs([3,1,4,1,5]) == 2
    assert Solution().findPairs([1,2,3,4,5]) == 1
    assert Solution().findPairs([1,3,1,5,4]) == 0
    assert Solution().findPairs([1,2,4,4,3,3,0,9,2,3]) == 3
    assert Solution().findPairs([-1,-2,-3]) == 1


if __name__ == '__main__':
    main()
