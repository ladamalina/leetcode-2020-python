import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = dict()
        for n in nums:
            if n in seen:
                del seen[n]
            else:
                seen[n] = 1

        return list(seen.keys())


def main():
    assert Solution().singleNumber([1,2,1,3,2,5]) == [3,5]
    assert Solution().singleNumber([1,4]) == [1,4]


if __name__ == '__main__':
    main()
