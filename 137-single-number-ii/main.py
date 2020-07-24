import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = dict()
        for n in nums:
            if n in seen:
                seen[n] += 1
                if seen[n] == 3:
                    del seen[n]
            else:
                seen[n] = 1

        last = list(seen.keys())[0]
        return last


def main():
    assert Solution().singleNumber([2,2,3,2]) == 3
    assert Solution().singleNumber([0,1,0,1,0,1,99]) == 99
    assert Solution().singleNumber([1]) == 1


if __name__ == '__main__':
    main()
