import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_seen = dict()
        i = 0
        while i < len(nums):
            num = nums[i]
            if num in nums_seen:
                if nums_seen[num] >= 2:
                    nums.pop(i)
                    continue
                else:
                    nums_seen[num] += 1
            else:
                nums_seen[num] = 1

            i += 1
        return len(nums)


def main():
    l = [1,1,1,2,2,3]
    assert Solution().removeDuplicates(l) == 5
    assert l == [1,1,2,2,3]

    l = []
    assert Solution().removeDuplicates(l) == 0
    assert l == []

    l = [1]
    assert Solution().removeDuplicates(l) == 1
    assert l == [1]

    l = [1,1]
    assert Solution().removeDuplicates(l) == 2
    assert l == [1,1]

    l = [0,0,1,1,1,1,2,3,3]
    assert Solution().removeDuplicates(l) == 7
    assert l == [0,0,1,1,2,3,3]


if __name__ == '__main__':
    main()
