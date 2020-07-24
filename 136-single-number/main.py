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
                seen[n] = True

        last = list(seen.keys())[0]
        return last


def main():
    assert Solution().singleNumber([2,2,1]) == 1
    assert Solution().singleNumber([4,1,2,1,2]) == 4
    assert Solution().singleNumber([1]) == 1


if __name__ == '__main__':
    main()
