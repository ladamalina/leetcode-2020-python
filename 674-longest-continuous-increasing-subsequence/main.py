import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = 0
        current_len = 0
        for i in range(0, len(nums)):
            if i == 0:
                current_len += 1
            else:
                if nums[i] > nums[i - 1]:
                    current_len += 1
                else:
                    current_len = 1
            if current_len > longest:
                longest = current_len

        return longest

def main():
    assert Solution().findLengthOfLCIS([1,3,5,4,7]) == 3
    assert Solution().findLengthOfLCIS([2,2,2,2,2]) == 1
    assert Solution().findLengthOfLCIS([]) == 0
    assert Solution().findLengthOfLCIS([1]) == 1


if __name__ == '__main__':
    main()
