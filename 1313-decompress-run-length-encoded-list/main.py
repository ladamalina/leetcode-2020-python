import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        i = 0
        while i + 1 < len(nums):
            freq = nums[i]
            val = nums[i + 1]
            output.extend([val] * freq)

            i += 2

        return output


def main():
    assert Solution().decompressRLElist([1,2,3,4]) == [2, 4, 4, 4]
    assert Solution().decompressRLElist([1,1,2,3]) == [1,3,3]


if __name__ == '__main__':
    main()
