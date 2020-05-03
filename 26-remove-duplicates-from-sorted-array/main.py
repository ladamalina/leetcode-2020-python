import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        for i in range(len(nums)-1, -1, -1):
            if i-1 >= 0 and nums[i] == nums[i-1]:
                nums.pop(i)

        return len(nums)


def main():
    l = [1,1,2]
    assert Solution().removeDuplicates(l) == 2
    assert l == [1,2]

    l = []
    assert Solution().removeDuplicates(l) == 0
    assert l == []

    l = [1]
    assert Solution().removeDuplicates(l) == 1
    assert l == [1]

    l = [1,1,1,2,2,2]
    assert Solution().removeDuplicates(l) == 2
    assert l == [1,2]


if __name__ == '__main__':
    main()
