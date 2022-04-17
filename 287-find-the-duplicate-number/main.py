import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen_nums = set()
        for num in nums:
            if num in seen_nums:
                return num
            else:
                seen_nums.add(num)


def main():
    assert Solution().findDuplicate([1,3,4,2,2]) == 2
    assert Solution().findDuplicate([3,1,3,4,2]) == 3
    assert Solution().findDuplicate([1,4,4,2,4]) == 4


if __name__ == '__main__':
    main()
